# Ask the user for the day and time of day, and normalize the input to lowercase
day = input("What day is it? ").strip().lower()
time_of_day = input("What time of day? ").strip().lower()

# Define valid days and times for validation
valid_days = ["monday", "wednesday", "saturday"]
valid_times = ["morning", "afternoon", "evening"]

# Check if both day and time are valid
if day not in valid_days:
    print(f"Sorry, I don't recognize that day. Try: Monday, Wednesday, Saturday")
elif time_of_day not in valid_times:
    print(f"Sorry, I don't recognize that time. Try: morning, afternoon, evening")
else:
    # 3 Days x 3 Times = 9 Combinations
    if day == "monday":
        if time_of_day == "morning":
            print("Suggestion: Morning Python review and coffee — great way to kick off the week!")
        elif time_of_day == "afternoon":
            print("Suggestion: Tackle your work tasks and check your GitHub pull requests.")
        elif time_of_day == "evening":
            print("Suggestion: Go for a steady ride on the stationary bike to unwind.")
            
    elif day == "wednesday":
        if time_of_day == "morning":
            print("Suggestion: Mid-week coding session and reviewing data structures.")
        elif time_of_day == "afternoon":
            print("Suggestion: Work on technical documentation or study cloud architecture.")
        elif time_of_day == "evening":
            print("Suggestion: Prepare a high-protein smoothie and prep ingredients for dinner.")
            
    elif day == "saturday":
        if time_of_day == "morning":
            print("Suggestion: Sleep in a bit, then enjoy a relaxed breakfast and coffee.")
        elif time_of_day == "afternoon":
            print("Suggestion: Go to the gym or handle some errands.")
        elif time_of_day == "evening":
            print("Suggestion: Perfect night for a movie or trying a new recipe.")