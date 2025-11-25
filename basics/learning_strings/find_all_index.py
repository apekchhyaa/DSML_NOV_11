"""
takes a word from the user
takes a letter from the user

find all the occurances of the letter in the word
"""

word: str = input("enter a word ")
letter: str = input("enter a letter ")
indexes : list[int] = [] #() - either can be used

if len(letter) != 1:
    print("letter is too long. Must be one Character")
    exit(1)

"""
for <storage> in <iterator>:
    {BL}
enumerate(<iterator>) - enumerate(Apekchhya) - (0,a), (1,p) ...

iter 1 :
index, character - (0,a) #tuple destructuring

finding letter h
iter 6:
index, character - (5, h ) 
if case: [].append(5) - index:[5]

iter 7:
index, character - (6,h)
if case: [5].append(6) - indexes : [5,6]

"""

for index, character in enumerate(word):
    if character.lower() == letter.lower():
        indexes.append(index)

if indexes :
    print(f"letter { letter} found at index {indexes}")
else:
    print (f"letter {letter} not found in {word}")
