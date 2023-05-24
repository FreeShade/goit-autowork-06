def total_salary(path):
    file = open(path, "r")
    number_list = file.readlines()
    file.close()

    total = 0
    for line in number_list:
        line = line.strip()
        name, salary = line.split(",")
        salary = float(salary)
        total += salary
    return total
