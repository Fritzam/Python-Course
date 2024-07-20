favorite_fruits = ["apples", "grapes", "cherries"]


fruits = ["apples", "bananas", "pears", "cherries", "grapes"]

for fruit in fruits:
    if fruit in favorite_fruits:
        print("Wow, you really like " + fruit + "!")
    else:
        print(fruit + " are okay I guess!")