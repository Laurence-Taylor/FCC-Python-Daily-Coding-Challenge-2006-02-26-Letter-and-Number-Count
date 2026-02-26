def count_letters_and_numbers(s):
    # set counter letters to 0
    count_letter = 0
    # set counter numbers to 0
    count_number = 0
    # iterate over each character in message
    for char in s:
        # if character is a leter count letters
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            count_letter += 1
        # if character is a number count numbers
        elif 48 <= ord(char) <= 57:
            count_number += 1
    # return result following the instructions
    if count_letter == 1 and count_number == 1:return f'The string has {count_letter} letter and {count_number} number.'
    elif count_letter == 1:return f'The string has {count_letter} letter and {count_number} numbers.'
    elif count_number == 1:return f'The string has {count_letter} letters and {count_number} number.'
    else:return f'The string has {count_letter} letters and {count_number} numbers.'

    return s

if __name__ == '__main__':
    print(count_letters_and_numbers("helloworld123"))
    print('--------')
    print(count_letters_and_numbers("Catch 22"))
    print('--------')
    print(count_letters_and_numbers("A1!"))
    print('--------')
    print(count_letters_and_numbers("12345"))
    print('--------')
    print(count_letters_and_numbers("password"))