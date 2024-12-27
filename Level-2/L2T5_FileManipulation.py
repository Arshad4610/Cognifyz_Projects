# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:56:53 2024

@author: rawqa
"""

def file_manipulation(file):
    try:
        with open(file,'r') as f:
            te=f.read()
        te=te.lower()
        te=te.replace('.',' ')
        te=te.replace(',',' ')
        te=te.replace('!',' ')
        w=te.split()
        d={i:w.count(i) for i in w}
        s=sorted(d.items())
        for word,cnt in s:
            print(f"{word}: {cnt}")
    except FileNotFoundError:
        print(f"Filename {file} was not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    
file=input("Enter the filename:")
file_manipulation(file)


'''Hello world! Hello Python.
Python is great. Hello, world!
Python is a programming language.'''