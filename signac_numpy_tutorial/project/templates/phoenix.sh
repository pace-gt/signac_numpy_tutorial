{% extends "slurm.sh" %}

{% block header %}
{% set np = operations|map(attribute='directives.np')|sum %}
{% set mem_per_cpu = operations|map(attribute='directives.mem-per-cpu')|max %}
{% set cpus_per_process = operations|map(attribute='directives.cpus-per-process')|max  %}
{% set gpus_per_process = operations|map(attribute='directives.gpus-per-process')|max  %}
{% set mpi_1_threaded_0 = operations|map(attribute='directives.mpi-1-threaded-0')|max  %}


    {{- super () -}}

#SBATCH -A phx-pace-staff
#SBATCH -q inferno
#SBATCH --output=/dev/null
#SBATCH --error=/dev/null
#SBATCH -N 1
#SBATCH --ntasks-per-node={{ np_global }}
#SBATCH --mem-per-cpu={{ mem_per_cpu }}G

{% if gpus_per_process > 0 %}
#SBATCH -p gpu-a100

    {% if mpi_1_threaded_0 == 1 %}
    #SBATCH --gres gpu:{{ np_global * gpus_per_process }}
    #SBATCH --gpus-per-task={{ np_global }}

    {% elif mpi_1_threaded_0 == 0 %}
    #SBATCH --gres gpu:{{ np_global * gpus_per_process }}
    #SBATCH --gpus-per-task={{ gpus_per_process }}

    {%- endif %}

{%- endif %}

{% if gpus_per_process == 0 %}
#SBATCH -p cpu-small

{%- endif %}

{% if mpi_1_threaded_0 == 1 %}
#SBATCH --cpus-per-task={{ np_global }}

{% elif mpi_1_threaded_0 == 0 %}
#SBATCH --cpus-per-task={{ cpus_per_process }}

{%- endif %}


echo  "Running on host" hostname
echo  "Time is" date

# load any modules here needed for both CPU and GPU versions
module load anaconda3

# Add any modules here needed only for the GPU versions
{% if gpus_per_task %}
module load cuda/12.1.1-6oacj6
{%- endif %}

# activate the required conda environment
conda activate signac_numpy_tutorial

{% endblock header %}

{% block body %}
    {{- super () -}}


{% endblock body %}