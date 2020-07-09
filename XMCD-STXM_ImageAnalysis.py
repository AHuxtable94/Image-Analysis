# -*- coding: utf-8 -*-
"""
Spyder Editor

STXM Image analysis:
For use with hdmf5 images gathered during a beamtime at PolLux, PSI.
- To view hdmf5 files, and combine them to creat an XMCD image that has
    the relevant metadata.
- To apply drift correction to the individual files such that the XMCD is aligned
- To normalise the z magnetisation using threshold values from the images pixel histogram
- To calculate the overall Mz of the disk and output this information,
    with the magnetic field, and rxy data, into a file for all images sorted into a folder
    which represents a minor hysteresis loop.
    
Written by A. J. Huxtable, July 2020.
"""

import os
import Stoner.HDF5 as SH
from Stoner.Image import ImageFile
from Stoner.Image import ImageFolder
import Stoner.Folders as SF
from Stoner import Data
import numpy as np
import scipy
from Stoner import Analysis as SA

def XMCD_metadata(i1,i2):
    """Returns the XMCD image with ___'s metadata."""
    i3=i1//i2
    
    return(i3,magnet,mean_rxy,std_rxy)
    
run=True
while run==True:
    fldr=(r'S:\Projects\TOPS  - Topological Skyrmions\Alex\STXM_PSI-2019\Sept_2019\Data1\Data1\TestingCode_2019-09-12')

    Mode=input("Would you like to:\n a) Sort hdf5 files by minorloop?\n OR \n b)process hdf5 files to make XMCD images & return metadata?\n")
    if Mode.lower=="a":
        
        start_num, start_date, end_num, end_date, daychg_num = input("Please enter the first image number and date, last image number and date, and day change number separated by spaces.\n").split()

        folder=os.path.join(fldr,input("Enter the folder name:\n"))

        os.chdir(folder)        

        if os.path.exists(folder):
            IMG_FLDR=ImageFolder(folder, pattern="*.hdf5")
            string_file = IMG_FLDR.files
            num_files=len(string_file)
            print("Number of files=", num_files)
            for i in range(0,num_files):
                print(i+1," out of ",num_files)
                Date, img_num = get_params_from_name(string_file[i])
                img_num=int(img_num)
    
                MinorLoop_folder=os.path.join(folder,input("Please enter a folder name for this set of images:\n"))
                print(MinorLoop_folder)
               # if os.path.exists(field_folder)==True:
               #     print("Folder ", field_folder, " exists!")
                #    shutil.move(string_file[i],field_folder)
                #else:
               #     os.mkdir(field_folder)
                #    shutil.move(string_file[i],field_folder)
                #i1=os.path.join
            choice=input("Do you wish to run this program again? (Y/N)\n")
            if choice=="N":
                run=False
            elif choice=="Y":
                run=True
        else:
            fldrnameerror=input("Folder does not exist, do you wish to try again? (Y/N)\n")
            if choice=="N":
                run=False
            elif choice=="Y":
                run=True    
    elif Mode.lower=="b":
       #Image, Field, Rxy, Rxy_err=XMCD_metadata(i1,i2)     
       choice=input("Do you wish to run this program again? (Y/N)\n")
       if choice=="N":
           run=False
       elif choice=="Y":
           run=True
print("Goodbye")