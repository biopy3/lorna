import os,shutil

def handle_fasta_file(input_dir):
    li =[]
    for dirpath,dirnames,filenames in os.walk(input_dir):
        for filename in filenames:
            postfix = os.path.splitext(filename)[1]
            if postfix == '.fasta' or postfix == '.fas' or postfix == '.fa' or postfix == '.txt' or postfix == '.xfasta':
                li.append(os.path.join(dirpath,filename))
    return li

li = handle_fasta_file("./SSP")
for i in li:
    os.mkdir(os.path.splitext(i)[0])
    shutil.move(i,os.path.splitext(i)[0])
