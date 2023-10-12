"""
Data Formats

URL: https://rosalind.info/problems/frmt/

GenBank can be accessed here. A detailed description of the GenBank format can be found here. A tool, from the SMS 2 package, for converting GenBank to FASTA can be found here.

Given: A collection of n (n≤10) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format.
"""

from Bio import Entrez
from Bio import SeqIO

def shortest_string(genbank_ids):
    Entrez.email = "your_name@your_mail_server.com"
    handle = Entrez.efetch(db="nucleotide", id=[genbank_ids], rettype="fasta")
    records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
    smallest_seq_len = float("inf")
    smallest_rec = None
    for each_record in records:
        if len(each_record.seq) < smallest_seq_len:
            smallest_seq_len = len(each_record.seq)
            smallest_rec = each_record
    print(smallest_rec.format("fasta"))

if __name__ == "__main__":
    with open("data/rosalind_frmt.txt", "r") as f1:
        genbank_ids_l = f1.readline().strip().split(" ")
        genbank_ids_s = ", ".join((i for i in genbank_ids_l))
        shortest_string(genbank_ids_s)
    

    
