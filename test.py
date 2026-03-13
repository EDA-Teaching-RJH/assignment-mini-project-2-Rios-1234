


def test_check_all_rules_pass():
    # Use a separate test CSV file so we don't affect real history
    checker = PasswordChecker("test_history.csv")

    # This password satisfies all rules
    pwd = Password("Aa1!aaaa")

    # Run rule checks
    rules = checker.check(pwd)

    # Assert each rule individually
    assert rules["length >= 8"] is True
    assert rules["uppercase letter"] is True
    assert rules["lowercase letter"] is True
    assert rules["digit"] is True
    assert rules["symbol"] is True
    def test_score():
    # Test scoring logic with a mix of passing/failing rules
    checker = PasswordChecker("test_history.csv")

    rules = {
        "length >= 8": True,
        "uppercase letter": True,
        "lowercase letter": True,
        "digit": False,
        "symbol": False,
    }

    # Expect 3 passing rules
    assert checker.score(rules) == 3
    def test_strength_label():
    # Ensure score → label mapping works correctly
    checker = PasswordChecker("test_history.csv")

    assert checker.strength_label(1) == "Weak"
    assert checker.strength_label(3) == "Medium"
    assert checker.strength_label(5) == "Strong"


def test_generate_random_password():
    # Test that generated passwords meet minimum requirements
    checker = PasswordChecker("test_history.csv")
    pwd = checker.generate_random_password()

    # Length requirement
    assert len(pwd) == 12

    # Character-type requirements
    assert any(c.isupper() for c in pwd)
    assert any(c.islower() for c in pwd)
    assert any(c.isdigit() for c in pwd)
    assert any(c in "!@#$%^&*(),.?\":{}|<>" for c in pwd)
    # CSV HISTORY TESTS
# These tests ensure that saving, clearing, and reading
# password history works correctly.


def test_save_to_history_creates_csv():
    filename = "test_history.csv"

    # Remove old test file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    checker = PasswordChecker(filename)

    # Save a password entry
    checker.save_to_history(Password("Test123!"), 5, "Strong")

    # CSV file should now exist
    assert os.path.exists(filename)

    # Read CSV contents
    with open(filename, "r") as f:
        rows = list(csv.reader(f))

    # First row = header
    assert rows[0] == ["password", "score", "label"]

    # Second row = saved password
    assert rows[1] == ["Test123!", "5", "Strong"]
 
    

