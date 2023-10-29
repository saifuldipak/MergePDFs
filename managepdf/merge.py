import PyPDF2
import os

def merge_pdfs(output_path, *input_paths, password=None):
    merged_pdf = PyPDF2.PdfMerger()
    
    for path in input_paths:
        with open(path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file, strict=False)
            if reader.is_encrypted:
                reader.decrypt(password)  # Provide the password to decrypt the PDF
            merged_pdf.append(reader)
    
    with open(output_path, 'wb') as output_file:
        merged_pdf.write(output_file)

##Configuration:
output_path = './PDFs/merged_file.pdf'
pdf_files_folder = './PDFs'
password = '01388698001'  #(Optional) Password of the pdf files
##

pdf_files_with_prefix = [os.path.join(pdf_files_folder, file) for file in sorted(os.listdir(pdf_files_folder))]
merge_pdfs(output_path, *pdf_files_with_prefix, password=password)


