location = []
while True:
    answer = input("Where would You like to go for a vacation? Write 'quit' to leave.")
    if answer == 'quit':
        break
    location.append(answer)

print(location)