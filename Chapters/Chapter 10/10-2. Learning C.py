with open('CanInPython') as file:
    print(file.read())
print("----------------------------")
with open('CanInPython') as file:
    for line in file:
        print(line.replace("Python", "C").strip())