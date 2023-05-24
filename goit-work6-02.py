def write_employees_to_file(employee_list, path):
    file = open(path, "w")
    try:
        for item in employee_list:
            for employee in item:
                file.write(employee + "\n")
    finally:
        file.close()
