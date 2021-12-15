# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:01:50 2021

@author: ALFA ELectronics
"""
from pywebio.output import put_file, put_html
from pywebio.session import hold
from frontend import getInfo
from backend import fillDoc

title = "<h1 style=\"text-align:center\">O'zbekiston Respublikasi fuqarolaringing xorijga chiqish biometrik\
    pasportini rasmiylashtirish uchun ANKETA</h1>"
put_html(title)

userInfo = getInfo()
filname =fillDoc(userInfo)

text ="<h3>Anketa Tayyor.\
    Yuklab olish uchun yuklamani bosing.</h3>"
put_html(text)
with open(filname, 'rb') as fayl:
    anketa = fayl.read()
    put_file(filname, content=anketa)
    hold()