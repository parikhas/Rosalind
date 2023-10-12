"""
FASTQ format introduction

URL: https://rosalind.info/problems/tfsq/

Given: FASTQ file

Return: Corresponding FASTA records
"""

from Bio import SeqIO

def convert_to_fasta(fastq_file,fasta_file):
    SeqIO.convert(fastq_file, 'fastq', fasta_file, 'fasta')

if __name__ == "__main__":
    convert_to_fasta("data/rosalind_tfsq.txt","data/rosalind_tfsq.fasta")