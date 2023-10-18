from Bio.KEGG import REST

def get_metabolites(ppu):
    metabolites = set()
    pathways = REST.kegg_list(f'{ppu}/pathway').read().split('\n')
    for pathway in pathways:
        pathway_id = pathway.split('\t')[0]
        compounds = REST.kegg_get(f'{ppu}:{pathway_id}/compound').read()
        for line in compounds.split('\n'):
            if line.startswith('COMPOUND'):
                metabolites.add(line.split()[1])
    return metabolites

def download_mol_files(metabolites):
    for metabolite_id in metabolites:
        mol_data = REST.kegg_get(f'{metabolite_id}/mol').read()
        with open(f'{metabolite_id}.mol', 'wb') as file:
            file.write(mol_data)

# Usage example
organism_id = 'eco'  # Example: E. coli's KEGG organism ID
metabolites = get_metabolites(organism_id)
download_mol_files(metabolites)
