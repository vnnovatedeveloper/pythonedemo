

from img2table.document import PDF
from img2table.ocr import TesseractOCR
import pandas as pd

from PIL import Image
from reportlab.pdfgen import canvas
import tabula







def convert_image_to_pdf(image_path, output_pdf_path):
    img = Image.open(image_path)
    img.save(output_pdf_path, "PDF", resolution=100.0)

def extract_table_data_from_pdf(pdf_path):
    try:
        # Use tabula to extract tables from the PDF
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

        # Assuming the table of interest is in the first extracted table
        if tables:
            # Get the first table
            table_data = tables[0]

            return table_data
        else:
            print("No tables found in the PDF.")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Path to the JPEG image and output PDF file
    image_path = "test1.jpeg"
    output_pdf_path = "output.pdf"

    # Convert image to PDF
    convert_image_to_pdf(image_path, output_pdf_path)

    # Extract table data from the PDF
    table_data = extract_table_data_from_pdf(output_pdf_path)

    if table_data is not None:
        # Display the table data
        print(table_data)
    else:
        print("Failed to extract table data from the PDF.")



# Instantiation of the pdf
pdf = PDF(src="output.pdf")

# Instantiation of the OCR, Tesseract, which requires prior installation
ocr = TesseractOCR(lang="eng")

# Table identification and extraction
pdf_tables = pdf.extract_tables(ocr=ocr)





# We can also create an excel file with the tables
pdf.to_xlsx('tables.xlsx',ocr=ocr)



# Specify the path to your Excel file
excel_file_path = 'path/to/your/excel/file.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel('tables.xlsx')

# Print the DataFrame
print("Contents of the Excel file:")
print(df)
