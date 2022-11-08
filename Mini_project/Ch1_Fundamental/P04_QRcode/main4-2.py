import qrcode

file_path = r'P04_QRcode\QRcode_list.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)