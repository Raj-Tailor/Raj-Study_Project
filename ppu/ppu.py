import Bio.KEGG
from Bio.KEGG.REST import kegg_get
from Bio.KEGG.KGML.KGML_parser import read
import requests

org = 'ppu01100' #KEGG Organism ID
f = open(org + '.kgml','w') #Creates a file .kgml to save all the information retrived from KEGG
dat = kegg_get(org,'kgml') #Retrive reactions and compounds from KEGG
datr = dat.read() #Convert data into a readible format
f.write (datr) #Write and save
f.close()
p= read(open('ppu01100.kgml', 'r')) #read the model
Metabolites=[] #Starting a list to save all the metabolites
for reaction in p.reactions: #Walk the reactions. From here you can also extract the ID for all the metabolites
    print('\n')
    print('Reaction')
    print(reaction.name)
    print('Substrates')
    for substrate in reaction.substrates:
        SubstrateName=substrate.name
        SubstrateID=SubstrateName.replace('cpd:','')
        print(SubstrateID)
        Metabolites.append(SubstrateID)
    print('Products')
    for product in reaction.products:
        ProductName=product.name
        ProductID=ProductName.replace('cpd:','')
        print(ProductID)
        Metabolites.append(ProductID)
   # print(str(x))
UniqueMetabolites = set(Metabolites)  # Delete repetitions
url='https://www.genome.jp/entry/-f+m+'
for met in UniqueMetabolites: #This is the list of metabolites name that you can use to retrieve the mol files
    print(met)
    mapa=url+met #Write a new URL following KEGG format
    print(mapa)
    url = f'https://www.genome.jp/entry/-f+m+{met}'
    mol = requests.get(url)
    # print('t',t)
    data = mol.text
# for met in data:
    x = open(f'{met}.mol', 'w')
    x.write(data)
    print("done")

 #This library is independent from KEGG, but you can extract information from web pages, such as the simple interface where mol files are stored
#url = 'https://www.genome.jp/entry/-f+m+C00048' The URL have an useful structure
# for met in UniqueMetabolites:
#     response = requests.get(mapa)  # Send a request to the URL
#     if response.status_code == 200:  # Check if the request was successful
#         mol_data = response.text  # Get the response data (mol file)
#         with open(f'{met}.mol', 'w') as mol_file:  # Open a new file with the metabolite name
#             mol_file.write(mol_data)  # Write the mol data to the file
#         print(f'{met}.mol saved successfully')  # Print a success message
#     else:
#         print(f'Error downloading {met} mol file')  # Print an error message if the request fails
