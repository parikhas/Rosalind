"""
Introduction to the Bioinformatics Armory

URL: https://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
"""

from Bio.Seq import Seq

def base_count(sequence):
    my_seq = Seq(sequence)
    print("Count of A:", my_seq.count("A"))

if __name__ == "__main__":
    f1 = open("data/rosalind_ini.txt", "r")
    seq = f1.readline().strip()
    base_count(seq)
    f1.close()