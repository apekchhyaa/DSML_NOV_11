#math related functions

def is_even(number):
    """
    returns true if the number is even else returns false
    """
    #return True if number % 2 == 0
    return number % 2 == 0

if __name__ != '__main__': #when DTC is not the main file.. imported in another file and function called
    print("DTC math imported")

if __name__ == '__main__': #when DTC is the main file.. this runs normally
    number = int(input("enter a number:"))
    print (f"Number: {number} is even {is_even(number)}")
    #print (is_even(2))


#is_odd function , true if odd, false

