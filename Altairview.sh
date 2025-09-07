#!/bin/bash
# simplify the jpgtofabgl converter for use on the command line.

echo "Script name: $0"
echo "Image file to open: $1"
echo "image size left to right: $2"
echo "Number of arugments: $#"

if [ "$#" -eq 2 ]; then
	echo "running command with arugments: altairview $1 $2 "
        jpgtofabglc $1 A T 0 0 $2 2 0
else
	echo "Usage: $0 <input_image> <image_resize>"
fi

