import string
import random
import subprocess
import os


def pass_generate(size=14, chars=string.ascii_uppercase + string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))
	
def create_file_list(dir="./reports"):
	f = open("files.txt", "w")
	for root, dirs, filenames in os.walk(dir):
		for file in filenames:
			#print os.path.splitext(file)[0]
			f.writelines(os.path.splitext(file)[0] + "=" + pass_generate() + "\n")
	f.close()

create_file_list()

f = open("files.txt", "r")
lines = f.readlines()
for line in lines:
	myfilename = "reports\\" + line.split("=")[0]
	mypassword = line.split("=")[1]
	print myfilename
	print mypassword

	mycommand = "\"C:\\Program Files\\7-Zip\\7z.exe\"" + " a \""+  myfilename + ".7z\" \"" + myfilename + ".pdf\"" + " -p" + mypassword
	print mycommand

	print subprocess.Popen(mycommand,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
	
f.close()
exit()


