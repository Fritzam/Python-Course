from UserClass import User
class Admin(User):

    def __init__(self, first_name, last_name, age, height):
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()

class Privileges:

    def __init__(self):
        self.privileges = ['Can ban users', 'Can create accounts', 'Can modify website', "Can access databases"]

    def list_privileges(self):
        for privilege in self.privileges:
            print(privilege)
