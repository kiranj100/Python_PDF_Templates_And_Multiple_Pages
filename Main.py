from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)    # for page not break for footers

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=25)
    pdf.set_text_color(20,56,14)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1,)
    pdf.line(10,21,195,21)


    # Set The Footers
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=10)
    pdf.set_text_color(150,50,25)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set The Footers
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(150, 50, 25)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

pdf.output("output.pdf")