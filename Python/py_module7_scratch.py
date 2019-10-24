import os
os.getcwd()
os.chdir('/Users/ddiaz/Documents/diazdc-pfb2019/Python')

"""
1
In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print
out the position.
"""
import re

# In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print 
# out the position.

poem = open('./data/Python_07_nobody.txt', 'r')

# this is the solution if you wanted to read the entire file into a string,and
# find the position in that string of each occurrance of Nobody. You may
# instead want to know the position in each line. Refer to the other version 
# of the solutions (from a different TA) to see that solution!

poem_contents = poem.read() 

line_number = 1

for line in re.finditer(r'(Nobody)', poem_contents, re.I):
    start_position = line.start(1) + 1
    print('Start position of Nobody:', start_position)
    line_number += 1
print('Done!')


#  my solution
del(poem_contents)
line_number = 1
with open('./data/Python_07_nobody.txt', 'r') as poem_contents:
    for line in poem_contents:
        for found in re.finditer(r'(Nobody)', line, re.I):
            print(found)
            # start_position = line.start(1) + 1
            # print('Start position of Nobody:', start_position)
            # line_number += 1

# Other solution
line_number = 1
with open('./data/Python_07_nobody.txt') as nobody:
    for line_number, line in enumerate(nobody):
        for found in re.finditer(r"Nobody", line):
            print("Found match in line {} pos {}".format(
                line_number, found.start()+1))


"""
2
In the file Python_07_nobody.txt substitute every occurrence of 'Nobody'
with your favorite name and write an output file with that person's name
(ex. Michael.txt).
"""
import re

poem_fo = open('./data/Python_07_nobody.txt', 'r')
poem_output = open('Somebody.txt', 'w')

for line in poem_fo:
    line = line.rstrip()
    line = re.sub(r'Nobody', 'Somebody', line, re.I)
    poem_output.write(str(line) + '\n') 

print('Wrote to Somebody.txt')
poem_fo.close()
poem_output.close()



"""
3
Using pattern matching, find all the header lines in Python_07.fasta.
Note that the format for a header in a fasta file is a line that starts with
a greater than symbol and is followed by some text (e.g. >seqName description
where seqName is the sequence name or identifier. The identifier cannot have
spaces in it. The description that follows it can have spaces.)
"""
import re

