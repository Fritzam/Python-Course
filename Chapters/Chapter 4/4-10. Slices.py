cubes = [number**3 for number in range(1, 11)]
print("The first three items in a list are: " + str(cubes[0:3]))
middleIndex = int((len(cubes)/2) - 1)
print(middleIndex)
print("Three items for the middle are: " + str(cubes[middleIndex: middleIndex + 3]))
print("Three last items are: " + str(cubes[-3:]))