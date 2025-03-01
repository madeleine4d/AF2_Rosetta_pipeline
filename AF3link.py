import pandas as pd
import json

defaultTemplate = """
job={
    "name": seqs.at[i, "name"],
    "modelSeeds": seed,
    "sequences": [
        {"proteinChain": {"sequence": seqs.at[i, "gf"], "count": 2}},
        {"proteinChain": {"sequence": seqs.at[i, "aff"], "count": 1}},
    ],
}
jobs.append(job)
"""


def LoadSeqs(path: str):
    match path.split(".")[-1]:
        case "csv":
            seqs = pd.read_csv(path)
            print("File imported:\n")
            print(seqs)
        case "xlsx":
            seqs = pd.read_excel(path)
            print("File imported:\n")
            print(seqs)
        case _:
            seqs = pd.DataFrame()
            print("File type is not supported")
    return seqs


def MakeStruct(seqs: pd.DataFrame, seed=[], template=defaultTemplate):
    jobs = []
    job = {}
    for i in list(seqs.index.values):
        exec(template, dict(i=i, seed=seed, seqs=seqs, job=job, jobs=jobs))
    return jobs


def SaveJson(struct: list, path: str):
    with open(path, "w") as outfile:
        json.dump(struct, outfile)


def SeqsToStruct(pathToSeqs: str):
    seqs = LoadSeqs(pathToSeqs)
    struct = MakeStruct(seqs)
    return struct


def SeqsToJason(pathToSeqs: str, pathToSave: str):
    struct = SeqsToStruct(pathToSeqs)
    SaveJson(struct, pathToSave)


SeqsToJason("./Seqs.csv", "./jobs2.json")
