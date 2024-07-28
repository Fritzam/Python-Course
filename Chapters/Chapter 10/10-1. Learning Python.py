with open('CanInPython') as textfile:
    contents = textfile.read()
    print(contents)

print("----------------------------------")

with open('CanInPython') as textfile:
    for line in textfile:
        print(line.strip())

print("----------------------------------")

with open('CanInPython') as textfile:
    contents = textfile.readlines()

for line in contents:
    print(line.strip())