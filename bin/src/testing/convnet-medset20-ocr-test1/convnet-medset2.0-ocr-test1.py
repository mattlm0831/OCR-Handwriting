# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:42:27 2019

@author: Matthew Mulhall
"""
TRAIN_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset2.0-ocr-test1\testing-data\train'
VALIDATION_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset2.0-ocr-test1\testing-data\validation'
TEST_DIR = r'C:\Users\matth\Documents\GitHub\OCR-Handwriting\bin\src\testing\convnet-medset2.0-ocr-test1\testing-data\test'

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
model.add(layers.Dropout(rate = .25))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation = 'relu'))
model.add(layers.Dropout(rate = .25))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (3, 3), activation = 'relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(22, activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics = ['acc'])

train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale=1./255)


train_generator= train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(150,150),
        batch_size=32,
        class_mode= 'categorical')

validation_generator =  test_datagen.flow_from_directory(
        VALIDATION_DIR,
        target_size=(150,150),
        batch_size=32,
        class_mode= 'categorical')



history = model.fit_generator(train_generator,
                              steps_per_epoch= 100,
                              epochs=300,
                              validation_data= validation_generator,
                              validation_steps=50)

model.save('convnet-medset-ocr-test2-model-lenet.h5')
np.save("history-lenet.npy", history)
