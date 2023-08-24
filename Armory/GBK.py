"""Problem
GenBank comprises several subdivisions:

Nucleotide: a collection of nucleic acid sequences from several sources.
Genome Survey Sequence (GSS): uncharacterized short genomic sequences.
Expressed Sequence Tags, (EST): uncharacterized short cDNA sequences.

Given: A genus name, followed by two dates in YYYY/M/D format.
Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
"""

from Bio import Entrez

def genbank_entries(genus, date1, date2):
    """Given a genus name and two dates, get total count of all entries of the genus between the two dates specified

    Args:
        genus (string): Genus of the organism
        date1 (string): Date1
        date2 (string): Date2
    """
    Entrez.email = "your_name@your_mail_server.com"
    term = ('"{}"[Organism] AND "{}"[Publication Date] : "{}"[Publication Date]').format(genus,date1,date2)
    handle = Entrez.esearch(db = "nucleotide", term = term)
    record = Entrez.read(handle)
    print(record["Count"])

if __name__ == "__main__":
    with open("data/rosalind_gbk.txt", "r") as f1:
        genus_name = f1.readline().strip()
        date1 = f1.readline().strip()
        date2 = f1.readline().strip()
        genbank_entries(genus_name, date1, date2)
