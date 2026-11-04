# Students list copied directly from week-4/data/roster.py
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis", "score": 74, "subject": "Data"},
    {"name": "Sara", "score": 91, "subject": "Python"},
    {"name": "Marcus", "score": 68, "subject": "Web"},
    {"name": "Priya", "score": 95, "subject": "Data"},
    {"name": "Devon", "score": 72, "subject": "Python"},
    {"name": "Mia", "score": 83, "subject": "Web"},
    {"name": "Eli", "score": 79, "subject": "Data"}
]

# 1. Find the top scorer
top_name = ""
highest_score = -1
for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_name = student["name"]

# 2. Calculate the class average
total_score = 0
for student in students:
    total_score += student["score"]
class_average = total_score / len(students)

# 3. List all unique subjects using a set
unique_subjects = set()
for student in students:
    unique_subjects.add(student["subject"])

# 4. List high scorers (score > 75) using .append()
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

# Print final results
print(f"Top scorer:       {top_name} ({highest_score})")
print(f"Class average:    {class_average}")
print(f"Subjects offered: {unique_subjects}")
print(f"High scorers:     {high_scorers}")