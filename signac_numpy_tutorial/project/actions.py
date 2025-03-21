"""Basic example of a signac project"""
# project.py

import argparse
import os
import numpy as np
import warnings
import signac
import shutil

import hpc_setup


# ******************************************************
# TYPICAL USER VARIBLES THAT CHANGE (START)
# ******************************************************

# Set the walltime, memory, and number of CPUs and GPUs needed
# for each individual job, based on the part/section.
# *******************************************************
# *******************   WARNING   ***********************
# It is recommended to check all HPC submisstions with the
# '--pretend' command so you do not make an errors requesting 
# the CPUs, GPUs, and other parameters by its value 
# that many cause more resources to be used than expected,
# which may result in higher HPC or cloud computing costs! 
# *******************   WARNING   ***********************
# *******************************************************

# *******************************************************
# *******************   Notes   ************************* 
# The following input parameters are all entered as if 
# you were doing a single job when submitting a single 
# schedular script, or running it as single job locally:
# - part_1_ntasks_int = integer
# - part_1_cpus_per_task_int = integer
# - part_1_gpus_per_task_int = integer
# - part_1_mem_per_cpu_gb  = integer or float
# - part_1_walltime_hr = integer or float
# *******************   Notes   ************************* 
# *******************************************************

part_1_ntask_int = 1
part_1_cpus_per_task_int = 2
part_1_gpus_per_task_int = 1
part_1_mem_per_cpu_gb = 4
part_1_walltime_hr = 0.25

part_2_ntask_int = 1
part_2_cpus_per_task_int = 1
part_2_gpus_per_task_int = 0
part_2_mem_per_cpu_gb = 4
part_2_walltime_hr = 0.5

part_3_ntask_int = 1
part_3_cpus_per_task_int = 1
part_3_gpus_per_task_int = 1
part_3_mem_per_cpu_gb = 4
part_3_walltime_hr = 0.75

part_4_ntask_int = 1
part_4_cpus_per_task_int = 1
part_4_gpus_per_task_int = 0
part_4_mem_per_cpu_gb = 4
part_4_walltime_hr = 1

# ******************************************************
# TYPICAL USER VARIBLES THAT CHANGE (END)
# ******************************************************


# ******************************************************
# SIGNAC MAIN CODE SECTION (START)
# ******************************************************

# ******************************************************
# NON-CHANGEABLE VARIABLES 
# NOTE: CAN CHANGE IF MANUALLY CHANGING THE
# 'workflow.toml' ALSO (START)
# ******************************************************
# file names extensions are added later 
# NOTE: DO NOT CHANGE NAMES AFTER STARTING PROJECT, ONLY AT THE BEGINNING
numpy_input_filename_str = "numpy_input_file"
numpy_output_filename_str = "numpy_output_file"
output_avg_std_of_replicates_txt_filename = "output_avg_std_of_replicates_txt_filename"
# ******************************************************
# NON-CHANGEABLE VARIABLES 
# NOTE: CAN CHANGE IF MANUALLY CHANGING THE
# 'workflow.toml' ALSO (ENT)
# ******************************************************

# SET THE PROJECTS DEFAULT DIRECTORY
project_directory = f"{os.getcwd()}"
print(f"project_directory = {project_directory}")

# ******************************************************
# CREATE THE INITIAL VARIABLES, WHICH WILL BE STORED IN 
# EACH JOB (START)
# ******************************************************

# Get the intial paramaters
def part_1_initial_parameters_command(*jobs):
    """Set the system's job parameters in the json file."""
    # The "signac_job_document.json" file needs to be the 'product'
    # for the workflow.toml file.

    for job in jobs:
        # Note: the sp=setpoint variables (from init.py file), doc=user documented variables
        
        # Creating a new json file with user built variables (doc)
        job.doc.value_0_int = job.sp.value_0_int

        # Manipulating the set points (sp) variables from the init.py file and making new variables
        # Here we are simply adding 1, 2, and 3. 
        # NOTE: Values mported as strings, so they need converted to integers
        job.doc.value_1_int = int(int(job.sp.value_0_int) + 1)
        job.doc.value_2_int = int(int(job.sp.value_0_int) + 2)
        job.doc.value_3_int = int(int(job.sp.value_0_int) + 3)  

        # Print the replicate number on the .doc file also
        job.doc.replicate_number_int = job.sp.replicate_number_int
        
# ******************************************************
# CREATE THE INITIAL VARIABLES, WHICH WILL BE STORED IN 
# EACH JOB (END)
# ******************************************************

# ******************************************************
# CREATE THE NUMPY FILE TO READ OR INPUT FILE (START)
# ******************************************************

