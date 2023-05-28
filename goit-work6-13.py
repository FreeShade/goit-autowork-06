import shutil


def create_backup(path, file_name, employee_residence):
    with open(path + "/" + file_name, "wb") as f:
        for key, value in employee_residence.items():
            f.write((key + " " + value + "\n").encode())
    return shutil.make_archive(f"backup_folder", "zip", path)
