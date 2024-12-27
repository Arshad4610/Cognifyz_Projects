# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:27:55 2024

@author: rawqa
"""

def pass_str(p):
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sym='!@#$%^&*(),.?":{}|<>[]'
    dig="0123456789"
    if(len(p) > 20 or len(p) < 8):
        print("Password length should be between 8 and 20!")
        return False
    if not any(i in lowercase for i in p):
        print("Password should have atleast one lowercase!")
        return False
    if not any(i in uppercase for i in p):
        print("Password should have atleast one uppercase!")
        return False
    if not any(i in sym for i in p):
        print("Password should have atleast one special character!")
        return False
    if not any(i in dig for i in p):
        print("Password should have atleast one digit!")
        return False
    print("Your password is strong!")
    return True
p=input("Enter Password:")
print(pass_str(p))