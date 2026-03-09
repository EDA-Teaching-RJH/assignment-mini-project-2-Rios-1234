
def main():
    # Create a PasswordChecker instance to handle all password logic
    checker = PasswordChecker()

    # command line mode (sys.argv)
   
    # If the user provided command-line arguments, handle them here
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()  # First argument = command

        # Show password history
        if cmd == "history":
            cowsay.stegosaurus("Showing password history!")
            checker.view_history()
            return

        # Generate a random password
        elif cmd == "generate":
            cowsay.dragon("Generating a mighty password!")
            pwd = checker.generate_random_password()
            print(f"Generated password: {pwd}")

            # Save generated password as strong by default
            checker.save_to_history(Password(pwd), 5, "Strong")
            return

        # Check a password directly from the command line
        elif cmd == "check":
            # Must include a password argument
            if len(sys.argv) < 3:
                print("Usage: python main.py check <password>")
                return

            raw = sys.argv[2]
            pwd = Password(raw)
