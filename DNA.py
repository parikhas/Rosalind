"""Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.
"""

def getBaseCountsFromString(string):
    """Get count of bases from DNA string

    Args:
        string (str): DNA string

    Returns:
        (str): String containing counts of A,C,G and T in the same order.
    """
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for base in string:
        if base == "A":
            A_count += 1
        elif base == "C":
            C_count += 1
        elif base == "G":
            G_count += 1
        elif base == "T":
            T_count += 1
    print((" ".join((str(A_count),str(C_count),str(G_count),str(T_count)))))

if __name__ == "__main__":
    getBaseCountsFromString("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