# Write numpy input command
def part_2_write_numpy_input_command(*jobs):
    """write the numpy input"""
    # The "numpy_input_file.txt" file needs to be the 'product'
    # for the workflow.toml file.

    for job in jobs:
        # get the integer values in the created json file with a random number generater
        numpy_input_value_0_int = int(int(job.doc.value_0_int) * 
                                    np.random.default_rng(seed=int(job.doc.replicate_number_int) + 1).integers(1, high=1000))
        numpy_input_value_1_int = int(int(job.doc.value_1_int) * 
                                    np.random.default_rng(seed=int(job.doc.replicate_number_int) + 2).integers(1, high=1000))
        numpy_input_value_2_int = int(int(job.doc.value_2_int) *
                                    np.random.default_rng(seed=int(job.doc.replicate_number_int) + 3).integers(1, high=1000))
        numpy_input_value_3_int = int(int(job.doc.value_3_int) * 
                                    np.random.default_rng(seed=int(job.doc.replicate_number_int) + 4).integers(1, high=1000))

        init_numpy_file = open(
            job.fn(f"{numpy_input_filename_str}.txt"),
        "w"
        )
        init_numpy_file.write('{: <20} {: <20} {: <20} {: <20}'.format(
            numpy_input_value_0_int,
            numpy_input_value_1_int,
            numpy_input_value_2_int,
            numpy_input_value_3_int,
            )
        )
        init_numpy_file.close()
        
        # check for file completion and print completion text file
        if job.isfile(f"{numpy_input_filename_str}_in_progress.txt"):
            os.rename(
                job.fn(f"{numpy_input_filename_str}_in_progress.txt"),
                job.fn(f"{numpy_input_filename_str}.txt")
            )

            

# ******************************************************
# CREATE THE NUMPY FILE TO READ OR INPUT FILE  (END)
# ******************************************************

# ******************************************************
# PERFORM THE NUMPY CALCULATIONS (START)
# ******************************************************

def part_3_numpy_calcs_command(*jobs):
    """Run the numpy calculations and any other bash command."""
    # The "numpy_output_file.txt" file needs to be the 'product'
    # for the workflow.toml file.

    for job in jobs:
        # Read the numpy input file and conduct numpy calculation.
        # Put the 4 input numbers in an array,calcuate the dot product 
        # (4 input numbers in an array dot [1, 2, 3, 4]).
        # All output values are integers.
        input_file = f"{numpy_input_filename_str}.txt"
        with open(job.fn(input_file), "r") as fp:
            input_line = fp.readlines()
            split_input_line = input_line  
            for i, line in enumerate(input_line):
                split_input_line = line.split() 
                if len(split_input_line) == 4:  
                    try:
                        input_array = np.array(
                            [
                            int(split_input_line[0]), 
                            int(split_input_line[1]), 
                            int(split_input_line[2]), 
                            int(split_input_line[3])
                            ],
                            dtype=int
                        ) 
                        print(f'input_array = {input_array}')
                        multiply_array = np.array([1, 2, 3, 4])
                        print(f'multiply_array = {multiply_array}')
                        dot_product = int(np.dot(input_array, multiply_array))
                        print(f'dot_product = {dot_product}')

                    except:
                        raise ValueError("ERROR: The numpy input file is not 4 integer values.")

        # Write the output
        ouput_filename_ip = f"{numpy_output_filename_str}_in_progress.txt"
        ouput_filename = f"{numpy_output_filename_str}.txt"
        ouput_file = open(job.fn(f"{numpy_output_filename_str}_in_progress.txt"), "w")
        ouput_file.write('{: <20}\n'.format(dot_product))
        ouput_file.write('{: <20} {: <20} {: <20}'.format("Numpy", "Calculations", "Completed"))
        ouput_file.close()

        # Check if the numpy calcs completed properly and rename the final file.
        if job.isfile(ouput_filename_ip):
            with open(job.fn(ouput_filename_ip), "r") as fp:
                output_line = fp.readlines()
                for i, line in enumerate(output_line):
                    split_move_line = line.split()
                    if "Numpy" in line and len(split_move_line) == 3:
                        if (
                            split_move_line[0] == "Numpy"
                            and split_move_line[1] == "Calculations"
                            and split_move_line[2] == "Completed"
                        ):
                            os.rename(
                                job.fn(f"{ouput_filename_ip}"),
                                job.fn(f"{ouput_filename}")
                            )

        # example of running a bash command
        print(f"Running job id {job}")
        run_command = "echo {}".format(
            'Running the echo command or any other bash command here',
        )

        print(f'example bash run command = {run_command}')

        os.system(run_command)

# ******************************************************
# PERFORM THE NUMPY CALCULATIONS (END)
# ******************************************************

# ******************************************************
# DATA ANALSYIS: GET THE REPLICATE DATA AVG AND STD. DEV (START)
# ******************************************************

