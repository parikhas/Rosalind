from Bio.Seq import Seq

def get_codon_table(dna_string, protein_string):
    dna_string, protein_string = Seq(dna_string), Seq(protein_string)
    codon_tables = [i+1 for i in range(15)]
    print(codon_tables)
    for i in codon_tables:
        if dna_string.translate(table=i, to_stop=True) == protein_string:
            return i
        
if __name__ == "__main__":
    f1 = open("data/rosalind_ptra.txt", "r")
    dna = f1.readline().strip()
    prot = f1.readline().strip()
    codon_table = get_codon_table(dna, prot)
    print(codon_table)