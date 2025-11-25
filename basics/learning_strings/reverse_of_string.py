word: str = input ("Enter a word: ")
reversed_word: str = ""
length_word: int = len(word)
i: int = length_word - 1 #(last index if len =8 i = 7)
index = -1

while i  >= 0 :
    #index = word[i]
    #print (word[i])

    index = word[i]
    reversed_word = reversed_word + index
    i -= 1

print(reversed_word)

"""
#word.reverse

word: str = input ("Enter a word: ")
initial_position :int = len(word)-1
reversed_word = ""
for index in range (initial_position, -1, -1): #while -> i=i-1
    reversed_word = reversed_word + word [index]
print(reversed_word)
"""
"""
list (range(5,-1,-1)
-1 -> n : where to stop n is excluded, if 0 then 1st letter not included
-1 -> substracted value 
"""

