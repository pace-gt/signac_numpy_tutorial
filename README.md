# Signac and Row Workflow Tutorial: Basic Numpy Calculations
----------------------------------------------------

## General Notes

Using `signac` and `row` workflows provide the following benefits: 

 - The `signac` and `row` workflows provide contained and totally reproducible results, since all the project steps and calculations are contained within this a single `signac`/`row` project. Although, to ensure total reproduciblity, the project should be run from a container.  Note: This involves building a container (Docker, Apptainer, Podman, etc.), using it to run the original calculations, and providing it the future parties that are trying to reproduce the exact results.

 - The `signac` and `row` workflows can simply track the progress of any project locally or on the HPC, providing as much or a little details of the project status as the user programs into the `actions.py` and `workflow.toml` file.  Note: `row` tracks the progress and completion of a project step or section by determining if a file exists.  Therefore, the user can generate this file after a verification step is performed to confirm a sucessful completion or commands run without error (Exampe: `Exit Code 0`).  

 - These `signac` and `row` workflows are designed to track the progress of all the project's parts or stages, only resubmitting the jobs locally or to the HPC if they are not completed or not already in the queue.
 
 - These `signac` and `row` workflows also allow colleagues to quickly transfer their workflows to each other, and easily add new state points to a project, without the fear of rerunning the original state points.  

 - Please also see the [signac website](https://signac.io/) and [row website](https://row.readthedocs.io/), which outlines some of the other major features. 


## Overview

This is a `signac` and `row` workflow example/tutorial for a simple `numpy` calculation, which utilizes the following workflow steps:

 - **Part 1:** For each individual job (set of state points), this code generates the `signac_job_document.json` file from the `signac_statepoint.json` data.  The `signac_statepoint.json` only stores the set of state points or required variables for the given job.  The `signac_job_document.json` can be used to store any other variables that the user wants to store here for later use or searching. 

- **Part 2:** This writes the input values into a file that `numpy` will use to do a calculation in `Part 3`.  There are four (4) random numbers generated that used the initial `value_0_int` value and the `replicate_number_int` value to seed the random number generator.

- **Part 3:** Calulates the dot product of the four (4) random numbers generated in `Part 2` (4 numbers dot [1, 2, 3, 4]).  Also, runs a bash command `echo "Running the echo command or any other bash command here"`, which is an example of how to run a bash command to run a software package inside the commands for each state point. 

- **Part 4:** Obtains the average and standard deviation for each input `value_0_int` value across all the replicates, and prints the output data file (`analysis/output_avg_std_of_replicates_txt_filename.txt`).  Signac is setup to automatically loop through all the json files (`signac_statepoint.json`), calculating the average and standard deviation for the jobs with the state points that only have a different `replicate_number_int` numbers. 

### Notes:
- **`src` directory:** This directory can be used to store any custom function that are required for this workflow.  This includes any developed `Python` functions or any template files used for the custom workflow (Example: A base template file that is used for a find and replace function, changing the variables with the differing state point inputs).

## Resources
 - The [signac documentation](https://signac.io/), [row documentation](https://row.readthedocs.io/), [signac GitHub](https://github.com/glotzerlab/signac), and [row GitHub](https://github.com/glotzerlab/row) and can be used for reference.

## Citation
-----------
Please cite this GitHub repository and the following repositories:

 - [signac GitHub](https://github.com/glotzerlab/signac)
 - [row GitHub](https://github.com/glotzerlab/row)

## Installation
---------------
The signac workflows for "this project" can be built using `mamba`.  Alternatively, you use can use `micromamba` or `miniforge`,  supplimenting `micromamba` or `conda`, respectively for `mamba` when using them.  

If you are using an HPC, you will likely need the below command or a similar command to load the correct python package manager.

```bash
module load mamba
```

The following steps can be used to build the environment:

```bash
cd signac_numpy_tutorial
```

```bash
mamba env create -f environment.yml
```

```bash
mamba activate signac_numpy_tutorial
```

## HPC setup file
-----------------
The `clusters.toml` file is used to specify the the HPC environment.  The specific HPC will need to be setup for each HPC and identified on the `workflow.toml` file.    

The following files are located here:

```bash
cd <you_local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project
```

### **Modify and add the `clusters.toml` file:**


- Modify the `clusters.toml` file to fit your HPC.
  1. This means replacing the **`<ADD_YOUR_HPC_NAME_STRING>`** values with your custom values. For Example at GT, `<ADD_YOUR_HPC_NAME_STRING>` is replaced with `"phoenix"`.
  2. You also may need to change the `"LMOD_SYSHOST"` environment variable to match how your specific HPC is setup. 

- **Add the modified cluster configuration file (`clusters.toml`) to the following location on the HPC under your account (`~/.config/row/clusters.toml`).**

```bash
cp clusters.toml ~/.config/row/clusters.toml
```

### **Modify and add the `workflow.toml` file:**
- Modify the `workflow.toml` file to fit your HPC.
  1. Replace the **`<ADD_YOUR_HPC_NAME>`**
  2. **`<ADD_YOUR_CHARGE_ACCOUNT_NAME>`** values with your custom values.
     
- Modify the slurm submission script, or modify the `workflow.toml` file to your cluster's partitions that you want to use, you can do that with the below addition to the `workflow.toml` file.

For parts 1, 2, and 4, add the CPU partion(s) you want to use:

    ```bash
    custom = ["","--partition=cpu-1,cpu-1,cpu-3"]
    ```

For part 3, add the GPU partion(s) you want to use:

    ```bash
    custom = ["","--partition=gpu-1,gpu-1,gpu-3"]
    ```

Note: As needed, the cluster partitions in the `clusters.toml` can be fake ones.  Then specifying the fake or real partition selection in the `workflow.toml` file (i.e., `partition=fake_partition_name`), allows you just override the selected partition and allow many real partitions in the `workflow.toml` (i.e., `custom = ["","--partition=cpu-1,cpu-1,cpu-3"]`), which is used to write the `Slurm` submission script.
- This can also be done if >1 or more partitions is needed.

## Testing the setup for running only locally, **not on an HPC**.  However, if `row submit` is run locally like this, then you must remove the HPC parts in the `workflow.toml` file (see the notes in the `workflow.toml`).

**Build the test workspace:**     

```bash
python init.py
```

**Run the following command as the test all available submissions or just from a spr:**     

```bash
row submit --dry-run
```

**You should see an output that looks something like this (<u>export ACTION_CLUSTER=\`none\`</u>) in the output if it is working:**

```bash
...

directories=(
be31aae200171ac52a9e48260b7ba5b1
)

export ACTION_WORKSPACE_PATH=workspace
export ACTION_CLUSTER=`none`

...
```

**Clean up row and delete the test workspace:**    

```bash
row clean
```

```bash
rm -r workspace
```

## Testing the setup for running **on an HPC**.

**Build the test workspace:**     

```bash
python init.py
```

**Run the following command as the test:**   

```bash
row submit --dry-run
```
    
**You should see an output that looks something like this (<u>export ACTION_CLUSTER=\`<YOUR_HPC_NAME>\`</u>) in the output if it is working:**

```bash
...

directories=(
be31aae200171ac52a9e48260b7ba5b1
)

export ACTION_WORKSPACE_PATH=workspace
export ACTION_CLUSTER=`<YOUR_HPC_NAME>`

...
```

**Clean up row and delete the test workspace:**    

```bash
row clean
```

```bash
rm -r workspace
```