fasta_open = open('./data/Python_07.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if line.startswith('>'): 
        header = re.findall(r'^>\S+.*', line)
        print('Fasta header is:', header)

print('Script is finished running.')

fasta_open.close()



"""
4
If a line matches the format of a FASTA header, extract the sequence name and
description using sub patterns (groups).
"""
import re

fasta_open = open('./data/Python_07.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if line.startswith('>'): 
        for (seq_id, desc) in re.findall(r'^>(\S+)\s(.*)$', line):
            print('Sequence ID is:', seq_id, 'Description:', desc)
fasta_open.close()



"""
5
Create a FASTA parser, or modify your FASTA parser from the previous problem
set, to use regular expressions. Also make sure your parser can deal with a
sequence that is split over many lines.
"""
import re

fasta_read = open('./data/Python_07.fasta', 'r')

fasta_seqs = {}
fasta_keys = None

for line in fasta_read:
    line = line.rstrip()
    if line.startswith('>'):
        for match in re.finditer(r'^>(\S+)\s(.*)$', line):   
            fasta_keys = match.group(1)
            fasta_seqs[fasta_keys] = ''
    else:
        fasta_seqs[fasta_keys] += line

#print(fasta_seqs)

for key, value in fasta_seqs.items():
    print('{} \t {}'.format(key, value))

fasta_read.close()



"""
6
The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate
nucleotideides. See the IUPAC table to identify the nucleotide possibilities
for the R and Y. Write a regular expression to find and print all occurrences
of the site in the following sequence Python_07_ApoI.fasta.

>seq1
GAATTCAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATTGTGCACACAGACGCGAC
TTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTTCATTTCTCGTTCTGTTTCTACTT
AACAATGTGGTGATAATATAAAAAATAAAGCAATTCAAAAGTGTATGACTTAATTAATGA
GCGATTTTTTTTTTGAAATCAAATTTTTGGAACATTTTTTTTAAATTCAAATTTTGGCGA
AAATTCAATATCGGTTCTACTATCCATAATATAATTCATCAGGAATACATCTTCAAAGGC
AAACGGTGACAACAAAATTCAGGCAATTCAGGCAAATACCGAATGACCAGCTTGGTTATC
AATTCTAGAATTTGTTTTTTGGTTTTTATTTATCATTGTAAATAAGACAAACATTTGTTC
CTAGTAAAGAATGTAACACCAGAAGTCACGTAAAATGGTGTCCCCATTGTTTAAACGGTT
GTTGGGACCAATGGAGTTCGTGGTAACAGTACATCTTTCCCCTTGAATTTGCCATTCAAA
ATTTGCGGTGGAATACCTAACAAATCCAGTGAATTTAAGAATTGCGATGGGTAATTGACA
TGAATTCCAAGGTCAAATGCTAAGAGATAGTTTAATTTATGTTTGAGACAATCAATTCCC
CAATTTTTCTAAGACTTCAATCAATCTCTTAGAATCCGCCTCTGGAGGTGCACTCAGCCG
CACGTCGGGCTCACCAAATATGTTGGGGTTGTCGGTGAACTCGAATAGAAATTATTGTCG
CCTCCATCTTCATGGCCGTGAAATCGGCTCGCTGACGGGCTTCTCGCGCTGGATTTTTTC
ACTATTTTTGAATACATCATTAACGCAATATATATATATATATATTTAT
"""
import re

#Y can be C or T
#R can be A or G

fasta_open = open('./data/Python_07_ApoI.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if not line.startswith('>'):
        for ApoI in re.findall(r'[A|G]AATT[C|T]', line):
            print(ApoI)

print("Script has finished.")



"""
7
Determine the site(s) of the physical cut(s) by ApoI in the above sequence.
Print out the sequence with "^" at the cut site.

Hints:

    Use sub()
    Use subpatterns (parentheses and group() ) to find the cut site within the
    pattern. Example: if the pattern is GACGT^CT the following sequence

    AAAAAAAAGACGTCTTTTTTTAAAAAAAAGACGTCTTTTTTT

we want to display the cut site like this:

    AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
"""
import re

#Y can be C or T
#R can be A or G

fasta_open = open('Python_07_ApoI.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if not line.startswith('>'):
        lineCut = re.sub(r'[A|G]AATT[C|T]', r'R^AATTY', line)
        print(lineCut)
    
print("Script has finished.")



"""
8
Now that you've done your restriction digest, determine the lengths of your
fragments and sort them by length (in the same order they would separate on an
electrophoresis gel).

Hint: Convert this string:

    AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT

Into this list:

    ["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]
"""
import re

#Y can be C or T
#R can be A or G

fasta_open = open('Python_07_ApoI.fasta', 'r')
fragments = []

for line in fasta_open:
    line = line.rstrip()
    if not line.startswith('>'):
        cutSites = re.sub(r'[A|G]AATT[C|T]', r'R^AATTY', line)
        #fragments.append(cutSites.split('^'))
        fragments += cutSites.split('^')

print(sorted(fragments, key = len))
print("Script has finished.")



"""
9
Download this file: ftp://ftp.neb.com/pub/rebase/bionet.txt of enzymes and
their cut sites to fill a dictionary of enzymes paired with their recognition
patterns. Be aware of the header lines, and be aware of how the columns are
delimited. You'll modify this script in the next question.
"""
import re

enzymeFile = open('bionet.txt', 'r')

enzymeDict = {}

for line in enzymeFile:
    match = re.search(r'^(.*?)\s{4,}(.*[A-Z^])$', line)
    if match:
        enzymes = match.group(1)
        enzymeDict[enzymes] = match.group(2)
    
for key, value in enzymeDict.items():
    print('Enzyme: {} \t Cut site {}'.format(key, value))



"""
10
Write a script which takes two command line arguments: the name of an enzyme
and a fasta file with a sequence to be cut. Load a dictionary of enzyme names
and cut sites from the code you developed in question 9. If the enzyme is
present in the dictionary, and can cut the sequence, print out:
    the sequence, annotated with cut sites
    the number of fragments
    the fragments in their natural order (unsorted)
    the fragments in sorted order (largest to smallest)
"""




