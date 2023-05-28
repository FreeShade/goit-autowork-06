def sanitize_file(source, output):
    with open(source, "r") as file:
        content = file.read()
        sanitized_content = "".join(char for char in content if not char.isdigit())

    with open(output, "w") as file2:
        file2.write(sanitized_content)
