
def test_cli_check(capsys):
    # Simulate: python main.py check Aa1!aaaa
    sys.argv = ["main.py", "check", "Aa1!aaaa"]

    main.main()

    output = capsys.readouterr().out

    # Should print the cowsay message for check results
    assert "Password check results!" in output
