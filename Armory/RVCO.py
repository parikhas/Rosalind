"""
Complementing a Strand of DNA

URL: https://rosalind.info/problems/rvco/

Given: A collection of n (n≤10) DNA strings.

Return: The number of given strings that match their reverse complements.
"""

from Bio import SeqIO
from Bio.Seq import reverse_complement

def reverse_complement_count(fasta):
    count = 0
    with open(fasta, "r") as f1:
        for record in SeqIO.parse(f1, "fasta"):
            rc = reverse_complement(record.seq)
            if record.seq == rc:
                count += 1
    print(count)

if __name__ == "__main__":
    reverse_complement_count("data/rosalind_rvco.txt")