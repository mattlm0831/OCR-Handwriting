# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:58:12 2019

@author: matth
"""
import pandas as pd
from keras import models
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
import numpy as np
import os
import cv2
################## TESTING #########################

path = r'C:/Users/matth/Documents/GitHub/OCR-Handwriting/bin/src/testing/convnet-smallset-ocr-test3/convnet-smallset-test3-model-TEST1.h5'
test_dir = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test3\testing-data\test'
l = {'a': 0, 'b': 1, 'c': 2, 'd': 3}



def manual_test(model_path, testing_dir, labels):
    classes = os.listdir(testing_dir)
    
    sub_dirs = [os.path.join(testing_dir, x) for x in classes]
    all_files = list()
    predictions = list()
    model = models.load_model(model_path)
    
    labels= dict((v,k) for k,v in labels.items())
    
    for d in sub_dirs:
        files_in_path = os.listdir(d)
        
        for f in files_in_path:
            img_path = os.path.join(d, f)
            img_name = d.split('\\')[-1] + '/' +  f
            image = cv2.imread(img_path)
            all_files.append(img_name)
            image = cv2.resize(image, (150,150))
            image = image.astype("float") / 255.0
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            
            pred = model.predict(image)
            choice = np.argmax(pred)
            pred = labels[choice]
            predictions.append(pred)    
        
    
    

    results = pd.DataFrame({'File' : all_files, 'Prediction' : predictions})
    new_path = path.split('/')
    p = ''
    for i in range(0, len(new_path)-1):
        p+= new_path[i] + '//'
    if 'results.csv' in os.listdir(p):
        results.to_csv(os.path.join(p, 'results_' + str(len(os.listdir(p)) + 1) + '.csv'), index= False)
    else:
        results.to_csv(os.path.join(p, "results.csv"), index = False)
    

def generator_test(model_path, testing_dir, labels):
    test_datagen = ImageDataGenerator(1./255)
    test_generator = test_datagen.flow_from_directory(testing_dir, target_size=(150,150), class_mode='categorical', shuffle = False)
    test_generator.batch_size= test_generator.n
    model = models.load_model(model_path)
    pred = model.predict_generator(test_generator, steps = 1, verbose=1)
    
    predicted_class_indices = np.argmax(pred, axis=1)
    
    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]
    
    filenames = test_generator.filenames
    results = pd.DataFrame({"File" : filenames, "Prediction" : predictions})
    new_path = path.split('/')
    p = ''
    for i in range(0, len(new_path)-1):
        p+= new_path[i] + '//'
    if 'results.csv' in os.listdir(p):
        results.to_csv(os.path.join(p, 'results_' + str(len(os.listdir(p)) + 1) + '.csv'), index= False)
    else:
        results.to_csv(os.path.join(p, "results.csv"), index = False)