"""
Computing GC Content

URL: https://rosalind.info/problems/gc/

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

gc_DNA = {}

def getGCFromFASTA(fastaFile,gc_DNA):
    """Get GC content for each string in the fast a file and add it to a dict

    Args:
        fastaFile (.fasta file): FASTA file
        gc_DNA (dict): Dict where GC content will be stored
    """
    sequence = ""
    with open(fastaFile,"r") as f1:
        for line in f1:
            line = line.strip()
            if line.startswith(">"):
                if sequence != "":
                    addGCToDict(sequence,gc_DNA,header)
                header = line[1:]
                gc_percent = float(0)
                sequence = ""
            else:
                sequence += line
    addGCToDict(sequence,gc_DNA,header)  

def getMaxGC(gc_DNA):
    """Get DNA sting with max GC percentage

    Args:
        gc_DNA (dict): Dict with GC content of each string

    Returns:
        header(str), gc_content(float): Prints the header and GC percentage of DNA string with highest GC percentage
    """
    max_gc = -1
    max_header = ""
    for dna,gc_perc in gc_DNA.items():
        if gc_perc > max_gc:
            max_gc = gc_perc
            max_header = dna
    print(max_header,"\n",max_gc)

def addGCToDict(seq,gc_DNA,header):
    gc_percent = ((seq.count("G") + seq.count("C"))/len(seq))*100
    gc_DNA[header] = gc_percent

if __name__ == "__main__":
    getGCFromFASTA("gc.fasta",gc_DNA)
    getMaxGC(gc_DNA)

