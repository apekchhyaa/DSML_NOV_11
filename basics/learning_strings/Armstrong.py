number: int = int(input ("Enter a number: "))
#length_number: int = len(str(number))
#i: int = length_number - 1
i :int = 0
sum_numbers :int = 0
string_number : str = str(number)
length_number: int = len(string_number)

while i < length_number:
    index = int(string_number[i])
    sum_numbers += index ** length_number
    i += 1

if sum_numbers == number:
    print(f"{number} is armstrong")
else:
    print (f"{number} is not armstrong")