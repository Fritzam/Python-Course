numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    else:
        print(str(number) + "th")