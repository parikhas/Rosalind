"""
Pairwise Global Alignment

URL: http://rosalind.info/problems/need/

Given: Two GenBank IDs.

Return: The maximum global alignment score between the DNA strings associated with these IDs.
"""

from Bio import Entrez, SeqIO, pairwise2

def max_global_alignment_score(genbank_ids):
    Entrez.email = "**@******"
    handle = Entrez.efetch(db="nucleotide", id=[genbank_ids], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])

if __name__ == "__main__":
    with open("data/rosalind_need.txt", "r") as f:
        genbank_ids = ", ".join(f.readline().strip().split())
        max_global_alignment_score(genbank_ids)
