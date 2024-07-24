class User:

    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        print("User is named " + self.first_name + " " + self.last_name + ".\nUser is "
              + self.age + " years old and is of " + self.height + " cm height.")

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_logins_attempts(self):
        self.login_attempts = 0


user = User("Michał", "Redacted", "27", "174")
user.greet_user()
user.describe_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_logins_attempts()
print(user.login_attempts)
