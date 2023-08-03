import pdfkit

def generate_pdf(html_content, output_path):
    try:

        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

        # generate PDF
        pdfkit.from_string(html_content, output_path, configuration=config)
        
        print(f"PDF generated successfully at: {output_path}")
        
    except Exception as e:
        print(f"Error generating PDF: {e}")

# Example usage
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample PDF</title>
</head>
<body>
    <h1>Hello, this is a sample PDF generated using Python and HTML!</h1>
    <p>More content can go here...</p>
</body>
</html>
"""

output_path = "sample_output.pdf"
generate_pdf(html_content, output_path)
