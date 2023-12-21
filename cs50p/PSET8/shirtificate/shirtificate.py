from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 25, 35, 160)
        self.set_font("helvetica", "B", 40)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "I", 25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(180, 120, name + " took CS50", align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
