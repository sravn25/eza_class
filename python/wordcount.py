def countCharacter(word):
    length = len(word)
    print("The character count is :", length)

def countWord(word):
    arr = word.split()
    length = len(arr)
    print("The word count is :", length, "\n")

while True:
    word = input("Please enter your words\nType Stop to stop\n")
    print("Your word is", word, sep=": ", end=".\n")
    countCharacter(word)
    countWord(word)
    if word.lower() == "stop":
        break

