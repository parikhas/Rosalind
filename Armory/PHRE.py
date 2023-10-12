"""
Read Quality Distribution

URL: http://rosalind.info/problems/phre/

Given: A quality threshold, along with FASTQ entries for multiple reads.

Return: The number of reads whose average quality is below the threshold.
"""

from Bio import SeqIO

def read_quality_below_threshlod(fastq):
    count = 0
    with open(fastq, "r") as f1:
        threshold = int(f1.readline())
        for record in SeqIO.parse(f1, "fastq"):
            read_quality = record.letter_annotations["phred_quality"]
            average_quality = sum(read_quality)/len(read_quality)
            if average_quality < threshold:
                count += 1
    print(count)

if __name__ == "__main__":
    fastq = "data/rosalind_phre.txt"
    read_quality_below_threshlod(fastq)