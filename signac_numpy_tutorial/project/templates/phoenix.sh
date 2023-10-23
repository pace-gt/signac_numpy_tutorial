{% extends "slurm.sh" %}

{% block header %}
{% set gpus = operations|map(attribute='directives.ngpu')|sum %}
    {{- super () -}}

{% if gpus %}
#SBATCH -q gpu
#SBATCH --gres gpu:{{ gpus }}
#SBATCH --constraint=v100
{%- else %}
#SBATCH -q primary
#SBATCH --constraint=intel
{%- endif %}

#SBATCH -N 1
#SBATCH --mail-type=ALL

echo  "Running on host" hostname
echo  "Time is" date

# load any modules here needed for both CPU and GPU versions
module load python/3.10

# Add any modules here needed only for the GPU versions
{% if gpus %}
module load cuda/11.0
{%- endif %}

# activate the required conda environment
conda activate signac_numpy_example

{% endblock header %}

{% block body %}
    {{- super () -}}


{% endblock body %}
