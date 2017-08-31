# Python Password Generator.

import requests
import random

def main_loop():
    print("Python Password Generator")

    print('''
        1. XKCD - Generates an XKCD-like password.
        2. String - Generates a string of random characters
        ''')

    o = int(input("Choose an option: "))

    if o == 1:
        XKCD()
    if o == 2:
        Char_Pass()

def XKCD():
    r_list = []

    n = int(input("Choose the number of words to generate: "))

    wordlist = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(wordlist)
    words = response.content.splitlines()

    pass_list = random.sample(words, n)

    for word_item in pass_list: # Simple formatting loop for each word. Decodes bstr to a str and checks if 1st letter is uppercase.
        word = word_item.decode('utf-8')
        if word[0] != word[0].upper(): # Simple check to see if first letter is uppercase.
            first_letter = word[0].upper() # Make a new first letter
            word = first_letter + word[1:] # Join the new first letter and rest of the word.
        r_list.append(word)

    r = " ".join(r_list)
    print(r)

def Char_Pass():
    # type_list = list(range(0,4))
    # print(random.sample(type_list, 12))
    type_list = []
    pass_list = []

    n = int(input("Choose the number of Characters to generate: "))
    print("""
        Add 'a' for numbers (0-9)
        Add 'b' for symbols (!@#$%^&*)
        Add 'c' for lowercase letters (a-z)
        Add 'd' for uppercase letters (A-Z)
        """)
    options = (input('Choose what characters you would like to generate: '))

    for i in range(n):
        choice = random.choice(options)
        type_list.append(choice)

    similar = input('Would you like to remove similar characters? (y/n): ')
    if similar == 'y' or similar == 'yes':
        r_list = typelist_no_sim(type_list)
    elif similar == 'n' or similar ==  'no':
        r_list = typelist_with_sim(type_list)

    r = "".join(r_list)
    print(r)

def typelist_no_sim(my_list):
    pass_list = []
    for i in my_list:
        if i == 'a':
            x = random.choice('2345789')
            pass_list.append(x)
        elif i == 'b':
            x = random.choice('!@#$%^&*')
            pass_list.append(x)
        elif i == 'c':
            x = random.choice('abcdefghjkmnpqrstuvwxyz')
            pass_list.append(x)
        elif i == 'd':
            x = random.choice('ABCDEFGHJKMNPQRSTUVWXYZ')
            pass_list.append(x)
    return(pass_list)


def typelist_with_sim(my_list):
    pass_list = []
    for i in my_list:
        if i == 'a':
            x = str(random.randint(0,9))
            pass_list.append(x)
        elif i == 'b':
            x = random.choice('!@#$%^&*')
            pass_list.append(x)
        elif i == 'c':
            x = random.choice('abcdefghijklmnopqrstuvwxyz')
            pass_list.append(x)
        elif i == 'd':
            x = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            pass_list.append(x)
    return(pass_list)

main_loop()