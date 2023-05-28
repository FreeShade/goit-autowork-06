def save_applicant_data(source, output):
    with open(output, "w") as output_file:
        for apl in source:
            name = apl["name"]
            spetiality = str(apl["speciality"])
            math_score = str(apl["math"])
            lang_score = str(apl["lang"])
            eng_score = str(apl["eng"])
            line = f"{name},{specialty},{math_score},{lang_score},{eng_score}\n"
            output_file.write(line)
