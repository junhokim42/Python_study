from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"P09_Translation\English_file.txt"
write_file_path = r"P09_Translation\Korean_file.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding = 'UTF8') as f:
        f.write(result1.text + '\n')