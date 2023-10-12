"""
Read Filtration by Quality

URL: http://rosalind.info/problems/filt/

Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.

Return: Number of reads in filtered FASTQ entries
"""

from Bio import SeqIO

def read_quality_filtration(fastq):
    count = 0
    with open(fastq, "r") as f1:
        threshold,percent = map(int, (f1.readline().strip().split()))
        print(threshold, percent)
        for record in SeqIO.parse(f1, "fastq"):
            read_quality = record.letter_annotations["phred_quality"]
            quality_passed = 0
            for phred_score in read_quality:
                if phred_score >= threshold:
                    quality_passed += 1
            if (quality_passed/len(read_quality)*100) >= percent:
                count += 1
    print(count)

if __name__ == "__main__":
    fastq = "data/rosalind_filt.txt"
    read_quality_filtration(fastq)
