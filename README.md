## Description
'merge.py' is a script to merge multiple pdf files into one. It can merge password protected pdf files also.

## Installation
**Install prerequisite packages**   
`$ pip install -r requirements.txt`

## Create merged pdf
1. **Copy the pdf files into 'PDFs' directory**

2. **Rename pdf files**   
    rename pdf files like a.pdf, b.pdf, c.pdf ....  
    'a.pdf' appear first and 'b.pdf' appear second in the merged file,   
    so rename the files in the order you want them to appear in the merged pdf file.

3. **Edit Configuration section in the merge.py file to set**   
    pdf files folder  
    output file folder and   
    pdf file password(if password protected)

4. **create merged pdf file**  
    `$ python3 merge.py`
    