## Project directory
--------------------

### Overview
All the `signac` commands are run from the `<local_path>/signac_numpy_tutorial/signac_numpy_tutorial/project` directory, which include, but are not limited to the following commands:
 - State point initialization.
```bash
python init.py
```
 - Checking the project status.
```bash
python project.py status
```
 - Running the project's selected part locally (general example only).
```bash
python project.py run -o <part_x_this_does_a_function_y>
```

  - Submitting the project's selected part to the HPC (general example only).
```bash
python project.py submit -o <part_x_this_does_a_function_y>
```


Additionally, can run the following flags for the  `run` or `submit` commands, controlling the how the jobs are executed or submitted to the HPC:
 - `--bundle 2` : Only available when using `submit`.  This bundles multiple jobs (2 in this case) into a single run or HPC submittion script, auto adjusting the time, CPU cores, etc., based on the total command selections.
  - `--pretend` : Only available when using `submit`.  This is used to output what the submission script will look like, without submitting it to the HPC. 
 - See the `signac` documenation for more information and features.
 - `--parallel 2` : This runs this many jobs in parallel (2 in this case) into a single run or HPC submittion script, auto adjusting the time, CPU cores, etc., based on the total command selections.


 ## templates directory and hpc_setup.py file
---------------------------------------------

### hpc_setup.py file
This file, `hpc_setup.py`, is used to specify the the HPC environment.  The `class` will need to be setup for each HPC (changing the class name and Default environment).  The following also need changed in the `class`:
 - The `template` variable to changed to the custom HPC submission script (the `slurm` `phoenix.sh` file is used here), which is located in the `templates` directory.  
 - The `hostname_pattern` variable to changed to the custom HPC hostname. In this case 'hostname' produced 'login-phoenix-slurm-2.pace.gatech.edu'.  

### Templates directory
This directory is used to store the custom HPC submission scripts and any template files used for the custom workflow (Example: A base template file that is used for a find and replace function, changing the variables with the differing state point inputs).  These find and replace template files could also be put in the `src` directory, but the HPC submission scripts must remain in the `templates` directory.   **All the standard or custom module load commands, conda activate commands, and any other custom items that needed to be HPC submission scripts should in included here for every project (Example: Specific queues, CPU/GPU models, etc.).** 

This specific `phoenix.sh` file is designed to auto-select and submit CPU or GPU Slurm scripts based on what CPUs only or GPUs the user selected for each part of the project (i.e., jobs in the project parts.)