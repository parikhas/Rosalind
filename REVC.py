"""
Complementing a Strand of DNA

URL: https://rosalind.info/problems/revc/

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

def reverseComplementString(DNA):
    """Get reverse complement of DNA string

    Args:
        DNA (str): DNA string

    Returns:
        (str): Reverse complement of DNA string
    """
    new_string = ""
    base_complement = {"A":"T","G":"C","C":"G","T":"A"}
    for i in range(len(DNA),0,-1):
        new_string += base_complement[DNA[i-1]]
    print(new_string)
    
if __name__ == "__main__":
    reverseComplementString("AAAACCCGGT")