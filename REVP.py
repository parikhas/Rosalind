"""
Locating Restriction Sites

URL: https://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""

from Bio import SeqIO
# from Bio.Seq import reverse_complement

def get_palindromes(fasta):
    f1 = open(fasta, "r")
    seq = SeqIO.read(f1, format="fasta")
    for start in range(len(seq)):
        for end in range(len(seq), start, -1):
            if end - start < 4:
                break
            if str(seq.seq[start:end]) == str(seq.seq[start:end].reverse_complement()):
                if len(seq.seq[start:end]) >= 4 and len(seq.seq[start:end]) <= 12:
                    print(start+1, len(seq.seq[start:end]))

if __name__ == "__main__":
    get_palindromes("data/rosalind_revp.txt")
