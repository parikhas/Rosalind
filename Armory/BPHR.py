"""
Base Quality Distribution

URL: https://rosalind.info/problems/bphr/

Given: FASTQ file, quality threshold q

Return: Number of positions where mean base quality falls below given threshold
"""

from Bio import SeqIO

def mean_base_qual_fail(threshold, fastq):
    qual = []
    for record in SeqIO.parse(fastq, "fastq"):
        read_quality = record.letter_annotations["phred_quality"]
        qual.append(read_quality)

    n = len(qual[0])
    failed = 0
    for i in range(n):
        sum_base_qual = 0
        for j in range(len(qual)):
            sum_base_qual += qual[j][i]
        if sum_base_qual/len(qual) < threshold:
            failed += 1

    return failed

if __name__ == "__main__":
    f1 = open("data/rosalind_bphr.txt", "r")
    thresh = float(f1.readline().strip())
    print(mean_base_qual_fail(thresh, f1))


