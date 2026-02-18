from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def has_permissions(self, permission):
        pass

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def has_permissions(self, permission):
        return True

    def get_role(self):
        return "Admin"

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.allowed_permissions = {"read"}

    def has_permissions(self, permission):
        return permission in self.allowed_permissions

    def get_role(self):
        return "Regular User"

# Example usage:
admin = Admin("Alice")
regular_user = RegularUser("Bob")

print(f"Admin {admin.name} has permission 'read': {admin.has_permissions('read')}")
print(f"Regular user {regular_user.name} has permission 'read': {regular_user.has_permissions('write')}")
print(f"Admin role: {admin.get_role()}")
print(f"Regular user role: {regular_user.get_role()}")