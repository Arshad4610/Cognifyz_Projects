# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:15:56 2024

@author: rawqa
"""

import os
import shutil

def organize_files(directory):
    # Change to the target directory
    os.chdir(directory)

    # Loop through all files in the directory
    for file in os.listdir('.'):
        if os.path.isfile(file):  # Check if it's a file
            # Get the file extension
            file_ext = file.split('.')[-1]
            # Create a new directory for the file type if it doesn't exist
            if not os.path.exists(file_ext):
                os.makedirs(file_ext)
            # Move the file into the corresponding directory
            shutil.move(file, f"{file_ext}/{file}")

# Example usage
organize_files('C:/cs')
