"""
Introduction to the Bioinformatics Armory

URL: https://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
"""

from Bio.Seq import Seq

def base_counts(sequence):
    """Generate and print counts of A, C, G and T in a given sequenc

    Args:
        sequence (string): DNA sequence
    """
    my_seq = Seq(sequence)
    print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))

if __name__ == "__main__":
    with open("data/rosalind_ini.txt","r") as f1:
        seq = f1.readline().strip()
        base_counts(seq)