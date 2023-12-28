"""
Finding Genes with ORFs

URL: https://rosalind.info/problems/orfr/

Given: A DNA string s of length at most 1 kbp.

Return: The longest protein string that can be translated from an ORF of s. If more than one protein string of maximum length exists, then you may output any solution.
"""

from Bio.Seq import Seq
from Bio.Seq import reverse_complement
import re

def longest_protein_string(dna):
    prot = []
    dna_seq = Seq(dna)
    rc = reverse_complement(dna_seq)
    x = re.findall("^ATG.*TAA$", dna)
    # prot.append(dna_seq.translate())
    # prot.append(rc.translate())
    print(x)

# if __name__ == "__main__":
#     with open("data/orf.txt", "r") as f1:
#         next(f1)
#         dna = f1.readline().strip()
#         print(dna)
#         longest_protein_string(dna)

# s1 = Seq("ATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
# print(s1.translate())
# s = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
# s_rc = reverse_complement(s)
# print(s_rc)
# s2 = Seq("ATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGAGTTAGCTACATGGCT")
# print(s2.translate())

# txt = "The rain in Spain"
# x = re.findall("^The.*Spain$", txt)
# print(x)

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE:
        protein = DNA_CODON_TABLE[codon]
    return protein


def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def possible_protein_strings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translate_codon(s[i:i+3])
        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        found_stop = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = translate_codon(s[j:j+3])

            if not protein:
                break

            if protein == 'Stop':
                found_stop = True
                break

            protein_string += protein

        if found_stop:
            results.append(protein_string)

    return results


if __name__ == "__main__":

    # small_dataset = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    large_dataset = open('data/rosalind_orf.txt').read().strip()
    # large_dataset = "ACTCCAGCGGTAGAAGCGACTGTTCTAAACCCACCGGAGTGGCCTGGTCAAATGTATAGGAATTTATGTTCAAAAGCCCCGGACGGACGGCCGAACCCCCCCGAAGAGCAGACCCAAGGGAGCCTACCGCTCTCACGCAATCGACGCAAGGGTGGCAATTCTCTAAGCCGTTGGCTACCGGCGTCCCGGCTCTCCTTCATTGGTGTAGGTGAACGTCTCGTTGCAAGGTGGCAATCACTTATAACGGTTCTCCTTAGACGAACCATTTCATGGCCCTATGTGAGCGTGCGGCTTAAGATTGATGGTGCCAATTTACAACGTTCATTCTATCGTGAATAGATACGTGTCTACTACTTACTTTTTGTGATTACAAATTGAGAATAACTCACAACATTTTCCTTGCGAGTAGTCTTAATTCTAGGCTTTAAATTACATAGGCGGTGAGCTTTAGTGGTTCCTGGTTATGTGGGGGCGTGTATGCCCAAGATGCTCATTTAGCTAAATGAGCATCTTGGGCATTCACGCCGAACCGGCTGCACTCCGCGAGGCGCACGTTAAAGGCCTAGTCGTCCCACGACACGACACACTTTCAACAGATGGTATAGGAGTGAAAGCAACAGGCACTTGCTAGCGATTGAGGTCGGATGAGCGCTAGAAGGCCGGGTCCCGGTATGCCTATGGGTGGAGGACTATCTGAATATCGAGAGGGCAAGACGCCTCTGAGCAAGACCCGGTGAATTCGGCATTCACCCTCTAGTTGATGTCCGCTCGTGTCGCCAGTGGGGTCATTAGCTCGCCTAGAAATCAGGGATGATCTCGGCCAGTGGGCAAAGACTTATCTCGTAATAGAGAGGGCACCCTGATTAGCATAGTCACATTTAGCCTCGCTGTCTAGGAGCGTCAACCTATGCTCTGGTACAACACCCGGTGTCACCGGTTATTGTTATCCTAGGTGGTTAGAATCACATTGTGGCAGTTCTCTCCATCTCGCTGCCA"
    large_dataset = "CTAGTGAGTGTCGTCTAGTAGTTAATGGCCCTTTTTTCAGTGGACCGTGACTCTAAATGCTAAGGATTCCGCTTGCTTTTACACCAAGGGGCACATTTACTAACCAGCAGAATGTCAATAGATGGACAACGCAGCTCTGTCTATGGAATCCGATGCCTGAACGCAATTAGAGTGGGACAGGCCGAGGAGCACGTGCGGAAGGTAAGTTCATCCCCCGCTCAGTCACTTTTGAGCCAGCCGGCTGTTTGTTCCACTTGAACACTGAATCGTAAGTGACATTCGATGTCTGCTCTTCAGATTTCCAGCCCCAAGATAGAATGAGATTACTCCGTCAAAAAAGGAGTTGATGGAGATACAGACCTATGCTCGAATCAGCCAGTTTAGGGAGGCCGCTACTTGGTGGAAGCACATCCCCCTCCACCCCATATTATTCGAGGATTCTTCCACTACACGCCCTGGCCTTACCGTATCGAATATGACTGGTATCTATTCGAACTAGCTAGTTCGAATAGATACCAGTCATCCAGAGTGGAACCCTGGCCCTTTTCTGAGCTGAACAATCTGGTAAATTATCTCGTCCGCTCTCGCTGCAGGGGGCTTCTTACGGTATAGCACTACGACGCCCATGACTACGGTGAAAATCGCCTCGTCACAGGCTCCGCTTTCGGTTGAAATAGCAGTGGTTCCAGTAGCGCGTTAAATTGATACAATGCATCCAATGACCATTCCTTGGCCGCATTGTGAACGCACCTCCCGACGGTGCGCCAAACTATGCCCTCTTCAGTTCGATGCCGGCCAGCACTTGCGTTTTCATACGGGCACGGTGGTTCGCTAGGTACTGTATTTAAACCCCTGGACACCGAACCATAACCGTGTAACAGGCTTACAAGCGCGGTACGTGCTTGTACCTCTTTATCGTGTAATCCCATAATCGTGACTGGCCCCTGGAAACGTTTCCTTAGGACTCTACAGGAGTTACGACGCCGGTGGAGTACCGT"
    print(large_dataset)

    possible_a = possible_protein_strings(large_dataset)
    possible_b = possible_protein_strings(reverse_complement(large_dataset))
    print ("\n".join(set(possible_a + possible_b)))