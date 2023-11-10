from fpdf import FPDF
import  pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #implicit e True, sa nu depinda paginile una de alta

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)# valori pt RGB, de la 0 la 254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 298, 10):  # 10 e pasul
        pdf.line(10, y, 200, y)

    #pdf.line(10, 21, 200, 21)#valori pt x1,y1,x2,y2, x-distanta in mm pe largimea,
    # iar y-inaltimea fata de marginile documentului, largimea e de 210mm pt A4
    # inaltimea e 298mm pt A4

    #Set the footer
    pdf.ln(265) #ar da de 278 Enter pe cursor sa ajunga in josul paginii
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)  # h=12 + ln initial 265= 277
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10): #10 e pasul
            pdf.line(10, y, 200, y)
pdf.output("output.pdf")

"""
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)

pdf.output("output.pdf")
"""