with open('GuestList', 'a') as listOfGuests:
    while True:
        value = input("Input Your name Dear Guests, type 'q' at any"
                      "time to end the prompt.")
        if value == 'q':
            break

        listOfGuests.write(value + '\n')
with open('GuestList') as listOfGuests:
    print(listOfGuests.read())