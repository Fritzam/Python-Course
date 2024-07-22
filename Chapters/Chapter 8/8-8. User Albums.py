def make_album():
    dictionary = {}
    while True:
        print("Input 'q' at any time to quit.")
        artists_name = input("Please input artist's name:")
        if artists_name == 'q':
            break
        album_title = input("Please input album title: ")
        if album_title == 'quit':
            break
        dictionary[artists_name] = album_title
    return dictionary


print(make_album())
