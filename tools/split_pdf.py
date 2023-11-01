#This is a script to split a pdf file 

from PyPDF2 import PdfWriter, PdfReader
from os.path import join

input_file = "Saiful-PF.pdf"
input_folder = "./PDFs"
output_folder = "./PDFs"

inputpdf = PdfReader(open(join(input_folder, input_file), "rb"))
input_file_name = input_file.split('.')

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    output_file = join(output_folder, f'{input_file_name[0]}-{i}.pdf')
    with open(output_file, "wb") as outputStream:
        output.write(outputStream)
