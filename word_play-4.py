# RTS 3/20/22

# defines function
def uses_only(word,letters):
    #Create lists
    l = list(letters)
    w = list(word)
    for x in letters:
        if x not in w:
            return False 
    return True

# open file
words = open("words.txt")

word = words.readlines()
num = 0
u_w = input("Enter the uses only letters: ")
for y in word:
    y = y.strip()
    if uses_only(y,u_w) == True:
        num += 1 # adds 1 if has use only letter

print("There are {0} words contain the use only letters.".format(num))

 # closes file
words.close()
