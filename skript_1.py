"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Šalanda
email: pavel.salanda@gmail.com
discord: pavelsalanda
"""
import re

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    'bob':'123',
    'ann':'pass123',
    'mike':'password123',
    'liz':'pass123'
}

separator = '----------------------------------------'

username = input('username:')
password = input('password:')
if users.get(username) == password:
    print(f'''{separator}
Welcome to the app, {username}
We have 3 texts to be analyzed.
{separator}'''
)
else:
    print('unregistered user, terminating the program..') 
    exit()
text_number = input('Enter a number btw. 1 and 3 to select: ')
if text_number.isdigit(): 
    text_number = int(text_number)
    if text_number > 0 and text_number < 4: 
        text_number = text_number - 1
        Number_of_words = len(TEXTS[text_number].split())
        print(f'''{separator} 
There are {Number_of_words} words in the selected text.''')
        titlecase_words = 0
        for i in TEXTS[text_number].split():
            if i[0].isupper():
                titlecase_words += 1
        print(f'There are {titlecase_words} titlecase words.') 
        uppercase_words = 0
        for i in TEXTS[text_number].split(): 
            if i.isupper() and not i[0].isdigit():
                uppercase_words += 1
        print(f'There are {uppercase_words} uppercase words.')
        lowercase_words = 0
        for i in TEXTS[text_number].split(): 
            if (not i.isupper() 
                and not i[0].isupper() 
                and not i[0].isdigit()):
                lowercase_words += 1
        print(f'There are {lowercase_words} lowercase words.')
        numeric_strings = 0
        for i in TEXTS[text_number].split():
            if i.isdigit():
                numeric_strings += 1
        print(f'There are {numeric_strings} numeric string.')
        sum_numbers = []
        for i in TEXTS[text_number].split():
            if i.isdigit():
                sum_numbers.append(int(i))
        print(f'The sum of all the numbers {sum(sum_numbers)}')
        print(f'''{separator}
LEN|  OCCURENCES  |NR. 
{separator}''') 
        clear_text = [re.sub(r'[^\w\s]', '', text) for text in TEXTS]
        occurences = {}
        for i in clear_text[text_number].split():
            number = str(len(i))
            if number in occurences:
                occurences[number] += 1 
            else:
                occurences[number] = 1
        max_value = max(occurences.values())  
        max_len_key = max(len(klic) for klic in occurences.keys())
        sorted_occurences = sorted(occurences.items(),                   
        key = lambda x: int(x[0]))
        for key, value in sorted_occurences:
            gap_len = max_len_key - len(key)
            gap_len_2 = max_value - value
            print(' ' * gap_len,key, '|', value * '*',
                  ' ' * gap_len_2, '|', value)
    else:
        print('Incorrect number, exit the program.')
else:
    print('Incorrect number, exit the program.')