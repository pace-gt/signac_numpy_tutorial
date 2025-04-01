## Project directory
--------------------

### Overview
All the `signac` and `row` commands are run from the `<local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project` directory, which include, but are not limited to the following commands:

This can be done at the start of a new project, but is not always required. If you moved the directory after starting a project or signac can not find the path correctly, you will need to run the following command (`signac init`) from the `project` directory:

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
 - Running the project's selected part locally (general example only).  See the `row show status` output for the part names.

    **Run the following command and review the output to make sure it is submitting the correct slurm scripts:**:**
    ```bash
    row submit --dry-run
    ```

  - Submitting the project's selected part to the HPC (general example only).  See the `python project.py status` output for the part names.

    **Run the following command and review the output to make sure it is submitting the correct slurm scripts:**:**
    ```bash
    row submit --dry-run
    ```

    **Run the following command:**
    ```bash
    row submit --action <part_x_this_does_a_function_y>
    ```

Some documention references:

- See the [sigac documenation](https://docs.signac.io/) for more information, features, and the how to populate the workspace with the init.py file.
- See the [row documenation](https://row.readthedocs.io/) for information on setting up and executing the workflows and job submissions. 

NOTES:
- `Row` status tracking is done only by looking for specific files located in the `workspace/*/` directories (i.e., for each state point).

- When using the `row submit` command, you can run utilize flags to control the how the jobs are submitted to the HPC. 

- `Warning`, the user should always confirm the job submission to the HPC is working properly before submitting jobs using the `--dry-run` flag.  This may involve programming the correct items in the custom HPC submission script (i.e., the `workflow.toml` file) as needed to make it work for their unique setup. 


### HPC setup file
------------------
The `clusters.toml` file is used to specify the the HPC environment.  The specific HPC will need to be setup for each HPC and identified on the `workflow.toml` file.    

- **Add the cluster configuration file (`clusters.toml`) to the following location on the HPC under your account (`~/.config/row/clusters.toml`).**
- Modify the `clusters.toml` file to fit your HPC (Example: Replace the <ADD_YOUR_HPC_NAME_STRING> values with your custom values.)
- Modify the `workflow.toml` file to fit your HPC (Example: Replace the <ADD_YOUR_HPC_NAME> and <ADD_YOUR_CHARGE_ACCOUNT_NAME> values with your custom values.)
- If you need to add custom parts to the slurm submission script, or modify the `workflow.toml` file to your partitions, you can do that with the below addition to the `workflow.toml` file.

```bash
custom = ["","--partition='cpu-1, cpu-1, cpu-3'"]
```

If needed, the cluster partitions can be ones that are made up, to select the proper memory per CPU or GPU, and the real paritions can be specificed in the `workflow.toml` file, under the `custom` section (see below and in the `workflow.toml` file). In the near future, `row` may encorporate a feature to select the job memory at the `workflow.toml` file, but this can be a workaround until that is available, and be used as a good example without providing any HPC details.
- Note: The `clusters.toml` file currently sets the memory based only on the partitions.  
- This can also be done if >1 or more partitions is needed.

```bash
...
[action.submit_options.<HPC_NAME>]
account = "<YOUR_CHARGE_ACCOUNT_NAME>"
setup = """
module load conda
conda activate signac_numpy_tutorial
"""
custom = ["","--partition='cpu-1, cpu-1, cpu-3'"]
...
```

- Testing the setup for running only locally, **not on an HPC**.

    **Run the following command:**
    ```bash
    row submit --dry-run
    ```

    **You should see an output that looks something like this in the output if it is working:**

    ...

    directories=(
    be31aae200171ac52a9e48260b7ba5b1
    )

    export ACTION_WORKSPACE_PATH=workspace
    export ACTION_CLUSTER=`none`

    ...

   **Run the following part of the workflow:**

    ```bash
    row submit --action <part_x_this_does_a_function_y>
    ```

  - Testing the setup for running **on an HPC**.

    **Run the following command:**
    ```bash
    row submit --dry-run
    ```
    
    **You should see an output that looks something like this in the output if it is working:**

    ...

    directories=(
    be31aae200171ac52a9e48260b7ba5b1
    )

    export ACTION_WORKSPACE_PATH=workspace
    export ACTION_CLUSTER=`<YOUR_HPC_NAME>`
    
    ...

    **Run the following part of the workflow:**
    ```bash
    row submit --action <part_x_this_does_a_function_y>
    ```