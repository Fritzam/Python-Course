lista = ["Mysz", "Migu", "Airetab", "Maks", "admin", "Iwona", "Agnieszka", "Agata"]

for user in lista:
    if user == "admin":
        print("Hello admin, would You like a status report?")
    else:
        print("Hello " + user + ", thank You for logging in again!")

sponsors = []
if sponsors:
    for sponsor in sponsors:
        print("Sponsor's name is: " + sponsor)
else:
    print("We need to find some sponsors!")
