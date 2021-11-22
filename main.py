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
from tensorflow.keras.models import Model, load_model, model_from_json

class Duck_model():

    #-----------------------------------------------------------------
    # 
    # PARAMETERS
    #
    #-----------------------------------------------------------------
    def __init__(self, args):
        self.height       = args.height
        self.width        = args.width
        self.main_path    = args.main_path
        self.input_path   = args.inputdata_path
        self.output_path  = args.output_path
        self.beach_path   = args.beach_path
        self.dir_rescal   = '/rescaling_img'
        self.list_img     = self.load_list_img()

    #-----------------------------------------------------------------
    # 
    # LOAD IMAGE NAMES LIST
    #
    #-----------------------------------------------------------------
    def load_list_img(self):
        os.chdir(self.main_path + self.beach_path + self.input_path)
        os.system('ls >> ' + self.main_path + '/name_img.txt')
        os.chdir(self.main_path)

        list_img = open(self.main_path+'/name_img.txt','r') 
        list_img = list(list_img.read().split('\n'))
        return list_img[:-1]

    #-----------------------------------------------------------------
    # 
    # RESCALING IMAGES
    #
    #-----------------------------------------------------------------
    def rescaling_img(self):

        # NAME IMG
        list_img = self.list_img

        # INPUTS
        width     = self.width
        height    = self.height
        number    = 1

        print('\nLoading images!')

        # LOOP TO CHANGE SIZE OF IMAGE
        for img in list_img:
            image_o = cv2.imread(self.main_path + self.beach_path + self.input_path + img,0)
            image_f = image_o# IF YOU WANNA SELECT PART OF IMAGE [-512-150:-150, -512-150:-150]
            cv2.imwrite(self.main_path +  self.beach_path + self.dir_rescal+'/'+img,image_f)
            number+=1

        print('Images are ready!')
    
    #-----------------------------------------------------------------
    # 
    # LOAD DUCK MODEL
    #
    #-----------------------------------------------------------------
    def load_model(self):
        import tensorflow as tf
        # Load JSON and Create model
        json_file          =  open(self.main_path+'/model/model_final.json', 'r')
        loaded_model_json  =  json_file.read()
        json_file.close()
        model              = model_from_json(loaded_model_json, {"tf":tf})

        # Load weight
        model.load_weights(self.main_path+"/model/best_model_final.h5")
        print("Model Loaded")
        return model

    #-----------------------------------------------------------------
    # 
    # CREATE MATRIX FOR TEST SET
    #
    #-----------------------------------------------------------------
    def image_to_matrix(self,name_img):

        # Create matrix
        x_tst = np.zeros((1, self.height, self.width, 1), dtype=np.float32)

        x_img = cv2.imread(self.main_path+self.beach_path + self.dir_rescal + '/' + name_img, 0)
        x_img = cv2.rotate(x_img, cv2.ROTATE_90_CLOCKWISE)
        
        x_img = x_img[..., np.newaxis]
        # Save images
        x_tst[0] = x_img / 255.0
        return x_tst


    #-----------------------------------------------------------------
    # 
    # TRANSFORM MATRIX INTO IMAGES
    #
    #-----------------------------------------------------------------
    def matrix_to_images(self,y_pred, name_img):
        #y_pred1 = y_pred_part
        y_pred2 = np.squeeze(y_pred[0]>0.5)
        #y_final = (y_pred1+y_pred2)>1
        cv2.imwrite(self.main_path + self.beach_path + self.output_path + name_img, np.squeeze(y_pred2)*255)

        return print('Predictions are ready!')


    #-----------------------------------------------------------------
    # 
    # IF YOU HAVE LARGER IMAGES THAN 512x512 PIXELS
    #
    #-----------------------------------------------------------------
    #def upsize_image(x_tst,im_height=512, im_width=512):
    #    img   = cv2.resize(np.squeeze(x_tst[0]),(1024,1024), interpolation=cv2.INTER_AREA)
    #    imgs  = [img[:512,:512],img[:512,512:],img[512:,:512],img[512:,512:]]

    #    x_tst = np.zeros((len(imgs), im_height, im_width, 1), dtype=np.float32)
    #    for i in range(len(imgs)):
    #        x_tst[i] = imgs[i][..., np.newaxis]
    #    return x_tst


    #def downsize_image(y_pred_part):
    #    img1   = np.concatenate((np.squeeze(y_pred_part[0]), np.squeeze(y_pred_part[1])), axis=1)
    #    img2   = np.concatenate((np.squeeze(y_pred_part[2]), np.squeeze(y_pred_part[3])), axis=1)
    #    img    = np.concatenate((img1, img2), axis=0)
    #    y_pred = cv2.resize(img.astype('float32'),(512,512),  interpolation=cv2.INTER_AREA)
    #    return y_pred



    #-----------------------------------------------------------------
    # 
    # RUN MODEL
    #
    #-----------------------------------------------------------------
    def run_model(self):

        # NAME IMG
        list_img = self.list_img

        for name_img in list_img:
            x_tst       = self.image_to_matrix(name_img)
            model       = self.load_model()
            y_pred      = model.predict(x_tst,
                                verbose = True)

            #x_tst_part  = upsize_image(x_tst,
            #                          im_height=512,
            #                          im_width=512)

            #y_pred_part = model.predict(x_tst_part,
            #                            verbose = True)

            #y_pred_part = downsize_image(y_pred_part)

            self.matrix_to_images(y_pred,
                             #y_pred_part,
                            name_img)

