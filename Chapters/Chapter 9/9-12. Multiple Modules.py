from PrivilegesAdminClass import Privileges, Admin, User

admin = Admin('Michal', 'Redacted', '27', '184')
admin.greet_user()
admin.describe_user()
admin.privileges.list_privileges()
