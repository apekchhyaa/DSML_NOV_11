word: str = input ("Enter a word: ")
reversed_word: str = ""
length_word: int = len(word)
i: int = length_word - 1 #(last index if len =8 i = 7)
index = -1

while i  >= 0 :
    index = word[i]
    reversed_word = reversed_word + index
    i-= 1

print(reversed_word)
if reversed_word == word:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")

