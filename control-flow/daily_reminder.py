<<<<<<< HEAD
# Step 1: Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no) ").lower()
=======
#step 1: Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()
>>>>>>> c2155adfbe21c9fc880b0bade5719b037d4d801d

# Step 2: Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        message = "This is a high-priority task."
    case "medium":
        message = "This is a medium-priority task."
    case "low":
<<<<<<< HEAD
        message = "This is a low-priority task."
=======
        message = "This is low-priority task."
>>>>>>> c2155adfbe21c9fc880b0bade5719b037d4d801d
    case _:
        message = "Invalid priority level. Please enter high, medium, or low."
        print(message)
        exit()

# Add time sensitivity details
if time_bound == "yes":
<<<<<<< HEAD
    message += " It requires immediate attention today!"
elif time_bound == "no":
    message += " It can be scheduled for later."
=======
    message += "It requires immediate attention today!"
elif time_bound == "no":
    message += "It can be scheduled for later."
>>>>>>> c2155adfbe21c9fc880b0bade5719b037d4d801d
else:
    print("Invalid input for time sensitivity. Please enter yes or no.")
    exit()

# Step 3: Provide a Customized Reminder
<<<<<<< HEAD
print(f"Task Reminder: {task}")
print(message)
=======
print(f"Task Remindeer: {task}")
print(message)
>>>>>>> c2155adfbe21c9fc880b0bade5719b037d4d801d
