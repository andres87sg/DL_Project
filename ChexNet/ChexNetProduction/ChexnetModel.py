
from os import path
import numpy as np
import matplotlib.pyplot as plt

import cv2 as cv
import os
import pydicom as dicom

from AbstractProducts import load_mdl_chexnet
from ChexnetUtils import gradcam
from GenerateReport import GenerateReportClass 

from ChexnetConstantManager import ImgSize, MaxIntensityValue,ImagenetMean,ImagenetStd



# ImgSize = (224,224)
# MaxIntensityValue = 255
# ImagenetMean = np.array([0.485, 0.456, 0.406])
# ImagenetStd = np.array([0.229, 0.224, 0.225])


#%%
class ChexnetModel():
    """This class is used to predict 14 different patologies in chest X-ray images"""

    def __init__(self,mdl):
        
        self.mdl=mdl
            
    def run_preprocessing(self,ImgIn):
        
        """ Input image normalized by ImageNet meand and std """
    
        ImgIn = cv.resize(ImgIn,ImgSize)    
        ImgIn = np.asarray(ImgIn/MaxIntensityValue)
        ImgMean = ImagenetMean
        ImgStd = ImagenetStd
        
        # Imagenet standarization -> z = (x-mean)/std
        ImgOut = (ImgIn - ImgMean ) / ImgStd

        return ImgOut


    def run_prediction(self,img):
        
        """
        Input: X-Ray thorax image 
        Output: Prediction of thoracic pathologies (1D vector)
        """
        
        # Preprocessin image (Standarization)
        PreprocessedImg = self.run_preprocessing(img)
        
        # Expanding image dimensions to feed classification model
        PreprocessedImgExpand = np.expand_dims(PreprocessedImg,axis=0)
        
        # Model prediction
        prediction = self.mdl.predict(PreprocessedImgExpand)
        
        # Dimention reduction (So as to obtain a 1-D vector)
        PredictionProbabilities = np.squeeze(prediction,axis=0) 
        
        # Heatmap building using gradcam function
        ImgHeatmap=gradcam(self.mdl,PreprocessedImg,PreprocessedImgExpand)

        return PredictionProbabilities

    def run_evaluation(self):
        pass

    def run_training(self):
        pass

#%% Prueba

mdl=ChexnetModel(load_mdl_chexnet())

#%%
imgdir = "C:/Users/Andres/Desktop/images/"

numfile = 2
listimgfile = os.listdir(imgdir)
imgfile = os.path.join(imgdir,listimgfile[numfile])

img = cv.imread(imgfile)

# plt.imshow(img,cmap='gray')
# plt.axis('off')
# plt.title(listimgfile[numfile])

prediction = mdl.run_prediction(img)

#%%

# Metadata
patient_name = "Andres"
ID = '12345'
genre = 'F'
date = '02/02/21'
study_name = 'CHEST CT'
study_date = '01/01/01'
region = 'LATAM' # or US
report='This report was automaticaly generated by theStella services. At least one patology pattern was indentified in this study. The heatmap overlead on the image represeted the area with the AI considered to do the automatic evaluation.'
report = report +report

report=GenerateReportClass(patient_name, ID, genre,date,study_name,study_date,report,prediction,region)
report.generate_pdf()

print("el reporte ha sido generado con exito")
#zz.generate_pdf()

