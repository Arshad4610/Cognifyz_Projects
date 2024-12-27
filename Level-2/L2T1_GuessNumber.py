# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:05:00 2024

@author: rawqa
"""
import random
def guess_number():
    guess=random.randint(1, 100)
    c=0
    while(True):
        user=int(input("Enter guess:"))
        c+=1
        if(user<guess):
            print("Too low")
        elif(user>guess):
            print("Too high")
        else:
            print(f"You guessed the right number in {c} attempts!")
            break
guess_number()
        