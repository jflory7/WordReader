#!/usr/bin/python3
import re
import sys

if len(sys.argv) != 2:
    print("Invalid number of arguments. Please provide only one argument as the file location.")
    exit()

in_file = open(sys.argv[1], 'r')
quote = in_file.readline().lower()
in_file.close()
words = re.split('[^A-Za-z]', quote)
while '' in words: words.remove('')

highest_char = []
index = 0
output_word = ""

while index < len(words):
    count = {}
    for s in words[index]:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    highest_char.append(max(count.values()))
    index += 1

index = 0
tmp = 0

while index < len(highest_char):
    if highest_char[index] > tmp:
        tmp = highest_char[index]
        output_word = words[index]
    index += 1

print(output_word)
