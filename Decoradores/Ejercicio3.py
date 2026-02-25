from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year

        # Adjust if your birthday hasn't happened yet this year.
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1

        try:
            if years < 18:
                raise ValueError("User must be at least 18 years old")
        except ValueError as e:
            print(f"Error: {e}")
        print("Access granted" if years >= 18 else "Access denied")
        return years

user = User(date(2015, 1, 1))
print(f"User's age: {user.age} years")
user = User(date(2000, 1, 1))
print(f"User's age: {user.age} years")