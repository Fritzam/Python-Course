current_users = ["laki", "pszemo823", "luffy", "ktoś", "jajestemadmin"]
new_users = ["Czaki", "Luffy", "pszemo823", "Ryś", "Hefajstos", "Ktoś"]

for user in new_users:
    if user.lower() in current_users:
        print("Username " + user + " is already taken. Please enter another name.")
    else:
        print("Username " + user + " is available.")