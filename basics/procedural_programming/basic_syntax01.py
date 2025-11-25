from dtc_math import is_even

#name = "apekchhya" #global variable
"""
number1 = input("enter number 1")
number2 = input("enter number 2")
"""

"""
integers = []
for i in range (4):
    #integers.append(int((f"Enter number {i+1}:")))
    value = int ( input(f"Enter number {i+1}:"))
    integers.append(value)
"""

#comprehention
value = input("enter number in sequence n1,n2,n3,n4: ")
numbers = value.split(',')

for i in range(len(numbers)):
    numbers[i] = int (numbers[i])

#takes four numbers and gives sum
def sum_four (n1,n2,n3,n4 = 0):
    return n1 + n2 + n3 + n4

#total = sum_four( 1,2,3,4)
total = sum_four( * numbers)
#total = sum_four( number[0], number[1], number[2], number[3])

#print (is_even(total))
print (f"Number: {total} is even {is_even(total)}")