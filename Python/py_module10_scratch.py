import os
os.getcwd()
os.chdir('/Users/ddiaz/Documents/diazdc-pfb2019/Python/data')

"""
# 1
Python 10 - Functions - Problem Set
===================

1. Create a function to format a string of DNA so that each line is no more than 60 nt long. Your function will:
    - INPUT: a string of DNA without newlines   
    - OUTPUT: a string of DNA with lines no more than 60 nucleoties long

```
INPUT:
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

OUTPUT: 
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTT
CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTT
GCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCA
GACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTC
CCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGT
GGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT
```
"""
def fold_sequence(linear_sequence):
    folded_sequence = []
    linear_sequence_length = len(linear_sequence)    
    for beg in range(0, linear_sequence_length, 60):
        end = beg + 60  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)

dna='GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

print("INPUT:")
print(dna)
print()

folded_seq = fold_sequence(dna)

print("OUTPUT:")
print(folded_seq)



"""
2. Modify your function so that it will work whether the DNA string does or does not have newlines. 

```
INPUT:
dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''


OUTPUT:
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTT
CTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTT
GCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCA
GACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTC
CCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGT
GGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT
```
"""
#!/usr/bin/env python3


def fold_sequence(linear_sequence):
    linear_sequence = linear_sequence.replace('\n', '')    

    # store sub-sequences in a temporary list:
    folded_sequence = []
    linear_sequence_length = len(linear_sequence)    
    for beg in range(0, linear_sequence_length, 60):
        end = beg + 60  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)

dna='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

print("INPUT:")
print(dna)
print()

folded_seq = fold_sequence(dna)

print("OUTPUT:")
print(folded_seq)




"""
3. Modify your function so that it takes two arguments, the DNA string and the max length of each line.

```
INPUT:
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
width = 80

OUTPUT:
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT
```
"""
def fold_sequence(linear_sequence, width=60):
    linear_sequence = linear_sequence.replace('\n', '')    

    # store sub-sequences in a temporary list:
    folded_sequence = []
    linear_sequence_length = len(linear_sequence)    
    for beg in range(0, linear_sequence_length, width):
        end = beg + width  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)

dna='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'''

print("INPUT:")
print(dna)
print()

line_width = 80
folded_seq = fold_sequence(dna, width=line_width)

print("OUTPUT: (width = {:d})".format(line_width))
print(folded_seq)



"""
4. Modify your script so that it can take two command line arguments:
     1) FASTA file name
     2) Max length of each line

The script should reformat every sequence in the file to the specified max
line length. Make sure your output is in proper FASTA format.
"""
#!/usr/bin/env python3

import sys

def fold_sequence(linear_sequence, width=60):
    linear_sequence = linear_sequence.replace('\n', '')    

    # store sub-sequences in a temporary list:
    folded_sequence = []
    linear_sequence_length = len(linear_sequence)    
    for beg in range(0, linear_sequence_length, width):
        end = beg + width  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)


try:
    fasta_filename = sys.argv[1]
    line_width = int(sys.argv[2])
except IndexError:
    sys.stderr.write("Please provide two input arguments: 1) fasta file name, 2) line width\n")
    sys.exit(1)

except ValueError:
    sys.stderr.write("Line width argument must be an unsigned integer value\n")
    sys.exit(1)

try:
    fasta_file = open(fasta_filename, 'r')
except IOError:
    sys.stderr.write("Cannot open {} for reading or it is not readable".format(fasta_filename))
    sys.exit(1)

sequence_id = None
sequence_desc = ''
sequence_string = ''
for line in fasta_file:
    if line.isspace():  # line is empty
        continue
    
    line = line.rstrip()

    if line.startswith('>'):
        if len(sequence_string) > 0:
            print(">{} {}".format(sequence_id, sequence_desc))
            print(fold_sequence(sequence_string, width=line_width))

        sequence_header = line.lstrip('>').split(maxsplit=1)
        sequence_string = ''
        sequence_id = sequence_header[0]

        if len(sequence_header) > 1: # has description
            sequence_desc = sequence_header[1]
        else:  # only an ID, no description
            sequence_desc = ''

    else:
        sequence_string += line

if len(sequence_string) > 0:
    print(">{} {}".format(sequence_id, sequence_desc))
    print(fold_sequence(sequence_string, width=line_width))



