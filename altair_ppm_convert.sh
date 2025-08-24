#!/bin/bash
echo "Script name: $0"
echo "First Argument: $1"
echo "Second Argument: $2"
echo "third Argument: $3"
echo "All Arugmenets: $@"
echo "Number of arugments: $#"

if [ "$#" -eq 3 ]; then
        echo "running command with arugments: altair_ppm.sh $1 $2 $3"
        convert "$1" -resize "$3" temp.jpg
        convert temp.jpg -compress none temp.ppm
        normal_ppm temp.ppm "$2"
else
        echo "Usage: $0 <input_image> <output.ppm> <image_resize>"
fi


