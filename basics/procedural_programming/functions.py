
#name = "apekchhya" #global variable
print("-"*50)

def greet(name):
    #name = "test"
    print (f"good morning {name}")
#greet() #test #scope of function remains inside function. cannot access test name outside the functions
#variable declared inside function cannot be called outside the function
#global name is replaced inside function
greet('a')
greet('p')
greet('e')


print("-"*50)

#takes four numbers and gives sum
def sum_four (n1,n2,n3,n4 = 0): #allowed to input only 3 numbers, default value for n4 set, if n4 value added then the default will be replaced
    #starting from right n3 = 0 is wrong is n4 is not given default 0 as well
    return n1 + n2 + n3 + n4

total = sum_four( 1,2,3,4)


