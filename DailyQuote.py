#!C:/Python34/python.exe

import random
import os

line_number = 0
line_num = 0

quotes_file = open('C:/Users/vfarrell/Documents/quotes/quotes.txt','rw')
for a_line in quotes_file:
    line_number += 1

quotes_file.seek(0)
fromLine = random.randint(1, line_number)

for a_line in quotes_file:
    line_num += 1
    if line_num == fromLine:
        todayquote = a_line

print(todayquote.strip())

quotes_file.close()

input("\n-Daily Quote\nHave a great day!")


