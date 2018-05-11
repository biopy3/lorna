import subprocess,os

input_dir = input("Please put in a path of dirctory:").strip().strip('\'')
print(input_dir)
def handle_fasta_file(input_dir):
	li =[]
	for dirpath,dirnames,filenames in os.walk(input_dir):
		for filename in filenames:
			postfix = os.path.splitext(filename)[1]
			if postfix == '.fasta' or postfix == '.fas' or postfix == '.fa' or postfix == '.txt' or postfix == '.xfasta':
				li.append(os.path.join(dirpath,filename))
	return li

li = handle_fasta_file(input_dir)
print(li)
for input_file in li:
    try:
	output_dir = os.path.splitext(input_file)[0]
	print(input_file)
	ps = subprocess.Popen(["clustalw",],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output_lines = ps.stdout.readlines()
	f = open(output_dir+"_results/RNAalifold.txt","w")
	for line in output_lines:
		f.write(str(line,encoding = "utf-8"))
	f.close()

    except:
	print("The file is wrong:"+input_file)
	continue
