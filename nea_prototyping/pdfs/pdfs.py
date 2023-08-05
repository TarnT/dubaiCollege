import pdfkit
from jinja2 import Environment, FileSystemLoader
import base64

def get_image_file_as_base64_data():
    with open(FILEPATH, 'rb') as image_file:
        return base64.b64encode(image_file.read())

def generate_html(template_path, data):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_path)
    return template.render(data)

def generate_pdf(input_data, output_path):
    try:

        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

        # generate PDF
        pdfkit.from_string(input_data, output_path, configuration=config)
        
        print(f"PDF generated!")

    except Exception as e:
        print(f"Error generating PDF: {e}")

data = {"title": "This a title using Jinja",
        "name": "Tarn",
        "watch_image": image_to_string("watch.jpg")}

output_path = "/Users/tarntimmermans/Documents/repositories/dubaiCollege/nea_prototyping/pdfs/output_pdfs/test.pdf"
html = generate_html("template.html", data)
generate_pdf(html, "output_pdfs/test.pdf")