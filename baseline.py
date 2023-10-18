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
for x in p.reactions: #Walk the reactions. From here you can also extract the ID for all the metabolites
    print(x)
