#math related functions

def is_even(number):
    """
    returns true if the number is even else returns false
    """
    return number % 2 == 0

if __name__ != '__main__':
    print("DTC math imported")

if __name__ == '__main__':
    number = int(input("enter a number:"))
    print (f"Number: {number} is even {is_even(number)}")



