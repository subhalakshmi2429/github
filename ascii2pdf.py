#!/bin/python

# This Program converts the norman ascii file into PDF file 

from fpdf import FPDF
import os

while True:
    datalist = os.listdir("source")

    if len(datalist) >= 1:

        # save FPDF() class into 
        # a variable pdf
        pdf = FPDF()   
        
        # Add a page
        pdf.add_page()
        
        # set style and size of font 
        # that you want in the pdf
        pdf.set_font("Arial", size = 14)
        
        # open the text file in read mode
        f = open(f"source/{datalist[-1]}", "r")
        
        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        
        # save the pdf with name .pdf and delete the files with in the source Directory
        pdf.output(f"destination/{datalist[-1]}.pdf")  
        os.remove(f"source/{datalist[len(datalist)-1]}")