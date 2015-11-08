#!/usr/bin/env python

# Find & Replace program by Mehran Toreihi
# 1394-08-14

import subprocess
import os

# Define path
mypath = "/opt/mtoreihi/test"
myfile = "words.txt"


# Open list of words from file
try:
	fp = open(myfile,'r')
except:
	print "Can not open file for reading"

# Loop through every line in file
for line in fp:
	wf,wr = line.split('=')
	wf = wf.rstrip()
	wr = wr.rstrip()
	# check for bad file format
	if wf == '' or wr == '':
		print "File format is wrong. It should be word_find=word_replace per line."
		fp.close()
		exit()
	for p,d,f in os.walk(mypath):
		for files in f:
			file_path = p + '/' + files
			# call sed and replace for each word in another process
			substitute = 's/' + wf + '/' + wr + '/g'
			subprocess.Popen(['sed', '-i', substitute, file_path])
	

fp.close()
