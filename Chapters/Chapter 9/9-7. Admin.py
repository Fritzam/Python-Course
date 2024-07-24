class User:

    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        print("User is named " + self.first_name + " " + self.last_name + ".\nUser is "
              + self.age + " years old and is of " + self.height + " cm height.")

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)


class Admin(User):

    def __init__(self, first_name, last_name, age, height):
        super().__init__(first_name, last_name, age, height)
        self.privileges = ['Can ban users', 'Can create accounts', 'Can modify website', "Can access databases"]

    def list_privileges(self):
        for privilege in self.privileges:
            print(privilege)

user = User("Michał", "Redacted", "27", "174")
user.greet_user()
user.describe_user()
admin = Admin("John", 'Wayne', '40', '183')
admin.describe_user()
admin.greet_user()
admin.list_privileges()

