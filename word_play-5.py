# RTS 3/30/22

#defines function
def is_abecedarian(word):
    w = list(word)
    x = 1
    while x < len(word):
        if not w[x] >= w[x-1]:
            return False
        
        x += 1

    return True

# opens file
words = open("words.txt")

# reads file
word = words.readlines()
num = 0


for y in word:
    y = y.strip() 
    if is_abecedarian(y) == True:
        num += 1

print(num)

# closes file
words.close()
