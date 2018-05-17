import os,shutil,csv,subprocess
from Bio import SeqIO
from Bio import Entrez

def inputdir():
	return input("Please put in dir:").strip().strip('\'')

def gettypefile(inputdir=inputdir(),types=[]):
    files =[]
    for dirpath,dirnames,filenames in os.walk(inputdir):
        for filename in filenames:
            postfix = os.path.splitext(filename)[1]
            for typ in types:
                if postfix == '.'+typ:
                    li.append(os.path.join(dirpath,filename))
    return files

def underdir(files):
    for i in files:
        os.mkdir(os.path.splitext(i)[0])
        shutil.move(i,os.path.splitext(i)[0])
    print('Done!')

def modifseqid(files):
    for file in files:
        records = list(SeqIO.parse(file,'fasta'))
        for record in records:
            description = record.description.split(' ')
            record.id = description[1]+'_'+description[2]+'_'+record.id
            record.description = ''
            SeqIO.write(records,file,'fasta')
    print("Done!")

def downloadseq(csvfiles=[],column_filname,column_accession):
    Entrez.email = 'wr695251173@163.com'
    for csvf in csvfiles:
        with open(csvf, newline='') as csvfile:
            reader = csv.reader(csvfile)
            count = 1
            for row in reader:
            filename=row[column_filename]
                accession=row[column_accession]
                try:
                    net_handle = Entrez.efetch(db="nucleotide",id=accession,rettype="fasta",retmode="text")
                    out_handle = open("data/"+filename,"a")
                    out_handle.write(net_handle.read())
                    out_handle.close()
                    net_handle.close()
                    print("Saved "+i+"!")
                    count = count + 1
                except:
                    print("failure download(accession number):"+accession)
                    continue
def locarna(files):
    for input_file in files:
	try:
		output_dir = os.path.splitext(input_file)[0]
		print(input_file)
		ps = subprocess.Popen(["mlocarna",input_file,"--tgtdir",output_dir+"_results/","--write-structure"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output_lines = ps.stdout.readlines()
		error_lines = ps.stderr.readlines()
		f = open(output_dir+"_results/RNAalifold.txt","w")
		for line in output_lines:
			f.write(str(line,encoding = "utf-8"))
		f.close()
		f = open(output_dir+"_results/error_info.txt","w")
		for line in error_lines:
			f.write(str(line,encoding = "utf-8"))
		f.close()

	except:
		print("The file is wrong:"+input_file)
		continue

def solvedup(files):
    for fasfile in files:
        records = list(SeqIO.parse(fasfile,"fasta"))
        length = len(records)
        i = 0
        while i < length:
            j = i+1
            while j < length:
                if records[i].id.strip() == records[j].id.strip() or records[i].seq.strip() == records[i.seq.strip()]:
                    if len(records[i]) > len(records[j]):
                        records.pop(j)
                        j = j-1
                        print("Removed!")
                    else:
                        records.pop(i)
                        j = i+1
                        print("Reomved!")
                    length = length - 1
                j = j+1
            i = i+1
        SeqIO.write(records,filename,"fasta")

if __name__ == "__main__":
    pass
