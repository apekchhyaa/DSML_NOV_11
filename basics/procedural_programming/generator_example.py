def maker():
    embigger = 2
    def adder (a,b):
        return a +b + embigger

    return adder
print (f"output = {maker() (4,5)}")

#increament value by 2,3,4
"""
def increment_2(value)
    return value + 2
#lambda x: x + 2 
    
def increment_3(value)
    return value + 3
"""
def generate_increase (increment: int) -> Callable:
    def inner (value):
        return value + increment
    return inner

increment_by_2 = generate_increase (2)
increment_by_3 = generate_increase (3)

print (f"output => {increase_by_2*(4)}")
