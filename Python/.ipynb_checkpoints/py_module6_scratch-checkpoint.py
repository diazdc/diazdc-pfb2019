import os
os.getcwd()
os.chdir('/Users/ddiaz/Documents/diazdc-pfb2019/Python')


# 1
"""
Write a script to do the following to Python_06.txt
    Open and read the contents.
    Uppercase each line
    Print each line to the STDOUT
"""
with open('./data/Python_06.txt', 'r') as song:
  for line in song:
    print(line.upper(), end='')


# 2
"""
Modifiy the script in the previous problem to write the contents to a
new file called "Python_06_uc.txt"
"""
song_uppercase = open('./data/Python_06_uc.txt', 'w')
with open('./data/Python_06.txt', 'r') as song:
    for line in song:
        print(line.upper(), end = '', file = song_uppercase)
song_uppercase.close()


# 3
"""
Open and print the reverse complement of each sequence in Python_06.seq.txt.

Each line is the following format: seqName\tsequence\n. Make sure to print
the output in fasta format including the sequence name and a note in the
description that this is the reverse complement. Print to STDOUT and capture
the output into a file with a command line redirect '>'.

Remember is is always a good idea to start with a test set for which you know
the correct output.
"""

with open('./data/Python_06.seq.txt', 'r') as sf:
  for line in sf:
    identifier, sequence = line.rstrip().split("\t")
    sequence_RC = sequence.replace('A', 't')
    sequence_RC = sequence.replace('T', 'a')
    sequence_RC = sequence.replace('C', 'g')
    sequence_RC = sequence.replace('G', 'c')
    sequence_RC=sequence_RC.upper()[:: - 1]
    print(">{}_reverse_complement\n{}".format(identifier,sequence))


# 4
"""
Open the FASTQ file Python_06.fastq and go through each line of the file.
Count the number of lines and the number of characters per line.
Have your program report the:
    total number of lines
    total number of characters
    average line length
"""

n_lines = 0
n_chars = 0

with open('Python_06.fastq', 'r') as fq:
  for line in fq:
    line = line.rstrip()
    n_lines += 1
    n_chars += len(line)
print("""There are {} lines and {} characters in the file.\nThe average line
    length is {}""".format(n_lines, n_chars, n_chars/n_lines))

# 5
"""
Generate Gene Lists:

Get all genes:

Go to Ensembl Biomart.

    In dropdown box, select "Ensembl Genes 94"
    In dropdown box, select "Alpaca Genes"
    On the left, click Attributes
    Expand GENE:
    Deselect "transcript stable ID".
    Click Results (top left)
    Export all results to "File" "TSV" --> GO
    Rename the file to "alpaca_all_genes.tsv"

Get genes that have been labeled with Gene Ontology term stem cell proliferation

    Click "Filters"
    Under "Gene Ontology", check "Go term name" and enter "stem cell proliferation"
    Click Results (top left)
    Export all results to "File" "TSV" --> GO
    Rename the file to "alpaca_stemcellproliferation_genes.tsv"

Get genes that have been labeled with Gene Ontology term pigmentation

    Click "Filters"
    Under "Gene Ontology", check "Go term name" and enter "pigmentation"
    Click Results (top left)
    Export all results to "File" "TSV" --> GO
    Rename the file to "alpaca_pigmentation_genes.tsv"

Open each of the three files and add the geneIDs to a Set. One Set per file.

    A. Find all the genes that are not cell proliferation genes.
    B. Find all genes that are both stem cell proliferation genes and pigment genes.

Note Make sure to NOT add the header to your set.

"""

all_genes=set()
pigmentation_genes=set()
stemcell_proliferation=set()

#read in all genes
with open("alpaca_all_genes.tsv") as ag:
  firstline=True
  for line in ag:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    all_genes.add(line)

#read in pigmentation genes
with open("alpaca_pigmentation_genes.tsv") as pg:
  firstline=True
  for line in pg:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    pigmentation_genes.add(line)

#read in sc proliferation genes
with open("alpaca_stemcellproliferation_genes.tsv") as sg:
  firstline=True
  for line in sg:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    stemcell_proliferation.add(line)

genes_not_cell_pro = all_genes-stemcell_proliferation
print("Non Stem-Cell Proliferation Genes:\n{}".format(genes_not_cell_pro))
scell_pigment=stemcell_proliferation & pigmentation_genes
print("Stemcell Proliferation & Pigmentation:\n{}".format(scell_pigment))


"""
Now, let do it again with transciption factors.

    Go back to your Ensembl Biomart window
    Deselect the "GO Term Name"
    Select "GO Term Accession"
    Enter these two accessions IDs which in most organisms will be all the
    transcription factors
    GO:0006355 is "regulation of transcription, DNA-dependent”.
    GO:0003677 is "DNA binding"
    Click Results (top left)
    Export all results to "File" "TSV" --> GO
    Rename the file to "alpaca_transcriptionFactors.tsv"

Open these two files: 1) the transcription factor gene list file and 2) the
cell proliferation gene list file. Add each to a Set, One Set per file

A. Find all the genes that are transcription factors for cell proliferation
"""

all_genes=set()
pigmentation_genes=set()
stemcell_proliferation=set()
transcription_factors=set()

with open("alpaca_stemcellproliferation_genes.tsv") as sg:
  firstline=True
  for line in sg:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    stemcell_proliferation.add(line)

with open("alpaca_transcriptionFactors_genes.tsv") as tf:
  firstline=True
  for line in tf:
    if firstline:
      firstline=False
      continue
    line=line.rstrip()
    transcription_factors.add(line)

tf_for_cp=stemcell_proliferation & transcription_factors

print('Transcription Factors for Stemcell Proliferation:\n{}'.format(tf_for_cp))
