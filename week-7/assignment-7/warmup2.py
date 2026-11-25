import csv
import os

file_path = os.path.join("..", "data", "students.csv")

try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['name']}: {row['score']}")
except FileNotFoundError:
    print(f"Error: {file_path} was not found.")