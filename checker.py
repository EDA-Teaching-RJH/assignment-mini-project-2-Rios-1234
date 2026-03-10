

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
