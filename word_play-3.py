# RTS 3/20/22

# Definines function 
def avoid(word,string):
    # creates list
    li = list(string)
    for x in word:
        if x in li:
            return False
    
    return True

words = open("words.txt")

word = words.readlines()
num = 0
forb_w = input("Enter the forbidden letters: ")
for y in word:
    y = y.strip()
    if avoid(y,forb_w) == True:
        num += 1

print("There are {0} words that don't contain the forbidden letters.".format(num))

# closes files
words.close()
