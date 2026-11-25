import os

file_path = os.path.join("..", "data", "notes.txt")

try:
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: {file_path} was not found.")