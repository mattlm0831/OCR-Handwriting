# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:58:12 2019

@author: matth
"""
import pandas as pd
from keras import models as m
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
import numpy as np
import os
import cv2
################## TESTING #########################

path = r'C:/Users/matth/Documents/GitHub/OCR-Handwriting/bin/src/testing/convnet-medset-ocr-test7/convnet-medset-test7.h5'
test_dir = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test7\testing-data\test'
l = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
lmed = {'0': 0, '1': 1, '2': 2, '3': 3,'4': 4,'A-upper': 5,'B-upper': 6,'C-upper': 7,'D-upper': 8,'E-upper': 9,'F-upper': 10,'G-upper': 11,'a-lower': 12,'b-lower': 13,'c-lower': 14,'d-lower': 15,'e-lower': 16,'f-lower': 17,'g-lower': 18}
label_list = [l, lmed]

def choose_test(file):
    
    folders= os.listdir(file)
    folders = [i for i in folders if os.path.isdir(os.path.join(file,i))]
    print("Tests:")
    for i in range(0, len(folders)):
        print("[",i,"]", folders[i].split("//")[-1])
    print("Please choose a number from this list and hit enter")
    ind = int(input())
    assert(ind <= len(folders))
    return os.path.join(file, folders[ind])

def choose_model(file):
    
    models = list()
    files = os.listdir(file)
    files = [i for i in files if i.endswith('.h5')]
    model_path = ''      
    if not files:
        print("No models")
        return None
    
    if len(models) == 1:
        model_path = files[0]
    else:
        print("Choose a model from the list:")
        for i in range(0, len(files)):
            print("[",i,"]", files[i].split("//")[-1])
        
        index = input()
        assert(int(index) <= len(files))
        model_path= os.path.join(file, files[int(index)])
        
    return model_path

def choose_label():
    
    for i in range(0, len(label_list)):
        print("[",i,"]", label_list[i])
    index = int(input())
    assert(index <= len(label_list))
    return label_list[index]

def choose_data(file):
    
    files = os.listdir(file)
    files = [i for i in files if os.path.isdir(os.path.join(file, i))]
    
    fname = ''
    
    if not files:
        print("Make sure your data folders have test or data in the name")
    if len(files) == 1:
        fname = files[0]
    else:
        for i in range(0, len(files)):
            print("[",i,"]", files[i])
        index = int(input())
        assert(index <= len(files))
        fname = files[index]
        
    return os.path.join(os.path.join(file, fname), 'test')
        
def test():
    root = r'C:/Users/matth/Documents/GitHub/OCR-Handwriting/bin/src/testing'
    test_folder = choose_test(root)
    model = choose_model(test_folder)
    data = choose_data(test_folder)
    labels = choose_label()
    manual_test(model, data, labels, test_folder)
    
def manual_test(model, testing_dir, labels, root):
    
    model = m.load_model(model)
    classes = os.listdir(testing_dir)
    
    sub_dirs = [os.path.join(testing_dir, x) for x in classes]
    all_files = list()
    predictions = list()
    
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
    os.chdir(root)
    p = root
    if 'results.csv' in os.listdir(p):
        name = 'results_' + str(len(os.listdir(p)) + 1) + '.csv'
        results.to_csv(os.path.join(p, name), index= False)
        
    else:
        name =  "results.csv"
        results.to_csv(os.path.join(p, name), index = False)
    
    print("[" + name + '] created')
    return

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
        
if __name__ == "__main__":
    test()   