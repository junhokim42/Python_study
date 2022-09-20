# def make_unicode(input):
#     if type(input) != unicode:
#         input =  input.decode('utf-8')
#     return input

with open('abandoned_pets_data.txt', 'r') as file:
    file = file.read()
    u = unicode(file, 'utf-8')