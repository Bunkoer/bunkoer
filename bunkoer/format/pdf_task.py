import PyPDF2
from fpdf import FPDF
from datetime import datetime


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text


def create_pdf_with_text(content):
    output_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".pdf"
    content = ''.join(char for char in content if char.isascii())
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    
    # Adding the content in a multi-cell
    pdf.multi_cell(0, 10, content)
    
    # Save the PDF with the specified filename
    pdf.output(output_filename)
    return output_filename
