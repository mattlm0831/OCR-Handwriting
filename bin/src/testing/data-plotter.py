# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:56:27 2019

@author: Matthew Mulhall
"""

import numpy as np
import matplotlib.pyplot as plt
import os

HIST_FILE = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-medset-ocr-test1'
new_hist = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test2'

def plot(file = HIST_FILE):
     history = np.load(os.path.join(file, 'history.npy'))
     history = history[()]
    
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
     