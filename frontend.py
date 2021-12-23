# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:52:25 2021

@author: ALFA ELectronics
"""

from pywebio.input import input, input_group




def getInfo():
    return input_group("Fuqaro haqida ma'lumot",[
        input('Ism', name='ism',),
        input('Familiya', name='familiya',),
        input('Otasinging ismi', name='otasi',),
        input("Tug'ilgan yili", name='tyil',),
        input("Tug'ilgan kun", name='tkun',),
        input("Tug'ilgan oy", name='toy',),
        input("Telefon raqami", name='telefon',),
        input("Pasport seriyasi", name='seriya',),
        input("Pasport raqami", name='pass_raqam',),
        input("Pasport berilgan sana", name='pass_sana',),
        ])













 
    

