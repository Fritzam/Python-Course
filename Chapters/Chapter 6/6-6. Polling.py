favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['jen', 'robert', 'sarah', 'winston', 'edward', 'phil', 'cassie']
for user in users:
    if user in favorite_languages.keys():
        print("Thank You for taking the poll, " + user.title() + "!")
    else:
        print("Please take the poll, " + user.title() + "!")