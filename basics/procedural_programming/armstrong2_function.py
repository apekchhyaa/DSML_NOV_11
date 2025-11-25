def is_armstrong(number):
    temp_number: int = number
    total = 0
    for i in range(len(str(number))):
        q = temp_number // 10
        r = temp_number % 10
        total += r ** len(str(number))
        temp_number = q
        if q == 0:
            return total

number: int = int(input ("Enter a number: "))

if is_armstrong(number) == number:
    print(f"{number} is armstrong")
else:
    print(f"{number} is not armstrong")