# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the Task Based on Priority using if/elif/else (compatible with all Python 3)
if priority == "high":
    reminder = f"'{task}' is a high priority task."
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task."
elif priority == "low":
    reminder = f"'{task}' is a low priority task."
else:
    reminder = f"'{task}' has an unknown priority level."

# Modify based on time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Provide a Customized Reminder (must match checker requirement)
print(f"Reminder: {reminder}")

