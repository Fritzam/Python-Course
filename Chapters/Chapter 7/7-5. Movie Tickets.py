active = True
while active:
    query = input("Provide the age to check the price.\nWrite 'quit' to end.")
    if query == 'quit':
        active = False
        continue
    query = int(query)
    if query < 3:
        print("The ticket is free!")
    elif query >= 3 and query < 12:
        print("The ticket is 10$")
    else:
        print("Ticket is 15$")
    print("------------------")