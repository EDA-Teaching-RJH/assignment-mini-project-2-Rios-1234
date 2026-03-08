import re
import random
import string
from password import Password

class PasswordChecker:
    def __init__(self, history_file="history.txt"):
        # Store the filename where password history will be written.
        # Keeping this as an attribute allows the user to change the file if needed.
        self.history_file = history_file

    def check(self, password: Password) -> dict:
        # Get the raw text of the password from the Password object.
        raw = password.raw
          # Each rule is checked using either length or a regex pattern.
        # The dictionary maps rule names to True/False results.
        rules = {
            "length >= 8": len(raw) >= 8,
            "uppercase letter": bool(re.search(r"[A-Z]", raw)),
            "lowercase letter": bool(re.search(r"[a-z]", raw)),
            "digit": bool(re.search(r"\d", raw)),
            "symbol": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", raw)),
        }

        # Return the dictionary so the caller can inspect each rule.
        return rules

    def score(self, rules: dict) -> int:
        # Convert True/False values into integers and sum them.
        # This gives a score from 0 to 5.
        return sum(rules.values())
         def strength_label(self, score: int) -> str:
        # Convert the numeric score into readable label.
        if score <= 2:
            return "Weak"
        elif score in (3, 4):
            return "Medium"
        else:
            return "Strong"

    def save_to_history(self, password: Password):
        # Append the raw password to the history file.
        # Each password is stored on its own line.
        with open(self.history_file, "a") as f:
            f.write(password.raw + "\n")

