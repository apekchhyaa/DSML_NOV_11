"""
range (start, end, step)
0 ~ len-1
range (0, len//2, 1)
"""

"""
LENGTH - 1 - i 
first index - 0
last index - 4 = length - 1

second index - 1
second last index - 3 = length - 1 - i(1)
"""

#i = 0
#x = length_word

word :str = input("enter a word: ")
length_word: int = len(word)
flag = True

for i in range (length_word//2):
    ending_index = length_word - 1 - i
    if word[i].lower() != word[ending_index].lower():
        flag = False
        break
if flag:
    print("is palindrome ")
else:
    print("is not a palindrome")

"""
while i < length_word//2 :
    index = word[i]
    end = word [x]
    if index == end :
        break
    i += 1
    x -= 1 
"""