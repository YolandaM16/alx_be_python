task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        priority_message = "This is a HIGH-priority task."
    case "medium":
        priority_message = "This is a MEDIUM-priority task."
    case "low":
        priority_message = "This is a LOW-priority task."
    case _:
        priority_message = "Priority not recognized. Treating it as LOW priority."

if time_bound == "yes":
    time_message = "It requires immediate attention today!"
else:
    time_message = "You can schedule this task at your convenience."

print("\n--- Daily Task Reminder ---")
print(f"Task: {task}")
print(priority_message)
print(time_message)

for i in range(3):
    print("Don't forget to complete your task!")
