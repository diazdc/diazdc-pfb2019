class DNARecord(object):
  # define class attributes
  sequence = 'ACGTAGCTGACGATC' 
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster'
  
  # define methods
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

dir(DNARecord)

## create a new DNARecord Object
dna_rec_obj = DNARecord() 

## Use New DNARecord object
print('Created a record for ' + dna_rec_obj.gene_name + ' from ' + dna_rec_obj.species_name) 
print('AT is ' + str(dna_rec_obj.get_AT()))
print('complement is ' + dna_rec_obj.reverse_complement())

dir(DNARecord)


dna_rec_obj.sequence
dna_rec_obj.get_AT()
dna_rec_obj.sequence
dna_rec_obj.reverse_complement()




"""
Using __init__
"""
# test
# works
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





"""
Problem Sets
"""




"""
1.
"""
class DNA_org(object):
    def __init__(self, seq, gene_name, species_name):
        self.seq = seq
        self.gene_name = gene_name
        self.species_name = species_name


"""
2.
"""
banana_seq = DNA_org('ACTGATCGTTACGTACGAGT', 'banana_gene1', 'Banana')


"""
3.
"""
banana_seq.seq
banana_seq.gene_name
banana_seq.species_name


"""
4.
"""
class DNA_org(object):
    def __init__(self, seq, gene_name, species_name):
        self.seq = seq
        self.gene_name = gene_name
        self.species_name = species_name
    
    def get_len(self): 
        length = len(self.seq)
        return length

banana_seq = DNA_org('ACTGATCGTTACGTACGAGT', 'banana_gene1', 'Banana')
banana_seq.get_len()


"""
5.
"""
class DNA_org(object):
    def __init__(self, seq, gene_name, species_name):
        self.seq = seq
        self.gene_name = gene_name
        self.species_name = species_name
    
    def get_len(self): 
        length = len(self.seq)
        return length
    
    def get_comp(self):
        a_count = self.seq.count('A')
        t_count = self.seq.count('T')
        g_count = self.seq.count('G')
        c_count = self.seq.count('C')
        return(a_count, t_count, g_count, c_count)

banana_seq = DNA_org('ACTGATCGTTACGTACGAGT', 'banana_gene1', 'Banana')
banana_seq.get_comp()


"""
6.
"""
class DNA_org(object):
    def __init__(self, seq, gene_name, species_name):
        self.seq = seq
        self.gene_name = gene_name
        self.species_name = species_name
    
    def get_len(self): 
        length = len(self.seq)
        return length
    
    def get_comp(self):
        a_count = self.seq.count('A')
        t_count = self.seq.count('T')
        g_count = self.seq.count('G')
        c_count = self.seq.count('C')
        return(a_count, t_count, g_count, c_count)
    
    def get_GC(self):
        length = len(self.seq)
        g_count = self.seq.count('G') 
        c_count = self.seq.count('C') 
        gc_content = (g_count + c_count) / length
        return gc_content

banana_seq = DNA_org('ACTGATCGTTACGTACGAGT', 'banana_gene1', 'Banana')
banana_seq.get_GC()


"""
7.
"""
class DNA_org(object):
    def __init__(self, seq, gene_name, species_name):
        self.seq = seq
        self.gene_name = gene_name
        self.species_name = species_name
    
    def get_len(self): 
        length = len(self.seq)
        return length
    
    def get_comp(self):
        a_count = self.seq.count('A')
        t_count = self.seq.count('T')
        g_count = self.seq.count('G')
        c_count = self.seq.count('C')
        return(a_count, t_count, g_count, c_count)
    
    def get_GC(self):
        length = len(self.seq)
        g_count = self.seq.count('G') 
        c_count = self.seq.count('C') 
        gc_content = (g_count + c_count) / length
        return gc_content
    
    def print_fasta(self):
        fasta_header = '>' + self.gene_name + '\n'
        return print(fasta_header + self.seq)

banana_seq = DNA_org('ACTGATCGTTACGTACGAGT', 'banana_gene1', 'Banana')
banana_seq.print_fasta()