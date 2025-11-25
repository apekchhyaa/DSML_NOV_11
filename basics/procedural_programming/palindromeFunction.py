

'''
if flag:
    print("is palindrome ")
else:
    print("is not a palindrome")
'''




def is_palindrome (word):
    flag = True
    for i in range(len(word) // 2):
        #ending_index = length_word - 1 - i
        #if word[i].lower() != word[ending_index].lower():
        if word[i].lower() != word [len(word)- 1 - i]:
            flag = False
            break

    return flag


word :str = input("enter a word: ")

if is_palindrome(word):
    print("is palindrome ")
else:
    print("is not a palindrome")


