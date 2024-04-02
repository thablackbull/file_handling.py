try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1\n")
        file.write("12345\n")
        file.write("Adding some numbers: 1, 2, 3\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending line 4\n")
        file.write("Another number: 6789\n")
        file.write("Appending some more: 4, 5, 6\n")

except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied to open the file!")
finally:
    print("Execution complete.")
