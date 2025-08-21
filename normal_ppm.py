# normal_ppm.py this will take output from convert making a jpg into a ppm then normalize the ppm in a better format.

# first run this to convert JPG to a PPM format
# 
# convert original.jpg -resize 500 resized.jpg
# convert original.jpg -compress none new.ppm
# python normal_ppm new.ppm final_new.ppm

import sys

filenamein = sys.argv[1]
filenameout = sys.argv[2]

file = open(filenamein, 'r')
outfile = open(filenameout, 'w')


#setup the first 4 lines.
dot=1

the_return="\r\n"

the_header="# Created by GIMP version 2.10.38 PNM plug-in\r\n"

while 1:

    # read by character
    char = file.read(1) 
    
    # break out of while loop
    if not char:
        break

    if dot >4 and ' ' not in char and '\n' not in char:   
           outfile.write(char)

   
    if dot <=4 and '\n' not in char:   
           outfile.write(char)

    if dot <=4 and '\n' in char:
           outfile.write(the_return)
           dot+= 1
           #print(dot)  

    if dot==2:
           outfile.write(the_header)
           dot+= 1
           #print(dot)
   
    if dot>4 and ' ' in char:
           outfile.write(the_return)
                
file.close()

