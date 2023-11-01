# Define the input and output file paths
input_file = "input.txt"
output_file = "output.txt"

# Open the input file for reading and the output file for writing
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
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
            
        if len(cleaned_line.strip()) == 11:
            output_line = f'88{cleaned_line}'
            outfile.write(output_line)


