import csv
from collections import defaultdict




def dictionaryContains(word):
    # print(len(all_phonetics))
    # all_phonetics = ["bAqbAn","An","b","mobile","samsung","sam","sung", 
    #                         "man","mango", "icecream","and", 
    #                         "go","i","love","ice","cream""bAq","Ce","Cera","ra","bAqCe"]
    # print(word)
    # print(type(word))
 
    for i in range(len(all_phonetics)):
        
        if all_phonetics[i] == word :
            return True
    return False


def wordBreak(sttr):
    print("oomad too in")
    wordBreakUtil(sttr, len(sttr), "")

  
f = open("b.txt", "w")
def wordBreakUtil( sttr,  n,  result):
     
    for i in range(1,n+1):
        prefix = sttr[0:i]


        if (dictionaryContains(prefix)) :
            if (i == n):
                result += prefix
                print(result)

                   
                f.write(result)
                f.write("\n")
                return
            wordBreakUtil(sttr[i:n+1], n-i, result + prefix + " ")




all_phonetics = []

with open("../in/Entries.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    for row in readCSV:
        i = 0
        # print(row)
        for each_data in row:
            # if i%5 == 1:
            #     persian_words.append(each_data)
            if i%5 == 0:
                all_phonetics.append(each_data)
            
            i += 1

wordBreak("bAqbAnAnbAqCerAnegAhkard")
# wordBreak("‌bAqbAnAnbAqCeranegAhkard")
