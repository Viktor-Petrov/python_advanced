import os

while True:
    command, *info = input().split("-")

    if command == "End":
        break

    elif command == "Create":
        file = open(f"files/{info[0]}", "w")
        file.close()

    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r") as file:
                text = file.read()
            text = text.replace(info[1], info[2])

            with open(f"files/{info[0]}", "w") as file:
                file.write(text)
        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred!")
