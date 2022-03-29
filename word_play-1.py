# RTS 3/30/22

# opens the files
words = open("words.txt")
file = open("file.txt","a")

word = words.readlines()
for x in word:
#checks if the word is > 20
    if len(x.strip()) > 20: 
        file.write(x)

# closes files
words.close()
file.close()
