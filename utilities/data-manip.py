# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:09:23 2019

@author: Matthew Mulhall
"""

import os, shutil
import random
ROOT_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test3\testing-data'
original_data_dir = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test3\testing-data\original-sets'
dirs = os.listdir(original_data_dir)


#This file was used to manipulate the images into the proper directories without having to do it manually for the larger dataset test.


def create_dirs():
    
    train_dir= os.path.join(ROOT_DIR, 'train')
    test_dir = os.path.join(ROOT_DIR, 'test')
    validate_dir = os.path.join(ROOT_DIR, 'validation')
    
    if not os.path.isdir(train_dir):
        os.mkdir(train_dir)
    if not os.path.isdir(test_dir):    
        os.mkdir(test_dir)
    if not os.path.isdir(validate_dir):
        os.mkdir(validate_dir)
    
    for fname in dirs:
        p = os.path.join(test_dir, fname)
        if not os.path.isdir(p):
            os.mkdir(p)
    
    for fname in dirs:
        p = os.path.join(train_dir, fname)
        if not os.path.isdir(p):
            os.mkdir(p)
        
    for fname in dirs:
        p = os.path.join(validate_dir, fname)
        if not os.path.isdir(p):
            os.mkdir(p)
            
    

        
def place_images():
    
    train_dir= os.path.join(ROOT_DIR, 'train')
    test_dir = os.path.join(ROOT_DIR, 'test')
    validate_dir = os.path.join(ROOT_DIR, 'validation')

    total = 0
    for dname in dirs:
        new_dir = os.path.join(original_data_dir, dname)
        dest_dir = ''
        all_pictures = os.listdir(new_dir)
        total+= len(all_pictures)
        train_limit = int(len(all_pictures) * .70)
        validate_limit = int(len(all_pictures) * .20) + train_limit
        test_limit = int(len(all_pictures) * .10) + validate_limit
        
        for i in range(0, train_limit):
            dest_dir = os.path.join(train_dir, dname)          
            fname = random.choice(all_pictures)
            all_pictures.remove(fname)
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
            
        print(len(all_pictures))    
        for i in range(train_limit, validate_limit):
            dest_dir = os.path.join(validate_dir, dname)
            fname = random.choice(all_pictures)
            all_pictures.remove(fname)
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
        print(len(all_pictures))
        
        for i in range(0, len(all_pictures)):
            dest_dir = os.path.join(test_dir, dname)
            fname = random.choice(all_pictures)
            all_pictures.remove(fname)
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
            
        print(len(all_pictures))
        
    print("Moving ", total, ' images to their respective test locations.')
            
            
            
            