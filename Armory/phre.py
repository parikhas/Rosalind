from Bio import SeqIO

def reads_failing_threshold(fastq, threshold):
    failed_counts = 0
    for record in SeqIO.parse(fastq, "fastq"):
        read_quality = record.letter_annotations["phred_quality"]
        if sum(read_quality)/len(record) < float(threshold):
            failed_counts += 1
    return failed_counts

if __name__ == "__main__":
    f1 = open("data/rosalind_phre.txt", "r")
    read_threshold = f1.readline().strip()
    reads_below_threshold = reads_failing_threshold(f1, read_threshold)
    print(reads_below_threshold)
