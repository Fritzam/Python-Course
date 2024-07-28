try:
    a = input("Proszę podać wartość a:")
    b = int(input("Proszę podać wartość b: "))
    result = int(a) + b  # Convert 'a' to integer before adding
except ValueError:
    print("One of the inputs is not a valid number!")
except TypeError:
    print("Type mismatch - cannot add different types!")
else:
    print("Value is: " + str(result))