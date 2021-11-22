"""
PROGRAM   : run_prediction.py
POURPOSE  : Convert images to matrix, make a prediction and convert matrix to images.
AUTHOR    : Francisco Sáez R.
EMAIL     : francisco.saez@sansano.usm.cl
V1.0      : 22/10/2021

This code allow to transform images from png or jpg file to matrix to
make a prediction with Duck Model proposed for Sáez et al. (2021)
"""

#-----------------------------------------------------------------
# 
# PACKAGES
#
#-----------------------------------------------------------------
import cv2
import os
import numpy as np
import argparse
import main
import tensorflow as tf
import shutil

#-----------------------------------------------------------------
# 
# INPUTS
#
#-----------------------------------------------------------------
def parse_args():
	parser = argparse.ArgumentParser(description='Path and image size')
	parser.add_argument('--height', type=int, default=512, help='pixels')
	parser.add_argument('--width', type=int, default=512, help='pixels')
	parser.add_argument('--beach_path', type=str, help='beach folder')
	parser.add_argument('--main_path', type=str, default=os.getcwd(),
	                        help='Duck model main path')
	parser.add_argument('--inputdata_path', type=str, default='./frames/',
	                        help='Input path for images')
	parser.add_argument('--output_path', type=str, default='./prediction_img',
	                        help='Output path for mask')
	args = parser.parse_args()
	return args


#-----------------------------------------------------------------
# 
# RUN MODEL
#
#-----------------------------------------------------------------	
if __name__ == '__main__':

	args = parse_args()

	try:
	    shutil.rmtree('.'+args.beach_path+args.output_path)
	except OSError as e:
	    print("Error: %s - %s." % (e.filename, e.strerror))

	try:
	    shutil.rmtree('.'+args.beach_path+'/rescaling_img/')
	except OSError as e:
	    print("Error: %s - %s." % (e.filename, e.strerror))

	os.system('mkdir -m 771 .'+args.beach_path+'/rescaling_img/')
	os.system('mkdir -m 771 .'+args.beach_path+args.output_path)

	# LLAMO A TODAS LAS FUNCIONES 
	functions = main.Duck_model(args)

	# Rescaling images
	functions.rescaling_img()

	# RUN MODEL
	functions.run_model()