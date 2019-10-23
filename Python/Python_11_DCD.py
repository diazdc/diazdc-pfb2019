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