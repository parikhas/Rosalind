from Bio import SeqIO
from Bio.Seq import Seq

def check_rvco(fasta):
    count = 0
    for record in SeqIO.parse(fasta, "fasta"):
        if record.seq == record.seq.reverse_complement():
            count += 1
    return count

if __name__ == "__main__":
    matches = check_rvco("data/rosalind_rvco.txt")
    print(matches)