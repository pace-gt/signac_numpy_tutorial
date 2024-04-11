{% extends "slurm.sh" %}

{% block header %}
{% set np_max = operations|map(attribute='directives.np')|max %}
{% set mem_per_cpu = operations|map(attribute='directives.mem-per-cpu')|max %}
{% set cpus_per_part = operations|map(attribute='directives.cpus-per-part')|max  %}
{% set gpus_per_part = operations|map(attribute='directives.gpus-per-part')|max  %}

    {{- super () -}}

#SBATCH -A phx-pace-staff
#SBATCH -q inferno
#SBATCH --output=/dev/null
#SBATCH --error=/dev/null
#SBATCH -N 1
#SBATCH --ntasks-per-node={{ np_global }}
#SBATCH --mem-per-cpu={{ mem_per_cpu }}G

{% if gpus_per_part > 0 %}
#SBATCH -p gpu-a100
{%- endif %}

{% if ( gpus_per_part > 0 and np_max > 1 ) %}
#SBATCH --gres gpu:{{ ( np_global / np_max * gpus_per_part ) | int }}
#SBATCH --gpus-per-task={{ gpus_per_part }}
{% elif ( gpus_per_part > 0 and np_max == 1 ) %}
#SBATCH --gres gpu:{{ np_global * gpus_per_part }}
#SBATCH --gpus-per-task={{ gpus_per_part }}
{%- endif %}

{% if gpus_per_part == 0 %}
#SBATCH -p cpu-small
{%- endif %}
{% if np_max > 1 %}
#SBATCH --cpus-per-task={{ 1 }}
{% elif np_max == 1 %}
#SBATCH --cpus-per-task={{ cpus_per_part }}
{%- endif %}


echo  "Running on host" hostname
echo  "Time is" date

# load any modules here needed for both CPU and GPU versions
module load anaconda3

# Add any modules here needed only for the GPU versions
{% if gpus_per_part %}
module load cuda/12.1.1-6oacj6
{%- endif %}

# activate the required conda environment
conda activate signac_numpy_tutorial

{% endblock header %}

{% block body %}
    {{- super () -}}


{% endblock body %}