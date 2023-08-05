import pdfkit
import base64
import csv
from jinja2 import Environment, FileSystemLoader

def get_image_file_as_base64_data(path):
    with open(path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def get_table_data(path):
    with open(path) as csv_file:
        csv_data = csv.DictReader(csv_file)
        return list(csv_data)

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
        "watch_image": get_image_file_as_base64_data("watch.jpg"),
        "table_data": get_table_data("data.csv")}

html = generate_html("template.html", data)
generate_pdf(html, "output_pdfs/test.pdf")