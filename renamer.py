import glob
from Bio.PDB import PDBList, PDBIO, PDBParser

pdbl = PDBList()

io = PDBIO()
parser = PDBParser()

pdbs = []
for i in glob.glob("*.pdb"):
    pdbs.append(i.split(".")[0])

for pdbName in pdbs:
    pdbl.retrieve_pdb_file(pdbName, pdir=".", file_format="pdb")

    # pdb6gch.ent is the filename when retrieved by PDBList
    structure = parser.get_structure(pdbName, f"{pdbName}.pdb")

    renames = {"B": "A", "C": "B"}

    for model in structure:
        for chain in model:
            old_name = chain.get_id()
            new_name = renames.get(old_name)
            if new_name:
                print(f"renaming chain {old_name} to {new_name}")
                chain.id = new_name
            else:
                print(f"keeping chain name {old_name}")

    io.set_structure(structure)
    io.save(f"{pdbName}_renamed.pdb")
