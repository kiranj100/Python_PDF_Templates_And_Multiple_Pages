from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

#this for loop for generate master pages
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=25)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L")
    pdf.set_text_color(150,50,85)

    #set the footer
    pdf.ln(277)
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(150, 50, 85)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R",ln=1)

    for y in range(20,298,10):
        pdf.line(10,y,200, y)

    pdf.line(10, 21, 200, 21)

    # in master page we want some blank pages 
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #set the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(150, 50, 85)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("exercise.pdf")