# run programme through command line like:
# python txtFileEncrypt.py 'your_Text_FileName.txt' 
# e.g. python txtFileEncrypt.py 'demoFile.txt' 

# Assumptions: 1) input file exists
               2) arguments through command lines are passed properly
# unit testing is not included
# code uses multiprocessing
# larger file is brokem down into smaller files of 400 lines each
# content from each of the smaller files is first encrypted and then append in output file 
# The Atbash cipher is an encryption method in which each letter of a word is replaced with its
# "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
# demoFile.txt is included for testing functionality of the application