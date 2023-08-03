from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_with_different_fonts(pdf_filename):

    c = canvas.Canvas(pdf_filename)

    # set font and size for the title
    c.setFont("Helvetica", 20)

    # draw the title on the PDF
    c.drawCentredString(A4[0] / 2, A4[1] - 72, "A title in Helvetica size 20!")

    # set font and size for the paragraph
    c.setFont("Helvetica", 12)

    # draw the regular paragraph on the PDF
    regular_text = "This is a regular paragraph in the PDF."
    c.drawString(72, A4[1] - 100, regular_text)

    # set font and size for the second title
    c.setFont("Helvetica", 20)

    # draw the second title on the PDF
    different_font_text = "This is a second title!"
    c.drawCentredString(A4[0] / 2, A4[1] - 144, different_font_text)

    # save the PDF
    c.save()

if __name__ == "__main__":
    pdf_filename = "different_fonts.pdf"
    generate_pdf_with_different_fonts(pdf_filename)