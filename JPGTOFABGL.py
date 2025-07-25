# Ver 0.64.5 07/24/2025 
# By John Galt Furball1985

# Change to Python 3

# added new arguement 7 which has 2 B&W picture modes and the Color mode

# you can also compile this script to make it faster
# python -m py_compile jpgtofabgl creates jpgtofabglc
# make sure to change permissions to allow it to run : chmod +x jpgtofabglc
# change to RGB to RGBA dealing with website transparency

# Fixed Cleanup and exit

# added terminal blocking mode

# python3 JPGTOFABGL %f A T 0 0 100 2 0: set Auto mode, Transparent pictures, x(not used), y(not used), width 100 pixels, color mode
# jpgtofabglc %f M N 25 75 50 0 0: set Manual mode, solid picture, x=25, y=75, width 50 pixels, 1 bit b&w mode


from PIL import Image
import sys, termios, tty, os, time, getch

arg1 = sys.argv[1] # filename
arg2 = sys.argv[2] # Auto, Semi, Manual mode Don't use Semi when using Elinks.
arg3 = sys.argv[3] # T transparency 'T' or not 'N'ot a 't'
arg4 = sys.argv[4] # X
arg5 = sys.argv[5] # Y
arg6 = sys.argv[6] # resize limit 
arg7 = sys.argv[7] # 0 black and white, 1 black and white 4 levels, 2 color
arg8 = sys.argv[8] # block terminal elinks yes or no 1 or 0

esc=chr(27)

if arg8 == "1": # we are blocking terminal so clear screen
 print (esc+"[2J")

FILENAME=arg1 #image can be in gif jpeg or png format

#automatic resize

image = Image.open(FILENAME)
tempimage='temp.png'

image.thumbnail((int(arg6),int(arg6)))

if arg7 == "0":
 imageout = image.convert("1",dither=Image.FLOYDSTEINBERG, palette=Image.WEB, colors=1)
 imageout.save(tempimage)
 im=Image.open(tempimage).convert('RGBA')

elif arg7 == "1":
 imageout = image.convert("L",dither=Image.FLOYDSTEINBERG, palette=Image.WEB, colors=4)
 imageout.save(tempimage)
 im=Image.open(tempimage).convert('RGBA') 

else:
 imageout = image.convert("P",dither=Image.FLOYDSTEINBERG, palette=Image.WEB, colors=64)
 imageout.save(tempimage)
 im=Image.open(tempimage).convert('RGBA')

pix=im.load()
w=im.size[0]
h=im.size[1]
YY=w
XX=h

# Automatic mode one image centered screen
if arg2=="A" or arg2=="a": 
 PS=512-YY
 PS2=384-XX
 PS=PS/2
 PS2=PS2/2 # The Picture in the Center of the screen X: PS2 Y: PS
 offsetx=PS
 offsety=PS2


# Semi-Automatic mode user positions possible center,left,right,middle
if arg2=="S" or arg2=="s":
 
 while True: 
  key = getch()
  if key=="L" or key=="l" or key=="R" or key=="r" or key=="M" or key=="m" or key=="C" or key=="c" or key=="Q" or key=="q":
   break

 if key=="L" or key=="l": #image left-top
  offsetx=128-(YY/2)
  offsety=40

 elif key=="R" or key=="r": #image right-top
  offsetx=384-(YY/2)
  offsety=40

 elif key=="M" or key=="m": #image middle-top
  offsetx=256-(YY/2)
  offsety=40

 elif key=="C" or key=="c": #image centered on screen
  PS=512-YY
  PS2=384-XX
  PS=PS/2
  PS2=PS2/2
  offsetx=PS
  offsety=PS2

 elif key=="Q" or key=="q" or key==chr(27):
  im.close()
  image.close()
  sys.exit()
  
 else: #just exit out if you push wrong button
  im.close()
  image.close()
  sys.exit()

# Manual Mode
if arg2=="M" or arg2=="m": # Honor user X,Y from Command prompt 
 offsetx=int(arg5)
 offsety=int(arg4)

#if arg8 == "1": # we are blocking terminal so clear screen
# print (esc+"[2J")
print (esc+"_E0")
#  OUTPUT TO FABGL TERMINAL IN COLOR
if w<=500 and h<=350: # Range check to make sure we don't go nuts 500 x 350 resolution
 for i in range(w):
    for j in range(h):
      
       if arg3=="T" or arg3=="t":
        # IMAGE IS TRANSPARENT 

        if pix[i,j][0]!=0 and pix[i,j][1]!=0 and pix[i,j][2]!=0:
         print(esc+"[H")
         print(esc+"_GPEN"+str(pix[i,j][0])+";"+str(pix[i,j][1])+";"+str(pix[i,j][2]))	
         print(esc+"_GPIXEL"+str(i+offsetx)+";"+str(j+offsety))

       else:
        # IMAGE IS NOT TRANSPARENT
        print(esc+"[H")
        print(esc+"_GPEN"+str(pix[i,j][0])+";"+str(pix[i,j][1])+";"+str(pix[i,j][2]))	
        print(esc+"_GPIXEL"+str(i+offsetx)+";"+str(j+offsety))
      
print (esc+"_E1")
print (esc+"_F0;46")
print (esc+"_GPEN255;255;255")

if arg8 == "1": # halt for keypress here and i need LINES and COLUMNS
 LINES1=int(os.environ["LINES"])
 COLUMNS1=int(os.environ["COLUMNS"])
 LINES1=LINES1-1
 COLUMNS1=(COLUMNS1/2)-11
 raw_input(esc+"["+str(LINES1)+";"+str(COLUMNS1)+"fPress Enter to Return.")

im.close()
image.close()
sys.exit()

