import RosettaLink as RL
import AF3link as AFL
import traceback


def commandHelp():
    print(
        """
Commands:


    """
    )


loop = True
while loop:
    try:
        currentCommand = input("PL> ")

        match currentCommand.split(" ")[0]:
            case "AF3_Json":
                RL.JobsFromDir(
                    str(currentCommand.split(" ")[1]), str(currentCommand.split(" ")[2])
                )

    except Exception:
        print(traceback.format_exc())
