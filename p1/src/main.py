import csv


def check_other_part_of_word(pointer, split_text, persian_words):
    string = ""
    print(split_text)
    for i in range(pointer+1,len(split_text)):
        
        string += split_text[i]
        for word in  persian_words:
            if s == word:
                # print(word)
                if check_other_part_of_word(pointer, split_text, persian_words):
                    s = ""
                    countinue
                    return true
                else:
                    pointer += 1
            else:
                pointer += 1


        

with open("../in/tests/my_sample.txt") as t:
    in_text = t.read()

# f = open("a.txt", "a")    
# f.write(in_text)

s = ""
persian_words = []
i = 0
step = 1
with open("../in/ha.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
    for row in readCSV:
        i = 0
        for each_data in row:
            if i%5 == 1:
                persian_words.append(each_data)
            i += 1
split_text = in_text.split()
print(type(split_text))
print(split_text)
pointer = 0
last_pointer_memory = 0
parts_found = []
visited = []

# for i in range(len(split_text[0])+1):
#     s += split_text[0][i]
#     print("i:%s"%i)
#     print(s)
#     for word in persian_words:
#         if s == word and s not in visited:
#             parts_found.append(s)
#             visited.append(s)
#             s = ""
#             last_pointer_memory = pointer
#         else:
#             if i== len(split_text[0])-1:#if pointer == len(split_text[0]):# 
#                 print ("here")
#                 i = 0 
#                 pointer = 0
#                 parts_found = []

#                 #goto step 
#                 # pointer = last_pointer_memory - len(s)-len(parts_found[-1])
#                 # i = pointer
#             pointer += 1
flag = True
i = 0
while(flag):
    s += split_text[0][i]
\
    print(visited)
    print(type(i))
    print(type(len(split_text[0])-1))
    print("i:%s , len(text):%s"%(i,len(split_text[0])-1))
    for word in persian_words:
        if s == word and s not in visited:
            print("oomad to =")
            parts_found.append(s)
            visited.append(s)
            s = ""
            
            if i == len(split_text[0])-1:
                print("FFF")
                flag = False

        else:
            if i== len(split_text[0])-1:
                print ("here")
                i = 0
                parts_found = []


            
    i += 1

# print(visited)
# print(parts_found)       
# for i in range(len(in_text)-1):
#     s += in_text[i]
#     print(s)
#     for word in persian_words:
#         if s == word:
#             # print(word)
#             s = ""

