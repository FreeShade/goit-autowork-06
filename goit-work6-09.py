def is_equal_string(utf8_string, utf16_string):
    try:
        utf8_encoded = utf8_string.decode("utf-8")
        utf16_encoded = utf16_string.decode("utf-16")

        if utf8_encoded == utf16_encoded:
            return True
        else:
            return False
    except UnicodeError:
        return False