def part_4_analysis_replicate_averages_command(*jobs):
    # Get the individial averages of the values from each state point,
    # and print the values in each separate folder.    
    # The 'avg_std_dev_calculated.txt' file needs to be the 'product'
    # for the workflow.toml file.

    # List the output column headers
    output_column_value_0_int_input_title = 'value_0_int' 
    output_column_numpy_avg_title = 'numpy_avg'
    output_column_numpy_std_dev_title = 'numpy_std_dev'  

    # create the lists for avg and std dev calcs
    value_0_int_repilcate_list = []
    numpy_replicate_list = []
    
    # write the output file before the for loop, so it gets all the 
    # values in the loops
    output_txt_file_header = \
        f"{output_column_value_0_int_input_title: <20} " \
        f"{output_column_numpy_avg_title: <20} " \
        f"{output_column_numpy_std_dev_title: <20} " \
        f" \n"

    if not os.path.isdir(f'analysis'):
        os.mkdir(f'analysis')
    write_file_name_and_path = f'analysis/{output_avg_std_of_replicates_txt_filename}.txt' 
    if os.path.isfile(write_file_name_and_path):
        replicate_calc_txt_file = open(write_file_name_and_path, "a")
    else:
        replicate_calc_txt_file = open(write_file_name_and_path, "w")
        replicate_calc_txt_file.write(output_txt_file_header)

    # Loop over all the jobs that have the same "value_0_int" (in sort_by="value_0_int"). 
    for job in jobs:
        # get the individual values
        output_file = f"{numpy_output_filename_str}.txt"
        with open(job.fn(output_file), "r") as fp:
            output_line = fp.readlines()
            split_output_line = output_line  
            for i, line in enumerate(output_line):
                split_line = line.split() 
                if len(split_line) == 1:
                   value_0_int_repilcate_list.append(int(job.doc.value_0_int)) 
                   numpy_replicate_list.append(int(split_line[0]))    

                elif not (
                    len(split_line) == 3 
                      and split_line[0] == 'Numpy' 
                      and split_line[1] == 'Calculations'
                      and split_line[2] == 'Completed'
                    ):
                    raise ValueError("ERROR: The format of the numpy output files are wrong.")

    # Check that the value_0_int are all the same and the aggregate function worked, 
    # grouping all the replicates of value_0_int
    print(value_0_int_repilcate_list)
    for j in range(0, len(value_0_int_repilcate_list)):
        if value_0_int_repilcate_list[0] != value_0_int_repilcate_list[j]:
            raise ValueError(
                "ERROR: The value_0_int values are not grouping properly in the aggregate function."
                )
        value_0_int_aggregate = value_0_int_repilcate_list[0] 

    # Calculate the means and standard devs
    print(f'********************')
    print(f'value_0_int_aggregate = {value_0_int_aggregate}')
    print(f'numpy_replicate_list = {numpy_replicate_list}')
    print(f'********************')

    numpy_avg = np.mean(numpy_replicate_list)
    numpy_avg_std = np.std(numpy_replicate_list, ddof=1)

    replicate_calc_txt_file.write(
        f"{value_0_int_aggregate: <20} "
        f"{numpy_avg: <20} "
        f"{numpy_avg_std: <20} "
        f" \n"
    )

    replicate_calc_txt_file.close()

    # Write the completion files for all the individual state spaces
    # where the averaging and standard deviations were calculated
    # The 'avg_std_dev_calculated.txt' file are auto-deleted when 
    # the 'init.py' file is run.  So if there are errors with this, 
    # you can run 'python init.py' and it will reset it, so you can 
    # rerun it. 
    # The 'avg_std_dev_calculated.txt' file needs to be the 'product'
    # for the workflow.toml file.
    for job in jobs:
        # Write the output
        ouput_filename = f"{'avg_std_dev_calculated'}.txt"
        ouput_file = open(job.fn(ouput_filename), "w")
        ouput_file.close()

# ******************************************************
# # DATA ANALSYIS: GET THE REPLICATE DATA AVG AND STD. DEV (END)
# ******************************************************

# ******************************************************
# ROW'S ENDING CODE SECTION (START)
# ******************************************************
if __name__ == '__main__':
    # Parse the command line arguments: python action.py --action <ACTION> [DIRECTORIES]
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', required=True)
    parser.add_argument('directories', nargs='+')
    args = parser.parse_args()

    # Open the signac jobs
    project = signac.get_project()
    jobs = [project.open_job(id=directory) for directory in args.directories]

    # Call the action
    globals()[args.action](*jobs)
    #globals()[args.action]()
# ******************************************************
# ROW'S ENDING CODE SECTION (END)
# ******************************************************

