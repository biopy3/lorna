import os,shutil
from Bio import SeqIO

def input_dir():
	return input("Please put in dir:").strip().strip('\'')

def handle_fasta_file(input_dir):
    li =[]
    for dirpath,dirnames,filenames in os.walk(input_dir):
        for filename in filenames:
            postfix = os.path.splitext(filename)[1]
            if postfix == '.fasta' or postfix == '.fas' or postfix == '.fa' or postfix == '.txt' or postfix == '.xfasta':
                li.append(os.path.join(dirpath,filename))
    return li

def mkdir_mv_into_dir(files):
	for i in files:
		os.mkdir(os.path.splitext(i)[0])
		shutil.move(i,os.path.splitext(i)[0])

def extract_sequence_name(files):
	for file in files:
		records = list(SeqIO.parse(file,'fasta'))
		for record in records:
			description = record.description.split(' ')
			record.id = description[1]+'_'+description[2]+'_'+record.id
			record.description = ''
			print(record.id,record.description)
		SeqIO.write(records,file,'fasta')
	print("Done!")

if __name__ == "__main__":
	extract_sequence_name(handle_fasta_file(input_dir()))