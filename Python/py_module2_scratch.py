#!/usr/bin/env python3
seq1 = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
'ATG' in seq1
'TTT' in seq1
0 == False
# seq1.find('TTT')

if 'ATG' in seq1:
    print('Bob')
else:
    print('Joe')


if 'ATG' in seq1:
    print('Bob')
elif 'TTT' in seq1:
    print('Mary')
else:
    print('Joe')

num = 5
if num < 0:
    print('negative')
elif num == 0:
    print('equal to 0')
else:
    print('positve')

num = 5
if num < 0:
    print('negative')
elif num == 0 :
    print('equal to 0')
elif num < 50:
    print('less than 50')

num = 6
if num < 0:
    print('negative')
elif num == 0:
    print('equal to 0')
elif (num < 50) & (num % 2 == 0):
    print('num is less than 50 and even')






