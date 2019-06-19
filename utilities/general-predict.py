# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:56:48 2019

@author: Matthew Mulhall
"""
import sys
import cv2
import os
from keras import models
from keras.preprocessing.image import img_to_array
import numpy as np
import imutils

model_path1= r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test1\convnet-smallset-ocr-test1-model.h5'
model_path2= r'C:/Users/mlm14013work/Desktop/OCR-Handwriting/bin/src/testing/convnet-smallset-ocr-test2/convnet-smallset-ocr-test2-model.h5'
model_path3 = r''
prediction_path_1 = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test1\predictions'
prediciton_path_2 = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test2\predictions'
prediction_path_3 = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test1\predictions'

model_1 = None
model_2 = None
model_3 = None

letterarray = [i for i in ('a','b','c','d')]
medset_labels  = ['0', '1', '2', '3', '4',
        'a-lower', 'b-lower', 'c-lower',
        'd-lower', 'e-lower', 'f-lower',
        'g-lower',
        'A-upper', 'B-upper', 'C-upper',
        'D-upper', 'E-upper', 'F-upper',
        'G-upper']


def predict_test1(img_path):
    
    image = cv2.imread(img_path)
    orig= image.copy()
    
    image = cv2.resize(image, (150,150))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    
    model = models.load_model(model_path1)
        
    (a, b, c, d) = model.predict(image)[0]
    probs = [a,b,c,d]
    m = max(probs)
    letter = probs.index(m)
    
    label = letterarray[letter] 
        
    text = "{}: {:.3f}%".format(label, m*100)
    output = imutils.resize(orig, width = 400)
    cv2.putText(output, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2)
    cv2.imshow("Output", output)
    cv2.waitKey(0)    
    l = len(os.listdir(prediction_path_1))
    name = "This_is_" + str(label) + str(l+1) + ".png"
    cv2.imwrite(os.path.join(prediction_path_1, name), output)
    print("Prediction created:" + name)
    
def predict_test2(img_path):
    
    image = cv2.imread(img_path)
    orig= image.copy()
    
    image = cv2.resize(image, (150,150))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    model = models.load_model(model_path2)
   
        
    (a, b, c, d) = model.predict(image)[0]
    probs = [a,b,c,d]
    m = max(probs)
    letter = probs.index(m)
    
    label = letterarray[letter] 
        
    text = "{}: {:.3f}%".format(label, m*100)
    output = imutils.resize(orig, width = 400)
    cv2.putText(output, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2)
    cv2.imshow("Output", output)
    cv2.waitKey(0) 
    l = len(os.listdir(prediciton_path_2))
    name = "This_is_" + str(label) + str(l+1) + ".png"
    cv2.imwrite(os.path.join(prediciton_path_2, name), output)
    print("Prediction created:" + name)

def predict_test3(img_path):
    
    image = cv2.imread(img_path)
    orig= image.copy()
    
    image = cv2.resize(image, (150,150))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    

    model = models.load_model(model_path3)

        
    probs = model.predict(image)[0]
    m = max(probs)
    letter = probs.index(m)
    
    label = medset_labels[letter] 
        
    text = "{}: {:.3f}%".format(label, m*100)
    output = imutils.resize(orig, width = 400)
    cv2.putText(output, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2)
    cv2.imshow("Output", output)
    cv2.waitKey(0) 
    l = len(os.listdir(prediction_path_3))
    name = 'This_is_' + str(label) + str(l+1) + '.png'
    cv2.imwrite(os.path.join(prediction_path_3, name), output)   
    print("Prediction created:" + name) 
    
    
if __name__ == "__main__": 
    args = sys.argv
    if len(args) >= 2:
        if args[1] == '1':
            predict_test1(args[2])
        elif args[1] == '2':
            predict_test2(args[2])
        else:
            predict_test3(args[2])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    