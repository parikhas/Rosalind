"""
Protein Translation

https://rosalind.info/problems/ptra/

Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.

Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)
"""
from Bio.Seq import Seq

def get_genetic_code_used(dna_seq, prot_seq):
    dna_seq, prot_seq = Seq(dna_seq), Seq(prot_seq)
    codon_tables = [1,2,3,4,5,6,9,10,11,12,13,14,15]
    for i in codon_tables:
        if dna_seq.translate(table=i,to_stop=True) == prot_seq:
            return i
        
if __name__ == "__main__":
    with open("data/rosalind_ptra.txt", "r") as f1:
        dna = f1.readline().strip()
        prot = f1.readline().strip()
    print(get_genetic_code_used(dna, prot))
