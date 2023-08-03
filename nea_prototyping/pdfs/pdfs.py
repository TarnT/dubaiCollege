import pdfkit

def generate_pdf(html_content, output_path):
    try:

        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

        # generate PDF
        pdfkit.from_string(html_content, output_path, configuration=config)
        
        print(f"PDF generated!")

    except Exception as e:
        print(f"Error generating PDF: {e}")

with open("pdf_html.html", "r") as html_file:
    html_content = html_file.read()

output_path = "/Users/tarntimmermans/Documents/repositories/dubaiCollege/nea_prototyping/pdfs/output_pdfs/test.pdf"
generate_pdf(html_content, output_path)