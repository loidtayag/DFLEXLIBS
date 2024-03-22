# Duplicates images from repository into the "mySite/static" 
# while keeping the directory structure for deployment

import os
import shutil

def getImages(srcDir, desDir):
    for item in os.listdir(srcDir):
        filePath = os.path.join(srcDir, item)
        desPath = os.path.join(desDir, item)

        if item.lower().endswith('.png'): 
            if not os.path.exists(desDir):
                os.makedirs(desDir) 
            shutil.copy2(filePath, desDir)
        elif os.path.isdir(filePath):  
            getImages(filePath, desPath)

getImages('mySite\DFLEXLIBS', 'mySite/static/')
