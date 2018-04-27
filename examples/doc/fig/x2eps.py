#!/usr/bin/python

import os
import sys

name=sys.argv[1]

if ".tex" in name:
    name=name.split(".")[0]

command="rm -f "+name+".eps"
os.system(command)
command="rm -f "+name+".pdf"
os.system(command)


# Make backup
command="cp -f "+name+".tex "+name+"_tmp.tex"
os.system(command)

inFile=open(name+".tex","r")
outFile=open(name+"_tmp.tex","w")

outFile.write("\\documentclass{minimal}\n")
outFile.write("\\usepackage{graphicx}\n")
outFile.write("\\usepackage{color}\n")
outFile.write("\\usepackage{amsmath}\n")
#outFile.write("\\usepackage[T1]{fontenc}\n")
#outFile.write("\\usepackage{relsize}\n")
outFile.write("\\usepackage[paper=a0paper]{geometry}\n")
outFile.write("\\newcommand{\\mr}[1]{\\mathrm{#1}}\n")
outFile.write("\\newcommand{\\jj}{\\mathrm{j}}\n")

outFile.write("\\usepackage[Symbolsmallscale]{upgreek}\n")
outFile.write("\\let\\omega\\upomega\n")
outFile.write("\\let\\pi\\uppi\n")

outFile.write("\\begin{document}\n")
for line in inFile:
    outFile.write(line)
outFile.write("\\end{document}\n")

inFile.close()
outFile.close()

command="latex "+name+"_tmp"
os.system(command)
command="dvips "+name+"_tmp"
os.system(command)
command="ps2eps -l "+name+"_tmp.ps"
os.system(command)
command="epstopdf "+name+"_tmp.eps"
os.system(command)
command="mv "+name+"_tmp.eps "+name+".eps"
os.system(command)
command="mv "+name+"_tmp.pdf "+name+".pdf"
os.system(command)

# Clean up files
command="rm -f "+name+"_tmp.tex"
os.system(command)
command="rm -f "+name+"_tmp.aux"
os.system(command)
command="rm -f "+name+"_tmp.log"
os.system(command)
command="rm -f "+name+"_tmp.dvi"
os.system(command)
command="rm -f "+name+"_tmp.ps"
os.system(command)
command="rm -f "+name+".eps"
os.system(command)

