#!/bin/bash


# PROGRAM   : run_prediction.py
# POURPOSE  : Convert images to matrix, make a prediction and convert matrix to images.
# AUTHOR    : Francisco Sáez R.
# EMAIL     : francisco.saez@sansano.usm.cl
# V1.0      : 22/10/2021

# This code allow to transform images from png or jpg file to matrix to
# make a prediction with Duck Model proposed for Sáez et al. (2021)


#-----------------------------------------------------------------
# 
# DELETE TXT FILE AND RUN MODEL
#
#-----------------------------------------------------------------
# DELETE TXT FILE
name_img=./name_img.txt
if [ -f "$name_img" ]; then
    rm ./name_img.txt
fi

# NETWORK
python3 run_prediction.py --height 512 --width 512 --beach_path /beach_name/ --inputdata_path /frames/ --output_path /prediction_img/		
echo



