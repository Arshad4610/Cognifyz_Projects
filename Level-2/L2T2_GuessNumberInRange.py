# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:19:15 2024

@author: rawqa
"""

import random
def guess_number():
    low=int(input("Enter lower limit:"))
    high=int(input("Enter upper limit:"))
    guess=random.randint(low, high)
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
        