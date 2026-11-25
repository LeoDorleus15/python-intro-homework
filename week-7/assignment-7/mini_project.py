import csv
import os
from datetime import datetime

# Build portable path and verify the file exists before opening
expenses_path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(expenses_path):
    print(f"Error: {expenses_path} not found. Stopping program.")
    exit()

# Load all rows into memory as a list of dictionaries
with open(expenses_path, "r") as file:
    records = list(csv.DictReader(file))

# Convert numeric string fields to float
for item in records:
    item["amount"] = float(item["amount"])

# Filter to only rows where category is "Food"
target_category = "Food"
filtered_expenses = [
    item for item in records if item["category"] == target_category
]

# Calculate total amount spent
total_spent = sum(item["amount"] for item in filtered_expenses)

# Format today's date
today_str = datetime.now().strftime("%B %d, %Y")

# Write the formatted report to food_report.txt
output_filename = f"{target_category.lower()}_report.txt"

with open(output_filename, "w") as report_file:
    report_file.write(f"{target_category} Expense Report — generated {today_str}\n")
    for item in filtered_expenses:
        report_file.write(f"{item['date']}: ${item['amount']:.2f}\n")
    report_file.write(f"Total: ${total_spent:.2f}\n")

print(f"Report saved to {output_filename}")