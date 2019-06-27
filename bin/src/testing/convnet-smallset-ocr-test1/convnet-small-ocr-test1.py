# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:39:58 2019

@author: Matthew Mulhall
"""

TRAIN_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test1\testing-data\train'
VALIDATION_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test1\testing-data\validation'
TEST_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-smallset-ocr-test1\testing-data\test'

import matplotlib.pyplot as plt
from keras import layers
from keras import models 
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

model = models.Sequential()

model.add(layers.Conv2D(32, (3,3), activation='relu',
                        input_shape=(150,150,3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation = 'relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation = 'relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics = ['acc'])

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator= train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(150,150),
        batch_size=20,
        class_mode= 'categorical')
validation_generator =  test_datagen.flow_from_directory(
        VALIDATION_DIR,
        target_size=(150,150),
        batch_size=20,
        class_mode= 'categorical')

history = model.fit_generator(train_generator,
                              steps_per_epoch= 100,
                              epochs=100,
                              validation_data= validation_generator,
                              validation_steps=50)

model.save('convnet-smallset-ocr-test2-model.h5')
