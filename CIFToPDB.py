import os
import glob
import pymol2

# TODO: generalize this

dirs = os.listdir()


def Convert(path: str):
    with pymol2.PyMOL() as pymol:
        print(path)
        pymol.cmd.load(path, "myprotein")
        pymol.cmd.save(
            os.path.dirname((os.path.abspath(__file__)))
            + "\\"
            + file.split("\\")[-1].replace(".cif", ".pdb"),
            selection="myprotein",
        )


for dir in dirs:
    print(dir)
    print(glob.glob(dir + "\\*.cif"))
    for file in glob.glob(dir + "\\*.cif"):
        print(" " + file)
        Convert(file)
