## Description
This is a collection of Python scripts to merge/split pdf files, format contact numbers etc. It can merge password protected pdf files also. Tested on Python >=3.10.6.

## Installation
**Install prerequisite packages**   
`$ pip install -r requirements.txt`

## Merge a pdf file
1. **Copy the pdf files into 'PDFs' directory**

2. **Rename pdf files**   
    rename pdf files like a.pdf, b.pdf, c.pdf ....  
    'a.pdf' appear first and 'b.pdf' appear second in the merged file,   
    so rename the files in the order you want them to appear in the merged pdf file.

3. **Edit Configuration section in the merge.py file to set**   
    pdf files folder  
    output file folder and   
    pdf file password(if password protected)

4. **Create merged pdf file**  
    `$ python3 merge.py`

## Split a pdf file
1. **Copy the pdf file that needs to be splitted into the 'PDFs' directory**

2. **In 'spilt.py' set the file(step 1) name in 'input_file = ' line**

3. **Split file. Note: it will create a pdf file of each page from the input file**
    `$ python3 split.py`

## Format contact numbers
This script removes some characters, replace some characters and ignore if its not a number. It takes number from a file and after formatting those numbers, writes to another file.

1. **Set the input and output filepath in the script.**
2. **Run script**  
    `$ python3 format_number.py`
