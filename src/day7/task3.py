filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print("file doesn't exist yet.")
