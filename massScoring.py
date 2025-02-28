from os import listdir

jobNames = []
for file in listdir("./AF2_out/"):
    jobNames.append(file)
print(jobNames)

for job in jobNames:
    exec(
        "sbatch -J "
        + job.split(".")[0]
        + " ./score.batch"
        + " ./AF2_out/"
        + job
        + " "
        + job
    )
