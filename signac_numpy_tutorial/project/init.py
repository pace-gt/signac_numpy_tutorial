"""Initialize signac statepoints to use with row for job submissions."""
# init.py

import os
import numpy as np
import signac
import shutil

# *******************************************
# ENTER THE MAIN USER STATEPOINTS (START)
# *******************************************
# Initialize the signac project
signac.init_project()

# Enter the variable 'values' (integer_only) 
# values_int = [set_0_value_0, set_1_value_0]
values_int = [1, 2]

# Enter the number of replicates desired (replicate_number). 
# replicate_number = [0, 1, 2, 3, 4]
replicate_number = [0, 1]



# *******************************************
# ENTER THE MAIN USER STATEPOINTS (END)
# *******************************************

# Setup the directories in the current directory
print("os.getcwd() = " +str(os.getcwd()))
pr_root = os.getcwd()
pr = signac.get_project(pr_root)


# Set all the statepoints, which will be used to create separate folders 
# for each combination of state points.
all_statepoints = list()

for values_int_i in values_int:
    for replicate_i in replicate_number:
        statepoint = {
            "value_0_int": values_int_i,
            "replicate_number_int": replicate_i,
        }

        all_statepoints.append(statepoint)

# Initiate all statepoint createing the jobs/folders.
for sp in all_statepoints:
    pr.open_job(
        statepoint=sp,
    ).init()

# Delete any analysis files that require analysis
# outside a single workspace file and reset row, 
# as row does not dynamically recheck for completion 
# status after the task is completed.  
# If any previous replicate averages and std_devs exist delete them, 
 # because they will need recalculated as more state points were added.

main_analysis_dir_path_and_name = "analysis"
try:
    if os.path.isdir(f'{main_analysis_dir_path_and_name}'):
        shutil.rmtree(f'{main_analysis_dir_path_and_name}')
except:
    print(
        f"No directory named "
        f"'{main_analysis_dir_path_and_name}' exists."
        )

# The 'avg_std_dev_calculated.txt' file are auto-deleted when 
# the 'init.py' file is run.  So if there are errors with this, 
# you can run 'python init.py' and it will reset it, so you can 
# rerun it. 
# This also resets and recalculated the completion status.
try:
    # Delete the 'avg_std_dev_calculated.txt' file
    exec_delete_avg_std_dev_file = subprocess.Popen(
        "rm workspace/*/avg_std_dev_calculated.txt", 
        shell=True, 
        stderr=subprocess.STDOUT
    )
    os.wait4(exec_delete_avg_std_dev_file.pid, os.WSTOPPED)

    # Clean and reset row's completion status
    exec_reset_row_status = subprocess.Popen(
        "row clean --completed && row scan", 
        shell=True, 
        stderr=subprocess.STDOUT
    )
    os.wait4(exec_reset_row_status.pid, os.WSTOPPED)

except:
    print(
        f"ERROR: Unable to delete the 'avg_std_dev_calculated.txt' file or clean and scan workspace progress.") 
