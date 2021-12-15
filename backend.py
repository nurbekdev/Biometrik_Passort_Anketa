# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:44:41 2021

@author: ALFA ELectronics
"""

from docxtpl import DocxTemplate


def fillDoc(info,fayl="anketa.docx"):
    anketa = DocxTemplate("anketa.docx")
    anketa.render(info)
    filname = f"{info['familiya']}_anketa.docx"
    anketa.save(filname)
    return filname
    