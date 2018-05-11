from Bio import Entrez
import csv

species = set()
Entrez.email = 'wr695251173@163.com'

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        filename=row[0]
        accession=row[2]
        try:
            net_handle = Entrez.efetch(db="nucleotide",id=accession,rettype="fasta",retmode="text")
            out_handle = open("data/"+filename,"a")
            out_handle.write(net_handle.read())
            out_handle.close()
            net_handle.close()
            print("Saved!")
        except:
            print(accession)
            continue
        
