class Password:
    def __init__(self, raw: str):
        # Store the raw password text exactly as the user typed it.
        # This keeps the Password object simple and focused on holding data.
        self.raw = raw

    def __repr__(self):
        # Return a developer-friendly string representation of the object.
        # This is useful when printing Password objects during debugging,
        # logging, or when pytest shows assertion failures.
        return f"Password(raw='{self.raw}')"
