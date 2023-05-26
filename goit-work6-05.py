def get_cats_info(path):
    try:
        cats = []
        with open(path, "r") as file:
            for line in file:
                line = line.strip().split(",")
                dictionary = {"id": line[0], "name": line[1], "age": line[2]}

                cats.append(dictionary)
            return cats
    except:
        print("Fail")
