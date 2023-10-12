"""
Finding Genes with ORFs

URL: https://rosalind.info/problems/orfr/

Given: A DNA string s of length at most 1 kbp.

Return: The longest protein string that can be translated from an ORF of s. If more than one protein string of maximum length exists, then you may output any solution.
"""

from Bio.Seq import Seq
from Bio.Seq import reverse_complement

def longest_protein_string(dna):
    prot = []
    dna_seq = Seq(dna)
    rc = reverse_complement(dna_seq)
    prot.append(dna_seq.translate())
    prot.append(rc.translate())
    print(prot)

if __name__ == "__main__":
    with open("data/orfr.txt", "r") as f1:
        dna = f1.readline().strip()
        longest_protein_string(dna)