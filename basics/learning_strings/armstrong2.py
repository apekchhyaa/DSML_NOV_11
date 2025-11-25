number: int = int(input ("Enter a number: "))
#q = number //10
#r = number % 10
total = 0
temp_number: int = number #temporary number
length_number = len(str(number))

while True:
    q = temp_number // 10
    r = temp_number % 10
    total += r ** length_number
    temp_number = q
    if q == 0:
        break

if total == number:
    print(f"{number} is armstrong")
else:
    print (f"{number} is not armstrong")
"""
iteration 1 
temp -> 153, R -> 3, q ->15: T-> Q
temp -> 15, R -> 5, q -> 1 : T-> 1
"""
