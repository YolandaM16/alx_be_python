task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

match priority:
    case "high":
<<<<<<< HEAD
        reminder = "This is a high-priority task. "
    case "medium":
        reminder = "This is a medium-priority task. "
    case "low":
        reminder = "This is a low-priority task. "
=======
        reminder ="This is a high-priority task."
    case "medium":
        reminder = "This is a medium-priority task."
    case "low":
        reminder = "This is a low-priority task."
>>>>>>> 6ea61ac750a233584f3480608b0de13d3f05d780
    case _:
        reminder = "Priority not recognized. "

if time_bound == "yes":
    reminder += "It requires immediate attention today!"
else:
<<<<<<< HEAD
    reminder += "You can schedule it flexibly."
=======
    reminder += "You can reschedule it flexibly."
>>>>>>> 6ea61ac750a233584f3480608b0de13d3f05d780

print(f"\nReminder: {task}")
print(reminder)
