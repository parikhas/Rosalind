def base_count(string):
    # return string.count("A"), string.count("C"), string.count("G"), string.count("T")
    for base in string:
        if base not in "ATGC":
            raise ValueError("Base has to be A, T, G or C")
        else:
            return string.count("A"), string.count("C"), string.count("G"), string.count("T")

def dna_to_rna(string):
    return string.replace("T", "U")

def revc(string):
    keys_map = {"A":"T","G":"C","T":"A","C":"G"}
    new_string = ""
    for i in string:
        new_string += keys_map[i]
    return new_string[::-1]

# if __name__ == "__main__":
#     print(revc("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

def max_gc_content(fasta):
    seq_gc = {}
    seq = ""
    with open(fasta, "r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">"):
                if seq != "":
                    seq_gc[string_id] = seq
                string_id = line[1:]
                seq = ""
            else:
                seq += line
    seq_gc[string_id] = seq

    max_id = ""
    max_gc = -float("inf")
    for id, seq in seq_gc.items():
        gc = (seq.count("G")+seq.count("C"))/len(seq)
        if gc > max_gc:
            max_id = id
            max_gc = gc
    return max_id, max_gc
                
if __name__ == "__main__":
    print(max_gc_content("data/gc.fasta"))



