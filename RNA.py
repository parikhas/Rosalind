"""
Transcribing DNA into RNA

URL: https://rosalind.info/problems/rna/

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

def RNAFromDNA(DNA):
    """Return RNA given a DNA string

    Args:
        DNA (str): DNA string

    Returns:
        (str): RNA string
    """
    return print((DNA.replace("T","U")))

if __name__ == "__main__":
    RNAFromDNA("GATGGAACTTGACTACGTAAATT")