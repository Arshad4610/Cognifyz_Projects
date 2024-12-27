# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:36:45 2024

@author: rawqa
"""

def Palindrome_Checker(s):
    return True if(s==s[::-1]) else False
s=input("Enter String to check Palindrome:")
print("Result:",Palindrome_Checker(s))