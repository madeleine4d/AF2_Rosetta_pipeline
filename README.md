# read me
This is a small terminal app that helps connect Alpha Fold 3 and Rosetta. To use just run Pipeline.py with an up to date version of python. It is best to do this inside of the computer you are using to run SLURM.

## commands
score_all_in_dir

This command will ask you for a path to a dir containing at least 1 .pdb file and the path to a batch file you want to use. It will use "sbatch" on every .pdb file found in the directory specified using the file name as the job name and the batch file. 
