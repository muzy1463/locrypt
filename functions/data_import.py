import os


def data_importer(input_text, output_text, algorithm, key=None, direction=1):
    if direction == 1:
        method = "Encryption"
    else:
        method = "Decryption"

    cwd = os.getcwd()
    file_code = 1

    while os.path.exists(f"{cwd}\\docs\\LoCrypt - {file_code}.txt") is True:
        file_code += 1

    with open(f"{cwd}\\docs/LoCrypt - {file_code}.txt", "w") as document:
        document.write("*" * 100)
        document.write("\n" * 2)
        document.write("LoCrypt App" + "\n"*2)
        document.write("*" * 100 + "\n"*2)
        document.write(f"The method used is {algorithm} {method}" + "\n"*2)
        document.write("Input: " + "\n")
        document.write(input_text + "\n"*2)
        document.write("Output: " + "\n")
        document.write(output_text + "\n"*2)

        if key:
            document.write("The key: " + "\n")

            for i, j in key.items():
                x = i + ": " + j
                document.write(x + "\n")
