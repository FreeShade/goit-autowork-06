def read_employees_from_file(path):
    f = open(path, "r")
    employee = []
    try:
        for line in f:
            employee.append(line.strip())
    finally:
        f.close()
    return employee
