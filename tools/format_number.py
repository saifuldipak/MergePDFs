import re

# Define the input and output file paths
pattern = re.compile('^01')
INPUT = "input.txt"
OUTPUT = "output.txt"

# Open the input file for reading and the output file for writing
with open(INPUT, "r", encoding='utf-8') as infile, open(OUTPUT, "w", encoding='utf-8') as outfile:
    for line in infile:
        cleaned_line = ''
        for char in line:
            if char.isalpha():
                continue 
            if char in (' ', '.', '-', ','):
                char = ''
            elif char in ('/'):
                char = '1'
            cleaned_line += char
            
        if len(cleaned_line.strip()) != 11:
            continue
        
        if not pattern.match(cleaned_line):
            continue
        
        output_line = f'88{cleaned_line}'
        outfile.write(output_line)
