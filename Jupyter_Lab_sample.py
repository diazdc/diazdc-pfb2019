import os
import re
os.getcwd()


num = 6
if num < 0:
    print('negative')
elif num == 0:
    print('equal to 0')
elif (num < 50) & (num % 2 == 0):
    print('num is positve, less than 50, and even')

line_number = 1
with open('Python/data/Python_07_nobody.txt') as nobody:
    for line_number, line in enumerate(nobody):
        for found in re.finditer(r"Nobody", line):
            print("Found match in line {} pos {}".format(
                line_number, found.start()+1))

            
class DNARecord(object):
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    def reverse_complement(self): 
        replacement1 = self.sequence.replace('A', 't') 
        replacement2 = replacement1.replace('T', 'a')
        replacement3 = replacement2.replace('C', 'g')
        replacement4 = replacement3.replace('G', 'c') 
        reverse_comp = replacement4[::-1]
        return reverse_comp.upper()
    
    def get_AT(self): 
        length = len(self.sequence)
        a_count = self.sequence.count('A') 
        t_count = self.sequence.count('T') 
        at_content = (a_count + t_count) / length 
        return at_content

## Create new DNARecord Objects with user defined data
dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
dna_rec_obj_2 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')

for d in [ dna_rec_obj_1, dna_rec_obj_2 ]:
  print('name:' , d.gene_name , ' ' , 'seq:' , d.sequence)


# Show console figures
import os
import pandas as pd
from matplotlib import pyplot as plt

os.chdir('/Users/ddiaz/Documents/diazdc-pfb2019/')
cell_attributes = pd.read_csv("./meta_data.csv", index_col=0)
cell_df_sub = cell_attributes.iloc[:10,[0,1,3,5]]

%matplotlib inline
cell_df_sub.loc[:,'n_counts'].plot.kde()
cell_df_sub.loc[:,'n_genes'].plot.kde()
