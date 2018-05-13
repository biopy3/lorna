import subprocess,os

input_dir = input("Please put in a path of dirctory:").strip().strip('\'')
os.environ['PATH'] = os.environ['PATH']+':'+os.getcwd()
def handle_fasta_file(input_dir):
    li =[]
    filename = []
    for dirpath,dirnames,filenames in os.walk(input_dir):
        for filename in filenames:
            postfix = os.path.splitext(filename)[1]
            if postfix == '.fasta' or postfix == '.fas' or postfix == '.fa' or postfix == '.txt' or postfix == '.xfasta':
                file_path = os.path.join(dirpath,filename)
                filename = os.path.splitext(filename)[0]
                tuple = file_path,filename
                li.append(tuple)
    return li

li= handle_fasta_file(input_dir)
print(li)
for i in li:
    try:
        output_dir = os.getcwd()+'/results/'
        ps = subprocess.call(["clustalw2","-INFILE="+i[0],"-ALIGN","-QUIET","-OUTPUT=FASTA","-OUTFILE="+output_dir+i[1]+'_aligned.fasta'])
    except:
        print("The file is wrong:"+i[0])
        continue
