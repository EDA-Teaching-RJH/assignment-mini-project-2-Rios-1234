

class PasswordChecker:
    def __init__(self, history_file="history.csv"):
        # Store the filename where password history will be saved
        self.history_file = history_file
          # Create the CSV file with headers if it does not already exist.
        # Using mode "x" means: create file, but raise error if it exists.
        try:
            with open(self.history_file, "x", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["password", "score", "label"])
        except FileExistsError:
            # File already exists — nothing to do
            pass
 # Password checker 
    

    def check(self, password: Password) -> dict:
        """
        Check the password against several rules and return a dict of results.
        """
        raw = password.raw   # Extract the raw string from the Password object

        # Dictionary of rules mapped to True/False results
        rules = {
            "length >= 8": len(raw) >= 8,                                        # Check minimum length
            "uppercase letter": bool(re.search(r"[A-Z]", raw)),                  # Contains uppercase
            "lowercase letter": bool(re.search(r"[a-z]", raw)),                  # Contains lowercase
            "digit": bool(re.search(r"\d", raw)),                                # Contains digit
            "symbol": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", raw)),          # Contains symbol
        }

        return rules  # Return the dictionary of rule results

    def score(self, rules: dict) -> int:
        """
        Convert rule results into a numeric score (True=1, False=0).
        """
        return sum(rules.values())  # Sum of booleans gives total score

    def strength_label(self, score: int) -> str:
        """
        Convert the numeric score into a human-readable strength label.
        """
        if score <= 2:          # 0–2 points
            return "Weak"
        elif score in (3, 4):   # 3–4 points
            return "Medium"
        else:                   # 5 points
            return "Strong"
           
    #This is prettry printing 
  

    def pretty_print(self, rules: dict):
        """
        Print each rule and whether it passed.
        """
        print("\nPassword Check Results:")  # Header
        for rule, passed in rules.items():  # Loop through rule dictionary
            print(f"{rule}: {passed}")      # Print rule name and result
