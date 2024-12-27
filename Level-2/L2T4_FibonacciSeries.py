# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:52:56 2024

@author: rawqa
"""

def fib_series(n):
    fib=[]
    a,b=0,1
    for _ in range(n):
        fib.append(a)
        a,b=b,a+b
    print(f"The first {n} terms of the Fibonacci series are: {fib}")
n=int(input("Enter number of terms for fibonacci series:"))
fib_series(n)