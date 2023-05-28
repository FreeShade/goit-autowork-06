def save_credentials_users(path, users_info):
    with open(path, "wb") as fh:
        for username, password in users_info.items():
            credentials = f"{username}:{password}\n"
            fh.write(credentials.encode("utf-8"))
