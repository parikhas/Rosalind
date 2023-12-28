from Bio.Seq import Seq

def base_count(seq):
    seq = Seq(seq)
    print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))

# if __name__ == "__main__":
#     f1 = open("data/rosalind_dna.txt", "r") 
#     sequence = f1.readline().strip()
#     base_count(sequence)


def rna_from_dna(seq):
    seq = Seq(seq)
    return seq.transcribe()

# if __name__ == "__main__":
#     print(rna_from_dna("GATGGAACTTGACTACGTAAATT"))

def revc(seq):
    
    seq = Seq(seq)
    return seq.reverse_complement()

# if __name__ == "__main__":
#     print(revc("AAAACCCGGT"))

def compare_gc(seq, highest_gc_perc, highest_gc_record, current_record):
    gc = (seq.count("G") + seq.count("C"))/len(seq)
    if gc > highest_gc_perc:
        highest_gc_perc = gc
        highest_gc_record = current_record
    return highest_gc_record, highest_gc_perc

def highest_gc(fasta):
    highest_gc_record = ""
    highest_gc_perc = 0
    seq = ""

    with open (fasta, "r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">") and seq != "":
                h,c = compare_gc(seq, highest_gc_perc, highest_gc_record, current_record)
                current_record = line[1:]
                seq = ""
            elif line.startswith(">") and seq == "":
                current_record = line[1:]
            else:
                seq += line
    h, c = compare_gc(seq, highest_gc_perc, highest_gc_record, current_record)
    return h,c

if __name__ == "__main__":
    print(highest_gc("data/gc.fasta"))

def prot_from_rna(file):
    f1 = open(file, "r")
    rna = Seq(f1.readline().strip())
    f1.close()
    return rna.translate(table=1)

# if __name__ == "__main__":
#     print(prot_from_rna("data/rosalind_prot.txt"))

def motif(s, t):
    matches = []
    l = len(t)
    for i in range(len(s)-(l+1)):
        if s[i:i+l] == t:
            matches.append(i+1)
    return matches

# if __name__ == "__main__":
#     print(motif("GATATATGCATATACTT", "ATAT"))

def point_mutations(s1, s2):
    count = 0
    for i,j in zip(s1,s2):
        if i != j:
            count += 1
    return count

# if __name__ == "__main__":
#     print(point_mutations("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))

def splc(fasta):
    dna = ""
    seq = ""
    with open(fasta, "r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">") and seq != "":
                if dna == "":
                    dna += seq
                else: 
                    dna = dna.replace(seq, "")
                seq = ""
            elif line.startswith(">") and seq == "":
                continue
            else:
                seq += line
    exon = dna.replace(seq, "")
    exon = Seq(exon)
    return exon.translate(table=1)

# if __name__ == "__main__":
#     print(splc("data/rosalind_splc.txt"))



def sseq(s,t):
    substring_ind = []
    substring_l = [i for i in t]
    for i in range(len(s)):
        if len(substring_l) > 0:
            if s[i] == substring_l[0]:
                substring_ind.append(i+1)
                del substring_l[0]
        else:
            break
    return substring_ind

def get_strings(fasta):
    s1 = ""
    s2 = ""
    l = 0
    with open(fasta, "r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">"):
                l += 1
            else:
                if l == 1:
                    s1 += line
                else:
                    s2 += line
    return s1, s2

# if __name__ == "__main__":
#     s,t = get_strings("data/rosalind_sseq.txt")
#     print(*sseq(s, t))
