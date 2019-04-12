import csv
from collections import defaultdict


with open("../in/tests/my_sample.txt") as t:
    in_text = t.read()

# f = open("a.txt", "a")    
# f.write(in_text)
s = ""
persian_words = []
i = 0
step = 1
with open("../in/Entries.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    for row in readCSV:
        i = 0
        for each_data in row:
            if i%5 == 1:
                persian_words.append(each_data)
            i += 1
split_text = in_text.split()

print(persian_words)

f = open("a.txt", "a")    
f.write(str(persian_words))
visited = []
flag = True
i = 0
forms_counter = 0
parts_found = defaultdict(list) 
total_counter = 0

for j in range(len(split_text)):
    total_counter = 0
    i = 0

    # print("comes here")
    while (flag):
        total_counter += 1
        s += split_text[j][i]
        # print(s)
        wc = 0
        for word in persian_words:
            wc += 1
        
            if s == word and s not in visited:
                visited.append(s)
                parts_found[forms_counter].append(s)
                print(parts_found[1])
                if i == (len(split_text[j])-1):
                    # print("tahe jomle")
                    # flag = False
                    print(forms_counter)
                    print(parts_found)
                    for i in range(forms_counter-1):
                        if parts_found[forms_counter] == parts_found[i]:
                            flag = False
                    forms_counter += 1
                    s = ""
                    i = 0
                    break
                s = ""

            else:
                
                if i == (len(split_text[j])-1) and wc == len(persian_words):
                    
                    parts_found[forms_counter] = []
                    s = ""
                    i = -1
        # print(total_counter)
        # print(s)
        if total_counter > 1000 :
            # print("here")
            flag = False


        i += 1
# print("na comes here")
# print(visited)
# print(parts_found)
