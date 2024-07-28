with open("reasonsToEnjoyProgramming.txt", 'a') as reasons:
    while True:
        reason = input("Why do you enjoy programming? Type 'q' to quit")
        if reason == 'q':
            break
        reasons.write(reason + '\n')

with open('reasonsToEnjoyProgramming.txt') as reasons:
    print(reasons.read().strip(), end='')