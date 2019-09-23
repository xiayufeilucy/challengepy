from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.fav_club = []

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)