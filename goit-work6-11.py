def get_credentials_users(path):
    with open(path, "rb") as file:
        lines = [line.decode("utf-8").strip() for line in file]
    return lines
