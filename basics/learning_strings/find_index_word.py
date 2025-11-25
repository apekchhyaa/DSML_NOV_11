word: str = input ("Enter a word: ")
letter: str = input ("Enter a letter: ")

#in the case that the letter is not in the given word
length_word: int = len(word)
i: int = 0
index : int = -1

if len(letter) > 1:
    print("letter is too long. Must be one Character")
    exit(1)

while i < length_word:
    if word [i] == letter:
        index = i
        #print (f"Value found at index:{index}")
        #exit (0)
        break
    i += 1

if index != -1:
    print (f"Value found at index:{index}")
else:
    print (f"Value found at word:{word}")

print(f"{'-'*50}")

#prints all letters of the word
"""
#printing the word char by char
#while i <= length_word - 1
while i < length_word:
    print (word[i])
    i += 1
"""

"""
#assuming one letter 
while i < length_word:
    if word [i] == letter:
        index = i
        print (f"Value found at index:{index}")
        exit (0)
"""
