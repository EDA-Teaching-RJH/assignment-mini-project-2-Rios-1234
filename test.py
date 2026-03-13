


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
 
    

