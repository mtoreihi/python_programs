#!/usr/bin/env python

# Find & Replace program by Mehran Toreihi
# 1394-08-14

import subprocess
import os

# Define path
mypath = "/mtoreihi/path"
myfile = "words.txt"


# Open list of words from file
try:
	fp = open(myfile,'r')
except:
	print "Can not open file for reading"

# Loop through every line in file
for line in fp:
	try:
		wf,wr = line.split('=')
	except:
		print "File format is wrong. It should be word_find=word_replace per line."
		fp.close()
		exit()
	wf = wf.rstrip()
	wr = wr.rstrip()
	# check for bad file format
	if wf == '' or wr == '':
		print "File format is wrong. It should be word_find=word_replace per line."
		fp.close()
		exit()
	# loop through file content
	for p,d,f in os.walk(mypath):
		for files in f:
			file_path = p + '/' + files
			# call sed and replace for each word in another process
			substitute = 's/' + wf + '/' + wr + '/g'
			subprocess.Popen(['sed', '-i', substitute, file_path])
	
	# loop through file & directory names
	for p,d,f in os.walk(mypath):
		for dirs in d:
			if (dirs.find(wf) != -1):
				# replace dir names
                newname = dirs.replace(wf,wr)
                oldpath = p + "/" + dirs
                newpath = p + "/" + newname
				substitute = "mv " + oldpath + " " + newpath
				os.system(substitute)
		for files in f:
			if (files.find(wf) != -1): 
                newname = files.replace(wf,wr)
                oldpath = p + "/" + files
                newpath = p + "/" + newname
				substitute = "mv " + oldpath + " "  + newpath
				os.system(substitute)
fp.close()
