import subprocess,multiprocessing,os

def clustalw(file):
    try:
        subprocess.call(["clustalw2","-INFILE="+file,"-ALIGN","-QUIET","-OUTPUT=FASTA","-OUTFILE="+ os.path.splitext(file)[0]+'_aligned.fasta'])
        os.remove(os.path.splitext(file)[0]+'.dnd')
    except:
        print("This file is wrong:"+file.split('/')[-1])

def multiclustalw(files):
    pool = multiprocessing.Pool(processes=len(files))
    pool.map(clustalw,files)
    print("Clustalw done.")
		
if __name__ == '__main__':
    pass