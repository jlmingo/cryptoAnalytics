import pandas as pd
from fpdf import FPDF
import glob, os

os.chdir("./")
img = []
for file in glob.glob("*.png"):
    img.append(file)
    print(file)

def createPDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.multi_cell(0, 10, 'Selected Charts for Stocks and Cryptocurrency Analysis', align='C')
    pdf.ln(10)
    for e in img:
        pdf.image('./{}'.format(e), w=200)
        print(e)
        pdf.ln(10)
    pdf.output('../output/crypto_Analysis.pdf', 'F')
    return ['../output/crypto_Analysis.pdf', 'crypto_Analysis.pdf' ]