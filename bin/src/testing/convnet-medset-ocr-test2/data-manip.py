# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:09:23 2019

@author: Matthew Mulhall
"""

import os, shutil

ROOT_DIR = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test1\testing-data'
original_data_dir = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test1\testing-data\original-data'

dirs = ['0', '1', '2', '3', '4',
        'a-lower', 'b-lower', 'c-lower',
        'd-lower', 'e-lower', 'f-lower',
        'g-lower',
        'A-upper', 'B-upper', 'C-upper',
        'D-upper', 'E-upper', 'F-upper',
        'G-upper']


#This file was used to manipulate the images into the proper directories without having to do it manually for the larger dataset test.


def create_dirs():
    
    train_dir= os.path.join(ROOT_DIR, 'train')
    test_dir = os.path.join(ROOT_DIR, 'test')
    validate_dir = os.path.join(ROOT_DIR, 'validation')
    
    for fname in dirs:
        p = os.path.join(test_dir, fname)
        if not os.path.isdir(p):
            os.mkdir(os.path.join(test_dir, fname))
    
    for fname in dirs:
        p = os.path.join(train_dir, fname)
        if not os.path.isdir(p):
            os.mkdir(os.path.join(train_dir, fname))
        
    for fname in dirs:
        p = os.path.join(validate_dir, fname)
        if not os.path.isdir(p):
            os.mkdir(os.path.join(validate_dir, fname))
            
    

        
def place_images():
    
    train_dir= os.path.join(ROOT_DIR, 'train')
    test_dir = os.path.join(ROOT_DIR, 'test')
    validate_dir = os.path.join(ROOT_DIR, 'validation')
    
    for dname in dirs:
        new_dir = os.path.join(original_data_dir, dname)
        dest_dir = ''
        all_pictures = os.listdir(new_dir)
        train_limit = int(len(all_pictures) * .50)
        validate_limit = int(len(all_pictures) * .25) + train_limit
        test_limit = int(len(all_pictures) * .25) + validate_limit
        
        for picture in range(0, train_limit):
            dest_dir = os.path.join(train_dir, dname)          
            fname = all_pictures[picture]
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
            
        for picture in range(train_limit, validate_limit):
            dest_dir = os.path.join(validate_dir, dname)
            fname = all_pictures[picture]
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
            
        for picture in range(validate_limit, test_limit):
            dest_dir = os.path.join(test_dir, dname)
            fname = all_pictures[picture]
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
            
            
            
            
            
            