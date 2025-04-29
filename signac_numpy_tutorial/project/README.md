# Project directory
-------------------

## Overview
All the `signac` and `row` commands are run from the `<local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project` directory, which include, but are not limited to the following commands:

- The signac workflows for "this project" can be built using `mamba`.  Alternatively, you use can use `micromamba` or `miniforge`,  supplimenting `micromamba` or `conda`, respectively for `mamba` when using them.  

If you are using an HPC, you will likely need the below command or a similar command to load the correct python package manager.  

```bash
module load mamba
```

Activate the environment:

```bash
mamba activate signac_numpy_tutorial
```

The `signac init` command can be done at the start of a new project, but is not always required. If you moved the directory after starting a project or signac can not find the path correctly, you may need to run the following command (`signac init`) from the `project` directory:

```bash
signac init
```

 - State point initialization.
    ```bash
    python init.py
    ```
 - Checking the project status.
    ```bash
    row show status
    ```

 - **All Available Project Parts:**  Submit and run all the available jobs from all the parts.
   1. See the `row show status` output for the part names.
   2. Note: This can be run on the HPC or locally.  However, if `row submit` is run locally like this, then you must remove the HPC parts in the `workflow.toml` file (see the notes in the `workflow.toml`).

    **Run the following command and test/review the output to make sure it is submitting the correct slurm scripts or local output:**
    ```bash
    row submit --dry-run
    ```

    **Run the following command to submit or execute all the available jobs:**
   ```bash
    row submit
    ```

- **Specific Project Parts:**  Submit and and run all the available jobs from specific the parts.
  1. See the `row show status` output for the part names.
  2. Note: This can be run on the HPC or locally.  However, if `row submit` is run locally like this, then you must remove the HPC parts in the `workflow.toml` file (see the notes in the `workflow.toml`).

    **Run the following command and review the output to make sure it is submitting the correct slurm scripts or local output:**:**
    ```bash
    row submit --action <part_x_this_does_a_function_y> --dry-run
    ```

    **Run the following command to submit or execute all the available jobs for that part:**
    ```bash
    row submit --action <part_x_this_does_a_function_y>
    ```

## Submit the workflow jobs locally or to an HPC, depending on the `workflow.toml` file setup. 

Please also look [here](https://row.readthedocs.io/en/0.4.0/workflow/action/submit-options.html) for more details on the HPC setup.

## Setup the Run this project.

All commands in this section are run from the `<local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project` directory.

The `signac init` command can be done at the start of a new project, but is not always required. If you moved the directory after starting a project or signac can not find the path correctly, you will need to run the following command (`signac init`) from the `project` directory:

```bash
signac init
```

In general, check the status of the workflows buy running `row show status` and `row submit --dry-run` before each submission to ensure each workflow part is not written in a way that is computationally expensive.  

```bash
row show status
```

```bash
row submit --dry-run
```

Initialize all the state points for the jobs (generate all the separate folders and state points).  
 - Note: This command generates the `workspace` folder, which includes a sub-folder for each state point (different variable or replicate combinations),  These sub-folders are numbered uniquely based of the state point values.  The user can add more state points via the `init.py` file at any time, running the below command to create the new state points files and sub-folders that are in the `init.py` file.

 ```bash
python init.py
```

Check the status of your project (i.e., what parts are completed and what parts are available to be run).

```bash
row show status
```

## These are two (2) different ways to submit jobs (see below):

1. ### **All Available Project Parts:**  Submit and run the all available jobs with `row submit`:
   - Run `all available jobs for the whole project` locally with the `submit` command. 
Note: This needs to be done for each part as it only submits the available parts to the scheduler.

 ```bash
 row submit
 ```

- Checking the project status.
  
 ```bash
 row show status
 ```

- When the new jobs are ready, repeat this cycle until all jobs and the project is completed.
  

2. ### **Specific Project Parts:**  Submit and and run all the available jobs from specific the part with `row submit --action <part_x_this_does_a_function_y>`.
 - Run all available `part 1` sections of the project locally with the `submit` command.

```bash
row submit --action part_1_initial_parameters_command
```

 - Checking the project status via the belw and move forward when the next part is ready to be submitted..
  
 ```bash
 row show status
 ```

 - Run all available `part 2` sections of the project locally with the `submit` command.

```bash
row submit --action part_2_write_numpy_input_command
```

 - Checking the project status via the belw and move forward when the next part is ready to be submitted..
  
 ```bash
 row show status
 ```

 - Run all available `part 3` sections of the project locally with the `submit` command.

```bash
row submit --action part_3_numpy_calcs_command
```

 - Checking the project status via the belw and move forward when the next part is ready to be submitted..
  
 ```bash
 row show status
 ```

 - Run all available `part 4` sections of the project locally with the `submit` command.

```bash
row submit --action part_4_analysis_replicate_averages_command
```

## Documention References:

- See the [sigac documenation](https://docs.signac.io/) for more information, features, and the how to populate the workspace with the init.py file.
- See the [row documenation](https://row.readthedocs.io/) for information on setting up and executing the workflows and job submissions. 

NOTES:
- `Row` status tracking is done only by looking for specific files located in the `workspace/*/` directories (i.e., for each state point).

- When using the `row submit` command, you can run utilize flags to control the how the jobs are submitted. 

- `Warning`, the user should always confirm the job submission to the HPC is working properly before submitting jobs using the `--dry-run` flag.  This may involve programming the correct items in the custom submission script (i.e., the `workflow.toml` file) as needed to make it work for their unique setup. 


