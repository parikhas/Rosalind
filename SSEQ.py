"""
Finding a Spliced Motif

URL: https://rosalind.info/problems/sseq/

A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).
As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""

def subsequence_index(string1,string2):
    """Get indices of substring 2 in subtring 1

    Args:
        string1 (str): DNA string1
        string2 (str): DNA string2
    """
    sub_idx = []
    string2_l = [i for i in string2]
    for i in range(len(string1)):
        if len(string2_l) > 0:
            if string1[i] == string2_l[0]:
                string_idx = i + 1
                sub_idx.append(string_idx)
                del string2_l[0]
        else:
            break

    print(*sub_idx)

def get_strings_from_fasta(fasta):
    """Get strings from fasta

    Args:
        fasta (file): FASTA file containing sequence strings

    Returns:
        (str): Sequence strings 
    """
    s1 = ""
    s2 = ""
    header_count = 0
    with open(fasta,"r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">"):
                header_count += 1
            else:
                if header_count == 1:
                    s1 += line
                else:
                    s2 += line
    return (s1,s2)

if __name__ == "__main__":
    string1,string2 = get_strings_from_fasta("data/rosalind_sseq.txt")
    subsequence_index(string1,string2)

                
