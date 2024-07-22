def build_profile(first_name, last_name, **traits):
    person = {'First Name': first_name, 'Last Name': last_name}
    for name, trait in traits.items():
        person[name] = trait

    return person


print(build_profile("Michał", "Fritza", Specialization='DevSecOps', Favorite_Cuisine='Asian',
              Favorite_animals='Love all of them, no exceptions!'))
