"""
Finding a Protein Motif

URL: https://rosalind.info/problems/mprt/

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

from __future__ import print_function
import re 


motif = re.compile('(?=N[^P][ST][^P])')

# loop through protein id's to import from uniprot website
# import urllib2
from urllib.request import urlopen  
from Bio import SeqIO

# dataset = open("data/rosalind_mprt.txt", 'r')
dataset = open("data/mprt.txt", 'r')
protein_ids = dataset.readlines()
dataset.close()

outhandle = open("MPRT.txt", 'w')
uniprot_url = "http://www.uniprot.org/uniprot/"

for protein in protein_ids:
    request = urlopen.Request("".join([uniprot_url+protein.rstrip()+".fasta"]))
    opener = urlopen.build_opener()
    f = opener.open(request)
    raw_data = SeqIO.read(f, 'fasta')
    print(raw_data)
    f.close()

    locations = []
    # Use search instead of match to search entire string
    if re.search(motif, str(raw_data.seq)):
        print(protein.strip(), file=outhandle)
        for m in re.finditer(motif, str(raw_data.seq)):
            locations.append(m.start()+1)
        print(" ".join(map(str, locations)), file=outhandle)
        
outhandle.close()