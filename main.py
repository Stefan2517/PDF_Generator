from fpdf import FPDF
import  pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)# valori pt RGB, de la 0 la 254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)#valori pt x1,y1,x2,y2, x-distanta in mm pe largimea,
    # iar y-inaltimea fata de marginile documentului, largimea e de 210 pt A4

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")

"""
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)

pdf.output("output.pdf")
"""