# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:14:41 2019

@author: mlm14013work
"""
import os 

def rename():

#Set old dir to the path up until your char folder . Something like: "C:\Users\yourname\Documents\OCR-Handwriting\bin\data\char"
    oldDir = r"C:\Users\mlm14013work\Desktop\OCR-Handwriting\bin\data\char"
    os.chdir(oldDir)
    overallCount = 0;
    #Sets up the walk starting at the char folder.
    
    for dir, subdirs, files in os.walk(oldDir):
        #Walks all subdirectories, and sets the "count" to 0, this is for naming purposes
        count = 0;
        for f in files:
        
            #if it is a readme we don't want to rename, also if it is a directory we don't want to rename it.
            if(f == "readme.txt" or os.path.isdir(f)):
                continue
            #fetches the parent directory name, this is useful in order to have our standardized naming
            
            d = os.path.basename(dir)
            
            fnew = d + "_" + (str(0) * (3-len(str(count)))) + str(count) + ".png";
            
            #creates the new name, calculates the required number, if we did up to 4 numbers we would need to do 4-len(str(count)) etc
            
            if(f == fnew):
                #if our file is named what we calculate its name to be, theres no use in renaming it, this saves us a lot of time.
                count += 1
                continue
            
            #changes us to the directory we are currently walking
            
            os.chdir(dir)
            
            #Does the renaming:
            
            os.rename(os.path.join(os.getcwd(),f), os.path.join(os.getcwd(), fnew))
            
            #gives a confirmation it worked.
            
            print("Renamed to: " + fnew + "\n")
            overallCount+= 1;
            #increments count.
            
            count += 1
            
    print("\nRenamed a total of " + str(overallCount) + " photos\n")