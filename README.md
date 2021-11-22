# Wave breaking patterns identification method automatically
This code allow to transform images from png or jpg file to matrix to make a prediction with Duck Model proposed for Sáez et al. (2021)

## Installation
This software has only been tested on ubuntu 16.04(x64), python3.5, cuda-9.0, cudnn-7.0 with 
a GTX-1070 GPU. To install this software you need tensorflow 1.12.0 and other version of 
tensorflow has not been tested but I think it will be able to work properly in 
tensorflow above version 1.10. Other required package you may install them by

```
pip3 install -r requirements.txt
```

## Test model
In this repo I uploaded a model trained on dataset provided by the origin author 
[origin_dataset](https://drive.google.com/open?id=1e7R76s6vwUJxILOcAsthgDLPSnOrQ49K).

The trained derain net model weights files are stored in folder model/

You can test a single image on the trained model as follows

```
cd REPO_ROOT_DIR
python tools/test_model.py --weights_path model/derain_gan/derain_gan.ckpt-100000
--image_path data/test_data/test_1.png
```
