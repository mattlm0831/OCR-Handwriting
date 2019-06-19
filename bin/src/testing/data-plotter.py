# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:56:27 2019

@author: Matthew Mulhall
"""

import numpy as np
import matplotlib.pyplot as plt


HIST_FILE = r'C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test2\history.npy'

def plot(file = HIST_FILE)
  
  history = np.load(file)
  history = history[()]

  acc = history.history['acc']
  val_acc= history.history['val_acc']
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs = range(1, len(acc) + 1)

  plt.plot(epochs, acc, 'bo', label='Training Accuracy')
  plt.plot(epochs, val_acc, 'b', label='Validation Accuracy')
  plt.title('Training and Validation Accuracy')
  plt.legend()
  plt.figure()
