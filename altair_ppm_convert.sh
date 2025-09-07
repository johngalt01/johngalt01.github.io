#!/bin/bash
# script to automatically convert jpg/gif/etc into a PPM format for viewing on the Altair with PPMVIEW2

echo "Script name: $0"
echo "Input Image name: $1"
echo "Output Image PPM (ext) format: $2"
echo "Image Size Left to Right rescale: $3"
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



