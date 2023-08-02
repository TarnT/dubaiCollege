from reportlab.pdfgen import canvas

my_canvas = canvas.Canvas("test.pdf")
my_canvas.drawString(100, 750, "This is a test PDF")
my_canvas.save()