import csv
from collections import defaultdict


# this function checks wether the input word is in dataset or not
def is_in_dataset(word):

    for i in range(len(all_phonetics)):
        
        if all_phonetics[i] == word :
            return True
    return False

# here is the function which first calls "breakWord"
def input(string):
    print("oomad too in")
    breakWord(string, len(string), "")

  

# this is my recursive function
def breakWord( string,  n,  result):

    # worde breaking procedure 
    for i in range(1,n+1):
        prefix = string[0:i]

        if (is_in_dataset(prefix)) :

            # if reached end of sentence
            if (i == n):
                result += prefix
                print(result)    
                f.write(result)
                f.write("\n")
                return
            # call "breakWord" recursively for the rest of word
            breakWord(string[i:n+1], n-i, result + prefix + " ")


if __name__ == '__main__':
    f = open("b.txt", "w")
    all_phonetics = []

    with open("../in/Entries.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # print(readCSV)
        for row in readCSV:
            i = 0
            for each_data in row:
                if i%5 == 0:
                    all_phonetics.append(each_data)
                
                i += 1
    
    # input("bedunerang'AsemAnzeSt'ast")
    input("bAqbAn'AnbAqCerAnegAhkard")
    # input("bAbAbA'AbAdAnjAleb'ast")
    # input("mAdAm")
    # input("‌bAqbAn'AnbAqCeranegAhkard")
