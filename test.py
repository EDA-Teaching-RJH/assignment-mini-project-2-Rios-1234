


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
