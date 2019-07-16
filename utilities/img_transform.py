# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:55:22 2019

@author: matth
"""
root_dir = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test3\testing-data\original-sets'


from scipy import ndarray
import random
import skimage as sk
from skimage import transform
from skimage import util
import os

sub_folders = [os.path.join(root_dir,folder) for folder in os.listdir(root_dir)]
num_files_desired = 250



def random_rotation(image_array: ndarray):
    rand_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, rand_degree)

def random_noise(image_array: ndarray):
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    return image_array[:, ::-1]


avail_transforms = {
        'rotate' : random_rotation,
        'noise' : random_noise,
        'horizontal_flip' : horizontal_flip
        
        }

for folder in sub_folders:
    images = [os.path.join(folder, pic) for pic in os.listdir(folder)]
    
    generated = 0
    
    while generated <= num_files_desired:
        transformed = None   
        image = random.choice(images)
        
        imgarray = sk.io.imread(image)
        num_transforms = 0
        t = random.randint(1, len(avail_transforms))
        while num_transforms <= t:
            key = random.choice(list(avail_transforms))
            imgarray = avail_transforms[key](imgarray)
            num_transforms+=1
        
        generated+=1
        name =  'augmented_' + str(generated) + '.png'
        newfile= os.path.join(folder, name)
        sk.io.imsave(newfile, imgarray)
    print('Generated ', generated, ' images for ', folder)
    