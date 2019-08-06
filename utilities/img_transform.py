# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:55:22 2019

@author: matth
"""

from scipy import ndarray
from scipy import ndimage
import random
import skimage as sk
from skimage import transform
from skimage import util
import os

def random_rotation(image_array: ndarray):
    rand_degree = random.uniform(-25, 25)
    return transform.rotate(image_array, rand_degree)

def random_noise(image_array: ndarray):
    return util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    return image_array[:, ::-1]

def scale_out(image_array: ndarray):
    factor = random.uniform(1, 2)
    return transform.rescale(image_array, scale=factor, mode='constant')

def scale_in(image_array: ndarray):
    factor = random.uniform(0,1)
    return transform.rescale(image_array, scale=factor, mode='constant')

def blur(image_array: ndarray):
    return ndimage.uniform_filter(image_array, size=(11,11,1))


avail_transforms = {
        'rotate' : random_rotation,
        'noise' : random_noise,
        'horizontal-flip' : horizontal_flip,
        'scale-in' : scale_in,
        'scale-out' : scale_out,
        'blur' : blur
        }
def transform_many(folder, num_files_desired = 300):
    sub_folders = [os.path.join(folder, f) for f in os.listdir(folder)]
    for folder in sub_folders:
        images = [os.path.join(folder, pic) for pic in os.listdir(folder)]
        
        generated = 0
        
        while generated <= num_files_desired:
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
        