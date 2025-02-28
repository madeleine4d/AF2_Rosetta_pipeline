import os
import glob
import pymol2

dirs = os.listdir()

for dir in dirs:
    print (dir)
    print (glob.glob(dir + '\\*.cif'))
    for file in glob.glob( dir + "\\*.cif"):
        print(' ' + file)
        with pymol2.PyMOL() as pymol:
            print(file)
            pymol.cmd.load(file,'myprotein')
            pymol.cmd.save(os.path.dirname((os.path.abspath(__file__)))+'\\' + file.split('\\')[-1].replace('.cif', '.pdb'), selection='myprotein')
