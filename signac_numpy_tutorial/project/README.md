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