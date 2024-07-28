with open('Alice.txt', encoding='UTF-8') as Alice:
    contents = Alice.read().lower()
    timesAliceIsUsed = contents.count('alice')
    theIsUsed = contents.count('the')
    print("'Alice' is mentioned: " + str(timesAliceIsUsed) + " times.")
    print("'The' is mentioned: " + str(theIsUsed) + " times.")