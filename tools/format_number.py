import re

# Edit the following variables as required
INPUT_PREFIX = '^01'
OUTPUT_PREFIX = '88'
NUMBER_OF_DIGITS = 11
INPUT = "input.txt"
OUTPUT = "output.txt"

# Open the input file for reading and the output file for writing
input_pattern = re.compile(f"{INPUT_PREFIX}")
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
            
        if len(cleaned_line.strip()) != NUMBER_OF_DIGITS:
            continue
        
        if not input_pattern.match(cleaned_line):
            continue
        
        output_line = f"{OUTPUT_PREFIX}{cleaned_line}"
        outfile.write(output_line)
