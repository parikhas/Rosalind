"""
Calculating Protein Mass

URL: https://rosalind.info/problems/prtm/

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""

def make_mass_table(mass_file):
    mass_dict = {}
    with open(mass_file, "r") as f1:
        for line in f1:
            line = line.strip()
            line = line.split()
            # print(line)
            amino_acid = line[0]
            mass = float(line[1])
            mass_dict[amino_acid] = mass
    return mass_dict

def calculate_protein_mass(string, mass_dict):
    protein_mass = 0
    for i in string:
        protein_mass += mass_dict[i]
    return round(protein_mass,3)

if __name__ == "__main__":
    with open("data/rosalind_prtm.txt", "r") as f:
        prot_string = f.readline().strip()
    prot_mass_table = make_mass_table("data/prot_mass.txt")
    print(calculate_protein_mass(prot_string, prot_mass_table))
    