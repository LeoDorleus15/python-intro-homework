from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%B %d, %Y")
print(f"Today is {formatted_date}.")