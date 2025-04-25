# Project directory
-------------------

## Overview
All the `signac` and `row` commands are run from the `<local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project` directory, which include, but are not limited to the following commands:

The `signac init` command can be done at the start of a new project, but is not always required. If you moved the directory after starting a project or signac can not find the path correctly, you will need to run the following command (`signac init`) from the `project` directory:

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

 - Submitting and running all the project's available parts (general example only).  See the `row show status` output for the part names. This can also be uese for local project running, which all depends on the system and the `cluster.toml` that is used.

    **Run the following command and test/review the output to make sure it is submitting the correct slurm scripts or local output:**
    ```bash
    row submit --dry-run
    ```

    **Run the following command to submit or execute all the available jobs:**
   ```bash
    row submit
    ```

- Submitting all the project's available parts/sections to be run (general example only).  See the `row show status` output for the part names. This can also be uese for local project running, which all depends on the system and the `cluster.toml` that is used.

    **Run the following command and review the output to make sure it is submitting the correct slurm scripts or local output:**:**
    ```bash
    row submit --action <part_x_this_does_a_function_y> --dry-run
    ```

    **Run the following command to submit or execute all the available jobs for that part or section:**
    ```bash
    row submit --action <part_x_this_does_a_function_y>
    ```

### Submit the workflow jobs locally or to an HPC, depending on the `workflow.toml` file setup. 

Please also look [here](https://row.readthedocs.io/en/0.4.0/workflow/action/submit-options.html) for more details on the HPC setup.

## Run this project.

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

Some documention references:

- See the [sigac documenation](https://docs.signac.io/) for more information, features, and the how to populate the workspace with the init.py file.
- See the [row documenation](https://row.readthedocs.io/) for information on setting up and executing the workflows and job submissions. 

NOTES:
- `Row` status tracking is done only by looking for specific files located in the `workspace/*/` directories (i.e., for each state point).

- When using the `row submit` command, you can run utilize flags to control the how the jobs are submitted to the HPC. 

- `Warning`, the user should always confirm the job submission to the HPC is working properly before submitting jobs using the `--dry-run` flag.  This may involve programming the correct items in the custom HPC submission script (i.e., the `workflow.toml` file) as needed to make it work for their unique setup. 


