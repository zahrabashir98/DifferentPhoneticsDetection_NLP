import csv
from collections import defaultdict


with open("../in/tests/my_sample.txt") as t:
    in_text = t.read()

# f = open("a.txt", "a")    
# f.write(in_text)
s = ""
persian_words = []
all_phonetics = []
i = 0
step = 1
phonetic_toghether = ""
with open("../in/ha.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    for row in readCSV:
        i = 0
        print(row)
        for each_data in row:
            if i%5 == 1:
                persian_words.append(each_data)
            if i%5 == 0:
                all_phonetics.append(each_data)
            i += 1
    # print(all_phonetics)
    split_text = in_text.split()

    

    # for word in split_text:
    for word in split_text:
        for row in readCSV:
            if row[1] == word:
                phonetic_toghether += row[0]

print(phonetic_toghether)
