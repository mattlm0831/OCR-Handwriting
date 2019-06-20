# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:29:19 2019

@author: mlm14013work
"""

import os

path = r'C:\Users\mlm14013work\Desktop\New folder'

num = 0
for d in os.listdir(path):
    
    genName = 'rand_' + str(num) + '.png'
    os.rename(os.path.join(path, d), os.path.join(path, genName))
    num +=1