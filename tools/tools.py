import os,shutil,csv,subprocess
from Bio import SeqIO
from Bio import Entrez
import re,multiprocessing,sys


def juge_os_and_set_PATH():
    if os.name == 'posix' and sys.version_info[0] == 3:
        os.environ['PATH'] = os.environ['PATH'] + ':' + os.getcwd() + '/tools/softwares'
        print("Unix Done!\n",os.environ['PATH'])
    
    else:
        os.environ['PATH'] = os.environ['PATH'] + ';' + os.getcwd() + '/tools/softwares'
        print("Windows Done!\n",os.environ['PATH'])


def inputdir():
    s = input("Please put in dir:").strip().strip('\'')
    return s


def getfile(inputdir=inputdir(),patterns=[]):
    files = []
    for dirpath,dirnames,filenames in os.walk(inputdir): 
        for pattern in patterns:
            for filename in filenames:
                status = re.search(pattern,filename,flags=0)
                if status:
                    files.append(os.path.join(dirpath,filename))
    return files


def getexceptfile(inputdir=inputdir(),patterns=[]):
    files = []
    for dirpath,dienames,filenames in os.walk(inputdir):
        for pattern in patterns:
            for filename in filenames:
                status = re.search(pattern,filename,flags=0)
                if status:
                    pass
                else:
                    files.append(os.path.join(dirpath,filename))
    return files

def remove(files):
    for file in files:
        os.remove(file)
    print("removed!")

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

def downloadseq(csvfiles,column_filname,column_accession):
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
                if records[i].id.strip() == records[j].id.strip() or records[i].seq.strip() == records[j].seq.strip():
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
        SeqIO.write(records,fasfile,"fasta")

def clustalw(file):
    #try:
    subprocess.call(["clustalw2","-INFILE="+file,"-ALIGN","-QUIET","-OUTPUT=FASTA","-OUTFILE="+ os.path.splitext(file)[0]+'_aligned.fasta'])
    os.remove(os.path.splitext(file)[0]+'.dnd')
        #except:
#print("This file is wrong:"+file.split('/')[-1])

def multiclustalw(files):
    pool = multiprocessing.Pool(processes=len(files))
    pool.map(clustalw,files)
    print("Clustalw done.")

    
if __name__ == "__main__":
    pass
