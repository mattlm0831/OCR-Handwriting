# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:08:02 2019

@author: matth
"""

import os

root = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset2.0-ocr-test1\testing-data\original-data'
def util():
    for fname in os.listdir(r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset2.0-ocr-test1\testing-data\original-data'):
        print(fname)
        if fname == '0' or fname == '1':
           continue
        else:
           os.rename(os.path.join(root, fname), os.path.join(root, fname+'_lower'))
          
            
def upperutil():
    for fname in os.listdir(root):
        if fname.islower() or fname == '0' or fname == '1':
            continue
        else:
            os.rename(os.path.join(root, fname), os.path.join(root, fname+'_upper') )
           
           