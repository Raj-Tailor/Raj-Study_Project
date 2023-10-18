from Bio import Entrez, SeqIO
Entrez.email = "rajtailor30@gmail.com"
handle = Entrez.esearch(db="pcsubstance", term="Sphingobacterium mizutaii[Organism]")
record = Entrez.read(handle)
id_list = record["IdList"]
for id in id_list:
    handle = Entrez.efetch(db="pcsubstance", id=id, rettype="mol")
    mol_file = handle.read()
    with open(f"{id}.mol", "w") as f:
        f.write(mol_file)
        