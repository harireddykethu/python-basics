user_input = input('Tell us something: ')

modified_input = map(lambda ch: ch.upper(), user_input)

modified_input_string = ''

for letter in modified_input:
    modified_input_string += letter
else:
    print(modified_input_string)
