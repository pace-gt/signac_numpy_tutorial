## Signac Workflow Tutorial: Basic Numpy Calculations
----------------------------------------------------

### General Notes

Using `signac` and `row` workflows provide the following benefits: 

 - The `signac` and `row` workflows provide contained and totally reproducible results, since all the project steps and calculations are contained within this a single `signac` project. Although, to ensure total reproduciblity, the project should be run from a container.  Note: This involves building a container (Docker, Apptainer, Podman, etc.), using it to run the original calculations, and providing it the future parties that are trying to reproduce the exact results.

 - The `signac` and `row` workflows can simply track the progress of any project on locally or on the HPC, providing as much or a little details of the project status as the user programs into the `project.py` file. 

 - These `signac` and `row` workflows are designed to track the progress of all the project's parts or stages, only resubmitting the jobs locally or to the HPC if they are not completed or not already in the queque.  
 
 - These `signac` and `row` workflows also allow colleagues to quickly transfer their workflows to each other, and easily add new state points to a project, without the fear of rerunning the original state points.  

 - Please also see the [signac website](https://signac.io/) and [row website](https://row.readthedocs.io/), which outlines some of the other major features. 


### Overview

This is a `signac` and `row` workflow example/tutorial for a simple Numpy calculation, which utilizes the following workflow steps:

 - **Part 1:** For each individual job (set of state points), this code generates the `signac_job_document.json` file from the `signac_statepoint.json` data.  The `signac_statepoint.json` only stores the set of state points or required variables for the given job.  The `signac_job_document.json` can be used to store any other variables that the user wants to store here for later use or searching. 

- **Part 2:** This writes the input values into a file that `Numpy` will use to do a calculation in `Part 3`.  There are four (4) random numbers generated that used the initial `value_0_int` value and the `replicate_number_int` value to seed the random number generator.

- **Part 3:** Calulate the dot product of the four (4) random numbers generated in `Part 2` (4 numbers dot [1, 2, 3, 4]).  Also, run a bash command `echo "Running the echo command or any other bash command here"`, which is an example of how to run a bash command to run a software package inside the commands for each state point. 

- **Part 4:** Obtain the average and standard deviation for each input `value_0_int` value across all the replicates, and print the output data file (`analysis/output_avg_std_of_replicates_txt_filename.txt`).  Signac is setup to automatically loop through all the json files (`signac_statepoint.json`), calculating the average and standard deviation for the jobs with the state points that only have a different `replicate_number_int` numbers. 

#### Notes:
- **src directory:** This directory can be used to store any custom function that are required for this workflow.  This includes any developed `Python` functions or any template files used for the custom workflow (Example: A base template file that is used for a find and replace function, changing the variables with the differing state point inputs).

### Resources
 - The [signac documentation](https://signac.io/), [row documenation](https://row.readthedocs.io/), [signac GitHub](https://github.com/glotzerlab/signac), and [row GitHub](https://github.com/glotzerlab/row) and can be used for reference.

### Citation

Please cite this GitHub repository.

 - This repository:  Add repository here

### Installation

These signac workflows "this project" can be built using `mamba`.  Alternatively, you can suppliment `conda` for `mamba` if you are using `conda`:

```bash
cd signac_numpy_tutorial
```

```bash
mamba env create -f environment.yml
```

```bash
mamba activate signac_numpy_tutorial
```

### Submit the Workflow Jobs locally or to an HPC, depending on the `workflow.toml` file setup. 

All commands in this section are run from the `<local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project` directory.

This can be done at the start of a new project, but is not always required. If you moved the directory after starting a project or signac can not find the path correctly, you will need to run the following command (`signac init`) from the `project` directory:

```bash
signac init
```

In general, check the status of the workflows buy running `row show status` and `row submit --dry-run` before each submission to ensure each workflow part is not written in a way that is computationally expensive.  

Initialize all the state points for the jobs (generate all the separate folders with the same variables).  
 - Note: This command generates the `workspace` folder, which includes a sub-folder for each state point (different variable combinations),  These sub-folders are numbered uniquely based of the state point values.  The user can add more state points via the `init.py` file at any time, running the below command to create the new state points files and sub-folders that are in the `init.py` file.

 ```bash
python init.py
```

Check the status of your project (i.e., what parts are completed and what parts are available to be run).

```bash
row show status
```

Run `all available jobs for the whole project` locally with the `submit` command.  Note: Using the run command like this will run all parts of the projects until completion.  Note: This feature is not available when submitting to HPCs.

```bash
row submit
```

Run all available `part 1` sections of the project locally with the `submit` command.

```bash
row submit --action part_1_initial_parameters_command
```

Run all available `part 2` sections of the project locally with the `submit` command.

```bash
row submit --action part_2_write_numpy_input_command
```

Run all available `part 3` sections of the project locally with the `submit` command.

```bash
row submit --action part_3_numpy_calcs_command
```

Run all available `part 4` sections of the project locally with the `submit` command.

```bash
row submit --action part_4_analysis_replicate_averages_command
```
