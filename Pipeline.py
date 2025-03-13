import RosettaLink as RL
import traceback
import AF3link as AF


def commandHelp():
    print(
        """
Commands:

score_all_in_dir
    submits every pdb in a directory to Rosetta scoring.

make_AF3_jobs
    takes a csv with 3 columns (name, aff, and gf), where name is the name of the comparison being made, aff is the sequence for an affibody, and gf is the sequence for a growth factor. Creates a .JSON file with the required structure to be submited to Alpah Fold 3.

help
    print this list of commands.

quit
    close this program.

    """
    )


commandHelp()
loop = True
while loop:
    try:
        currentCommand = input("PL> ")

        mainCommand = currentCommand.split(" ")[0]

        match mainCommand:
            case "score_all_in_dir":
                pathToDir = input("Dir to run: ")
                pathToBatch = input("Batch to use: ")
                RL.JobsFromDir(pathToBatch, pathToDir)
            case "make_AF3_jobs":
                pathToSeqs = input("Seqs to turn into jobs.JSON: ")
                pathToSave = input("Name and path of new .JSON file: ")
                AF.SeqsToJason(pathToSeqs, pathToSave)
            case "quit":
                loop = False
            case "help":
                commandHelp()
            case _:
                print("command not recognized")

    except Exception:
        print(traceback.format_exc())
