Coming soon a more organized main website hosted on GITHUB explaining what and how this repository works:

main page:
https://johngalt01.github.io/


![IMG_0553](https://github.com/user-attachments/assets/45e866a8-92a6-4d58-9040-7920d4e22e82)

This project is ment to work with THE LINKS,LINKS2,ELINKS Text browser,
In conjuction with the FABGL VGA32 ANSI Color Terminal.

https://github.com/johngalt01/johngalt01.github.io/blob/main/DSCN5986.JPG

You will have to setup one of the browsers above, I recommend ELINKS, on a Raspberry PI.

set terminal to max resolution 512x384,64 colors

the main script to use is: JPGTOFABGL.py for outputing jpg to the fabgl terminal.

set your telnet terminal 
LINES to 45-48
and 
COLUMNS to 80-83 
depending on your monitor.

When using any of the browsers above know they are extremely buggy
they can crash and start to generate a tmp file that will fill your
harddrive until system crash. I would isolate things.
 
for Elinks
i would setup a alias
alias elinks="elinks -no-connect -touch-files 1"

DO NOT use the bookmarks function in these browsers as it tends to make them go crazy.

here is my elinks.conf file which setups up the file associations.

https://github.com/johngalt01/johngalt01.github.io/blob/main/elinks.conf

You can use cat to output to the serial terminal
or use a small shell program:

#!/bin/bash
echo "$(<$1)"

that will pipe to the stdout.

the configuration file below sets the browser to automatically download and run cat which will send the escape codes to your terminal
i named the escape character files BMP because Elinks got confused with using VT file extensions.

python script settings can be edited from within ELINKS to customize how to display the image.

Automatic mode "python jpgtofabgl %f A N 0 0 100 2"

works best, Semi Automatic mode tends to crash the ELINKS browser as it does not like an 
external keypress to tell the script what to do.

<hr>

added a GEOFF Graphics terminal verson of the script

https://github.com/johngalt01/johngalt01.github.io/blob/main/jpgtogeoff.py

problem is the GEOFF terminal does not even have basic VT100 support and no browers will work with it.
but you can use it to display jpg images on your terminal screen.

you also need my graphics patch to be able to use this.

https://github.com/johngalt01/GEOFF-USB-Terminal-Graphics-Patch

i would compile the python code before using.

example usage:

./jpgtogeoffc cat.jpg A T 0 0 150 0 1  

only use in transperency mode T this is due to how the pixels can be turned on or off with the GEOFF terminal. always blank the terminal with the trailing 1 and you can only use B&W bitmap mode.

here is the cat.jpg image displayed on the GEOFF Terminal

![DSCN6428](https://github.com/user-attachments/assets/bb4314d4-1cb9-42dd-8ba8-93d04c0b014c)

