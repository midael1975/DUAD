user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        global user_logged_in
        if user_logged_in == False:
            print("Error: unauthenticated user")
            return None
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Viewing profile...")

user_logged_in = True
view_profile()
user_logged_in = False
view_profile()

