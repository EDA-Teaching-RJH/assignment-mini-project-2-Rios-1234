import re
from password import Password

class PasswordChecker:
    def __init__(self, history_file="history.txt"):
        # Store the filename where password history will be written.
        # Keeping this as an attribute allows the user to change the file if needed.
        self.history_file = history_file

    def check(self, password: Password) -> dict:
        # Get the raw text of the password from the Password object.
        raw = password.raw
