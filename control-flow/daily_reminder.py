# Step 1: Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no) ").lower()

# Step 2: Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        message = "This is a high-priority task."
    case "medium":
        message = "This is a medium-priority task."
    case "low":
        message = "This is a low-priority task."
    case _:
        message = "Invalid priority level. Please enter high, medium, or low."
        print(message)
        exit()

# Add time sensitivity details
if time_bound == "yes":
    message += " It requires immediate attention today!"
elif time_bound == "no":
    message += " It can be scheduled for later."
else:
    print("Invalid input for time sensitivity. Please enter yes or no.")
    exit()

# Step 3: Provide a Customized Reminder
print(f"Task Reminder: {task}")
print(message)