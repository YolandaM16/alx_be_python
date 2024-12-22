task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

match priority:
    case "high":
        reminder ="This is a high-priority task."
    case "medium":
        reminder = "This is a medium-priority task."
    case "low":
        reminder = "This is a low-priority task."
    case _:
        reminder = "Priority not recognized. "

if time_bound == "yes":
    reminder += "It requires immediate attention today!"
else:
    reminder += "You can reschedule it flexibly."

print(f"\nReminder: {task}")
print(reminder)
