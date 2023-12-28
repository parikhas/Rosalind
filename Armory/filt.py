from Bio import SeqIO

def filt_reads(quality, percent, fastq):
    reads_passed = 0
    for record in SeqIO.parse(fastq, "fastq"):
        read_qual = record.letter_annotations["phred_quality"]
        qual_passed = 0
        for each_score in read_qual:
            if each_score >= quality:
                qual_passed += 1
        if (qual_passed/len(record)*100) >= percent:
            reads_passed += 1
    return reads_passed

if __name__ == "__main__":
    f1 = open("data/rosalind_filt.txt", "r")
    threshold, percentage = map(int, (f1.readline().strip().split(" ")))
    num_passed = filt_reads(threshold, percentage, f1)
    print(num_passed)
    f1.close()
        