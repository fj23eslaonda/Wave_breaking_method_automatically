# Wave breaking patterns identification method automatically
This code allow to transform images from png or jpg file to matrix to make a prediction with Duck Model proposed for Sáez et al. (2021)

Link Paper: [Wave-by-wave Nearshore Wave Breaking Identificationusing U-Net](https://www.sciencedirect.com/science/article/pii/S037838392100168X)
Link Repository: [Wave-by-wave_identification](https://github.com/fj23eslaonda/Wave_by_Wave_Identification)

# Installation
To use the Duck model it is necessary to install specific packages. Therefore, it is recommended to create a virtual environment to install the packages.

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

# Use Duck model to make predictions

```
cd REPO_ROOT_DIR
sh prediction_model.sh
```
