# RTS 3/20/22

# Defines function 
def no_e(word1):
    for x in word1:
        # Checks for "e"
        if x == "e":
            return False

    return True

# opens files
words = open("words.txt")
file = open("words_without_e.txt","a")

word = words.readlines()
num1 = 0
num2 = 0
# Loop
for y in word:
    y = y.strip()
    num1 += 1
    if no_e(y) == True:
        file.write(y)
        num2 += 1

# finds %
percent = num2 / num1 * 100
print("{:.4f} percent of words do not contain e".format(percent))
# closes files
words.close()
file.close()
