def check_email(string):
    if " " not in string and '@' in string and '@.' not in string:
        return string.rfind('.') > string.index('@')
    return False
