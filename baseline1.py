import Bio.KEGG
from Bio.KEGG.REST import kegg_get
from Bio.KEGG.KGML.KGML_parser import read

org = 'T00114' #KEGG Organism ID
f = open(org + '.kgml','w') #Creates a file .kgml to save all the information retrived from KEGG
dat = kegg_get(org,'kgml') #Retrive reactions and compounds from KEGG
datr = dat.read() #Convert data into a readible format
f.write (datr) #Write and save 
f.close()
p= read(open('T00114.kgml', 'r')) #read the model
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