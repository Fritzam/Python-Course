def print_magicians(list_of_magicians):
    for i in range(len(list_of_magicians)):
        list_of_magicians[i] = list_of_magicians[i] + ' the Great'

    print(list_of_magicians)


magicians = ['Sarah', 'Carrie', 'Jamie', 'Steve']
print_magicians(magicians[:])
print(magicians)