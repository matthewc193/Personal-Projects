import os
import shutil
mcroc_downloads = "c:/Users/mcroc/Downloads"


math_folder = 'c:/Users/mcroc/Downloads/MATH'
data_folder = 'c:/Users/mcroc/Downloads/DATA101'
cosc_folder = 'c:/Users/mcroc/Downloads/COSC'
scie_folder = 'c:/Users/mcroc/Downloads/SCIE101'

test = os.scandir(data_folder)
files = os.scandir(mcroc_downloads)


for file in files:
    print(file)
    if 'data' in file.name.lower() or 'aswk' in file.name.lower() or 'markdown' in file.name.lower():
        if file.name != "DATA101":
            shutil.move(file, data_folder)

    if 'math' in file.name.lower():
        if file.name != 'MATH':
            shutil.move(file, math_folder)      

    if 'cosc' in file.name.lower() or 'object_file' in file.name.lower():
        if file.name != 'COSC':
            shutil.move(file, cosc_folder)

    if 'sci' in file.name.lower():
        if file.name != 'SCIE101':
            shutil.move(file, scie_folder)    
    