"""
5. Create a new function that calculates the GC content of a DNA sequence. 
    - it will take a DNA sequence without spaces and no header as an argument
    and return the percentage of nucleotides that are a G or C.
    - example `percentGC = gc_conent('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA')` 
    or `percentGC = gc_content(dna)`
"""
import sys


def gc_content(sequence):
    gc_count = 0

    GC = set('gcGC')
    for nt in sequence:
        if nt in GC:
            gc_count += 1

    return 100.0 * gc_count / len(sequence)


try:
    fasta_filename = sys.argv[1]
    
except IndexError:
    sys.stderr.write("Please provide one input argument: fasta file name\n")
    sys.exit(1)
    
try:
    fasta_file = open(fasta_filename, 'r')
except IOError:
    sys.stderr.write("Cannot open {} for reading or it is not readable".format(fasta_filename))
    sys.exit(1)

sequence_id = None
sequence_desc = ''
sequence_string = ''
for line in fasta_file:
    if line.isspace():  # line is empty
        continue
    
    line = line.rstrip()

    if line.startswith('>'):
        if len(sequence_string) > 0:
            percentGC = gc_content(sequence_string)
            print("{0}\t{1:.2f}".format(sequence_id, percentGC))

        sequence_header = line.lstrip('>').split(maxsplit=1)
        sequence_string = ''
        sequence_id = sequence_header[0]

        if len(sequence_header) > 1: # has description
            sequence_desc = sequence_header[1]
        else:  # only an ID, no description
            sequence_desc = ''

    else:
        sequence_string += line

if len(sequence_string) > 0:
    percentGC = gc_content(sequence_string)
    print("{0}\t{1:.2f}".format(sequence_id, percentGC))



"""
6. Create a new function that computes and returns the reverse complement of a
sequence
    - it will take a DNA sequence without spaces and no header as an argument and return the reverse complement, with no spaces and no header.
    - example `revComp_sequence = get_reverse_complement(dna)`
"""
import sys

def fold_sequence(linear_sequence, width=60):
    linear_sequence = linear_sequence.replace('\n', '')    
    folded_sequence = []
    linear_sequence_length = len(linear_sequence)    
    for beg in range(0, linear_sequence_length, width):
        end = beg + width  # end of line subsequence

        folded_sequence.append(linear_sequence[beg:end])

    return '\n'.join(folded_sequence)

def reverse_complement(sequence):
    sequence = sequence[::-1].lower()
    sequence = sequence.replace('a','T')
    sequence = sequence.replace('t','A')
    sequence = sequence.replace('g','C')
    sequence = sequence.replace('c','G')
    
    return sequence

try:
    fasta_filename = sys.argv[1]
    line_width = int(sys.argv[2])
except IndexError:
    sys.stderr.write("Please provide two input arguments: 1) fasta file name, 2) line width\n")
    sys.exit(1)

except ValueError:
    sys.stderr.write("Line width argument must be an unsigned integer value\n")
    sys.exit(1)

try:
    fasta_file = open(fasta_filename, 'r')
except IOError:
    sys.stderr.write("Cannot open {} for reading or it is not readable".format(fasta_filename))
    sys.exit(1)

sequence_id = None
sequence_desc = ''
sequence_string = ''
for line in fasta_file:
    if line.isspace():  # line is empty
        continue
    
    line = line.rstrip()

    if line.startswith('>'):
        if len(sequence_string) > 0:
            print(">{} {}".format(sequence_id, sequence_desc))
            print(fold_sequence(reverse_complement(sequence_string), width=line_width))

        sequence_header = line.lstrip('>').split(maxsplit=1)
        sequence_string = ''
        sequence_id = sequence_header[0]

        if len(sequence_header) > 1: # has description
            sequence_desc = sequence_header[1]
        else:  # only an ID, no description
            sequence_desc = ''

    else:
        sequence_string += line

if len(sequence_string) > 0:
    print(">{} {}".format(sequence_id, sequence_desc))
    print(fold_sequence(reverse_complement(sequence_string), width=line_width))


"""
7. Pipelines:  
  a. Create a script that runs a command with `subprocess.run`.    
  b. Check the exit status  
  c. If exit status is good, run a second command. 
"""