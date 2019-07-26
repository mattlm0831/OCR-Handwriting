# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:09:23 2019

@author: Matthew Mulhall
"""
from img_transform import transform_many
import os, shutil
import random
#This file was used to manipulate the images into the proper directories without having to do it manually for the larger dataset test.



def compile_data(original_data, root_dir=None, num_files = 300):
    
    if not root_dir:
        root_dir = os.path.dirname(original_data)
        
    create_dirs(root_dir, original_data)
    transform_many(original_data, num_files)
    place_images(root_dir, original_data)
        



def create_dirs(ROOT_DIR, original_data_dir):
    
    dirs = os.listdir(original_data_dir)
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
            
    

        
def place_images(ROOT_DIR, original_data_dir):
    
    dirs = os.listdir(original_data_dir)
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
            
           
        for i in range(train_limit, validate_limit):
            dest_dir = os.path.join(validate_dir, dname)
            fname = random.choice(all_pictures)
            all_pictures.remove(fname)
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
        
        
        for i in range(0, len(all_pictures)):
            dest_dir = os.path.join(test_dir, dname)
            fname = random.choice(all_pictures)
            all_pictures.remove(fname)
            src = os.path.join(new_dir, fname)
            dest = os.path.join(dest_dir, fname)
            shutil.copyfile(src, dest)
            
        
        
    print("Moving ", total, ' images to their respective test locations.')
            
            
            
            