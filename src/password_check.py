import re
from collections import Counter
import getpass

def password_check(password):

    # calculating the length
    length_error = len(password) < 10

    # searching for digits
    digit_error = re.search(r'\d', password) is None

    # searching for uppercase
    uppercase_error = re.search(r'[A-Z]', password) is None

    # searching for lowercase
    lowercase_error = re.search(r'[a-z]', password) is None

    # searching for symbols
    symbol_error = re.search(r'\W', password) is None

    WC = Counter(password)
    c = 0
    # Finding no. of  occurrence of a character
    # and get the index of it.
    for letter, count in WC.items():
        if (count > 1):
            c += 1
    # searching for repeating characters
    if c == 0:
        repeat_char_error = False
    else:
        repeat_char_error = True

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error or repeat_char_error )

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
        'repeat_char_error' : repeat_char_error
    }

if __name__ == '__main__':
    print ('Enter a password')
    #in case for hidding password
    #password = getpass.getpass('Password: ')
    password = input('Password: ')
    dict = password_check(password)
    for item in dict:
        print('\t{} : {}'.format(item, dict[item]))