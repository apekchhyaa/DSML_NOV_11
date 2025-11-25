def custom_sum(operation_type = sum, *args): #return total of any number of numbers
    """
    function to add values using args
    :param operation_type:
    :param args:
    :return:
    """
    total = 0
    for value in args:
        total+= value

    return total

"""
def square(number: int | float ) -> int | float:
    return number ** 2
"""
#square = lambda x: x ** 2

def custom_apply (func:callable, *args ):
    applied_list = list()
    for value in args:
        applied_list.append(
            func(value)
        )

    return applied_list

#print (f"total => { custom_apply (square,  1,2,3,4,5,1,1)}")
print (f"total => { custom_apply (
        lambda x: x ** 2, 
    #square,
        1,2,3,4,5,1,1
    )}"
)
