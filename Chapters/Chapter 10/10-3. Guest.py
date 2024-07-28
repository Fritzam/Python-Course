print("Hello, please enter Your name dear Guest: ")
name = input("Name: ")

with open('GuestList', 'a') as guestList:
    guestList.write(name)

with open('GuestList') as guestList:
    list = guestList.read()
    print(list)