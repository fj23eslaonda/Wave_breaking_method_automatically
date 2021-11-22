# Wave breaking patterns identification method automatically
This code allow to transform images from png or jpg file to matrix to make a prediction with Duck Model proposed for Sáez et al. (2021)

# Installation


### Install Virtual Environment 
```
sudo apt install python3-venv
```
### Create Virtual Environment 
```
python3 -m venv my-project-env
```
### Activate environment and install packages
```
source my-project-env/bin/activate
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
