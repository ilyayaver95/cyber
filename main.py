
input_path = input("Enter path ")
directory = input_path + "\Empty_file.txt"

if "DoNotCopy" in input_path:
    print("Nice try")
    exit(0)
with open(directory, "w") as file:
    file.write("")

print(f"The path is {input_path}")