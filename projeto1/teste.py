import re

def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if re.match(pattern, email):
        return True
    return False