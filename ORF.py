"""Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s
 of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s
. Strings can be returned in any order.
"""

def parse_fasta(fasta):
    dna = ""
    with open(fasta,"r") as f1:
        for line in f1:
            line = line.strip()
            if not line.startswith(">"):
                dna += line
    return dna
    
def amino_acid_from_dna(dna):
    # print(dna)
    amino_acid = ""
    translated_protein = []
    dna_codon = {
        'TCA' : 'S',    # Serine
        'TCC' : 'S',    # Serine
        'TCG' : 'S',    # Serine
        'TCT' : 'S',    # Serine
        'TTC' : 'F',    # Phenylalanine
        'TTT' : 'F',    # Phenylalanine
        'TTA' : 'L',    # Leucine
        'TTG' : 'L',    # Leucine
        'TAC' : 'Y',    # Tyrosine
        'TAT' : 'Y',    # Tyrosine
        'TAA' : 'Stop',    # Stop
        'TAG' : 'Stop',    # Stop
        'TGC' : 'C',    # Cysteine
        'TGT' : 'C',    # Cysteine
        'TGA' : 'Stop',    # Stop
        'TGG' : 'W',    # Tryptophan
        'CTA' : 'L',    # Leucine
        'CTC' : 'L',    # Leucine
        'CTG' : 'L',    # Leucine
        'CTT' : 'L',    # Leucine
        'CCA' : 'P',    # Proline
        'CCC' : 'P',    # Proline
        'CCG' : 'P',    # Proline
        'CCT' : 'P',    # Proline
        'CAC' : 'H',    # Histidine
        'CAT' : 'H',    # Histidine
        'CAA' : 'Q',    # Glutamine
        'CAG' : 'Q',    # Glutamine
        'CGA' : 'R',    # Arginine
        'CGC' : 'R',    # Arginine
        'CGG' : 'R',    # Arginine
        'CGT' : 'R',    # Arginine
        'ATA' : 'I',    # Isoleucine
        'ATC' : 'I',    # Isoleucine
        'ATT' : 'I',    # Isoleucine
        'ATG' : 'M',    # Methionine
        'ACA' : 'T',    # Threonine
        'ACC' : 'T',    # Threonine
        'ACG' : 'T',    # Threonine
        'ACT' : 'T',    # Threonine
        'AAC' : 'N',    # Asparagine
        'AAT' : 'N',    # Asparagine
        'AAA' : 'K',    # Lysine
        'AAG' : 'K',    # Lysine
        'AGC' : 'S',    # Serine
        'AGT' : 'S',    # Serine
        'AGA' : 'R',    # Arginine
        'AGG' : 'R',    # Arginine
        'GTA' : 'V',    # Valine
        'GTC' : 'V',    # Valine
        'GTG' : 'V',    # Valine
        'GTT' : 'V',    # Valine
        'GCA' : 'A',    # Alanine
        'GCC' : 'A',    # Alanine
        'GCG' : 'A',    # Alanine
        'GCT' : 'A',    # Alanine
        'GAC' : 'D',    # Aspartic Acid
        'GAT' : 'D',    # Aspartic Acid
        'GAA' : 'E',    # Glutamic Acid
        'GAG' : 'E',    # Glutamic Acid
        'GGA' : 'G',    # Glycine
        'GGC' : 'G',    # Glycine
        'GGG' : 'G',    # Glycine
        'GGT' : 'G',    # Glycine
        }    
    print(dna)
    for i in range(0,len(dna)-2,3):
        codon = dna[i:i+3]
        amino_acid += dna_codon[codon]
    print(amino_acid)
    prot = amino_acid.split("Stop")
    print(prot)
    for p in prot:
        for i in range(len(p)):
            if p[i] == "M":
                translated_protein.append(p[i:])
                break
    print(translated_protein)

if __name__ == "__main__":
    dna = parse_fasta("orf.txt")
    amino_acid_from_dna(dna)

    