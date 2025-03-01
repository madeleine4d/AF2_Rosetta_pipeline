from os import listdir, system


def SubmitJob(jobName: str, pathToBatch: str, pathToPDB: str):
    system("sbatch -J " + jobName + " " + pathToBatch + " " + pathToPDB + " " + jobName)


def JobsFromDir(pathToBatch: str, pathToDir: str):
    jobNames = []
    for file in listdir(pathToDir):
        jobNames.append(file)
    print(jobNames)

    for job in jobNames:
        SubmitJob(job.split(".")[0], pathToBatch, pathToDir + "/" + job)
