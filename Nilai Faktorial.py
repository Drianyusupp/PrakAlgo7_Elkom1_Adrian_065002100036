# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:28:45 2021

@author: User
"""


print("=== PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA ===")
def factorial(angka) : 
    if angka > 1 :
        return angka * factorial (angka-1)
    else : 
        return 1
    
angka = int(input("Masukkan Angka : "))
print("Nilai faktorialnya adalah : ", factorial(angka))   