# Converts file from UTF-8 Encoding to UTF-16 Encoding
# Created May 2022 by Harrison Low
valid = False
while not valid:
    original_chart = input("Input the name of the text file being converted: ")
    # Checks if file given ends with txt
    if original_chart.endswith('.txt'):
        new_chart = input("New text file being created: ")
        if new_chart.endswith('.txt'):
            valid = True
    if not valid:
        print('Invalid file name, please end both files with .txt')
file_format = input('Input original file format: ')
new_format = input('Input new file format: ')
with open(original_chart, 'rb') as f:   # Opens the file and reads it in binary form, this allows us to read it in byte form
    with open(new_chart, 'wb') as chart:   # Creates a new file named Hiragana.txt and writes in binary form to keep the form of the original file
        original_content = f.read()
        # Decodes the original content of the file(which is utf-8 by default in python but could change so I should probably set it as a variable instead of hard coding) then encodes it to utf-16
        #chart.write(original_content.decode('utf-8').encode('utf-16')) 
        chart.write(original_content.decode(file_format.lower()).encode(new_format.lower()))
