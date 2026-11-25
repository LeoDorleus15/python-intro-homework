# Keep validation logic in one function so you can reuse it cleanly:

def is_valid_score(score):
    if isinstance(score, bool) or not isinstance(score, int):
        return False
    return 0 <= score <= 100


score = int(input("Enter a score (0-100): "))

if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")