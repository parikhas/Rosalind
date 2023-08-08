"""Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)
"""
def removeIntrons(fastafile):
    """Remove intron sequences from dna sequence

    Args:
        fastafile (file): .fasta file

    Returns:
        sequence(str): DNA string with introns removed
    """
    sequence = ""
    intron_seq = ""
    string_num = 0
    with open(fastafile,"r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">"):
                if sequence != "":
                    if intron_seq != "":
                        sequence = sequence.replace(intron_seq,"")
                        intron_seq = ""
                string_num += 1

            else:
                if string_num == 1:
                    sequence += line
                else:
                    intron_seq += line
    sequence = sequence.replace(intron_seq,"")
    return sequence

def protFromExons(sequence):
    """Convert dna sequence to amino acid sequence

    Args:
        sequence (str): DNA sequence

    Returns:
        amino acid sequnece (str): Amino acid sequence
    """
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
    prot_seq = ""
    for i in range(0,len(sequence)-2,3):
        amino_acid = dna_codon[sequence[i:i+3]]
        if amino_acid != "Stop":
            prot_seq += amino_acid
    print(prot_seq)

if __name__ == "__main__":
    seq = removeIntrons("splc.fasta")
    protFromExons(seq)




