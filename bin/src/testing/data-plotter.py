# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:56:27 2019

@author: Matthew Mulhall
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from keras import models
from keras.utils import plot_model
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot


HIST_FILE = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test1'
new_hist = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test2'
medset_2 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test2'
medset_3 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test3'
medset_4 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test4'



mdl_path1 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test1\convnet-smallset-ocr-test1-model.h5'
mdl_path2 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test2\convnet-smallset-ocr-test2-model.h5'
mdl_path4 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test2\convnet-medset-ocr-test2-model.h5'
mdl_path5 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test3\convnet-medset-ocr-test31-model.h5'
mdl_path6 = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test4\convnet-medset-ocr-test4-model.h5'


def plot(file = None, obj = None):
    
     if not obj and not file:
         return "Cannot operate on nothing"
     
     if not obj:
         history = np.load(os.path.join(file, 'history.npy'))
         history = history[()]
     if not file:
         history = obj
     acc = history.history['acc']
     val_acc= history.history['val_acc']
     loss = history.history['loss']
     val_loss = history.history['val_loss']

     epochs = range(1, len(acc) + 1)

     plt.plot(epochs, acc, 'bo', label='Training Accuracy', color = '#991A00', linewidth = .5)
     plt.plot(epochs, val_acc, 'b', label='Validation Accuracy', color = '#991A00', linewidth = 2)
     plt.title('Training and Validation Accuracy')
     plt.legend()
     
     plt.savefig(os.path.join(file, 'train-vs-val-acc.png'))
     plt.figure()
     
    
    
    
     plt.plot(epochs, loss, 'bo', label = 'Training loss', color = '#991A00', linewidth = .5)
     plt.plot(epochs, val_loss, 'b', label = 'Validation Loss', color = '#991A00', linewidth = 2)
     plt.title('Training and Validation Loss')
     plt.legend()
     
     plt.savefig(os.path.join(file, 'train-vs-val-loss.png'))
     plt.figure()
     

def model_to_img(model_path):

     model = models.load_model(model_path)
     file_path = os.path.dirname(os.path.abspath(model_path))
     file_path = os.path.join(file_path, 'model.png')
     plot_model(model, to_file = file_path, show_shapes = True, show_layer_names=True)
     return str("Saved to " + file_path)

def mdl_dot(model):
     SVG(model_to_dot(model).create(prog='dot', format = 'svg'))
