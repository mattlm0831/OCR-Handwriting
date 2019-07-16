# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:58:12 2019

@author: matth
"""
import pandas as pd
from keras import models
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import imutils
################## TESTING #########################

path = r'C:/Users/matth/Documents/GitHub/OCR-Handwriting/bin/src/testing/convnet-smallset-ocr-test3/convnet-smallset-test3-model-TEST.h5'
test_dir = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test3\testing-data\test'
l = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    
    
    


def test(model_path, testing_dir, labels):
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
    results.to_csv(os.path.join(p, "results.csv"), index = False)