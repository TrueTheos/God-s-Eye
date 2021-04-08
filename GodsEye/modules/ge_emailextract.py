import re

def validEmail(email):
    if "@" not in email:
        return False

    if not re.match(r'^([\%a-zA-Z\.0-9_\-\+]+@[a-zA-Z\.0-9\-]+\.[a-zA-Z\.0-9\-]+)$', email):
        return False

    if len(email) < 6:
        return False

    # Skip strings with messed up URL encoding
    if "%" in email:
        return False

    # Skip strings which may have been truncated
    if "..." in email:
        return False

    return True

def extractEmails(data):
    emails = set()

    matches = re.findall(r'([\%a-zA-Z\.0-9_\-\+]+@[a-zA-Z\.0-9\-]+\.[a-zA-Z\.0-9\-]+)', data)

    for match in matches:
        if validEmail(match):
            emails.add(match)

    return list(emails)