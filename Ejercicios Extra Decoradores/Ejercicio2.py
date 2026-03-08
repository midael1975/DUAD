user_logged_in = False

class NotAuthenticatedError(Exception):
    pass

def requires_login(func):
    def wrapper(*args, **kwargs):
        global user_logged_in
        if not user_logged_in:
            raise NotAuthenticatedError("User must be logged in to access this function")
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Viewing profile...")

user_logged_in = True
view_profile()
user_logged_in = False
try:
    view_profile()
except NotAuthenticatedError as e:
    print("Error:", e)

