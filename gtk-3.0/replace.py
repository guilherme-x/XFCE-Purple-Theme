fin = open("gtk-dark.css", "rt")
#output file to write the result to
fout = open("gtk-dark2.css", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('#3598db', '#832fef'))
#close input and output files
fin.close()
fout.close()
