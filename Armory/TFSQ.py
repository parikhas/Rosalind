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


# from Bio import SeqIO

# def convert_fasta_to_fastq(fasta, fastq):
#     SeqIO.convert(fasta, "fasta", fastq, "fastq")

# if __name__ == "__main__":
#     convert_fasta_to_fastq("data/rosalind_tfsq.fasta","data/rosalind_tfsq1.fastq")

with open("data/rosalind_tfsq.fasta", "r") as fasta, open("data/rosalind_tfsq1.fastq", "w") as fastq:
    for record in SeqIO.parse(fasta, "fasta"):
        print(len(record))
        record.letter_annotations["phred_quality"] = [40] * len(record) 
        read_quality = record.letter_annotations["phred_quality"]
        print(read_quality)
        SeqIO.write(record, fastq, "fastq")