<<<<<<< HEAD
<<<<<<< HEAD
=======
task = input("Enter the tas description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (ye or no): ").lower()
=======
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
>>>>>>> 6415922f8124fcf5e5c392544de0a85ab0d2c49a

match priority:
    case "high":
        message = "This is a high-priority task."
    case "medium":
        message = "This is a medium-priority task."
    case "low":
<<<<<<< HEAD
>>>>>>> 687aa96f612e2d0bb57f4dfaeabfb43d67303f5c
        message = "This is a low-priority task."
=======
<<<<<<< HEAD
        message = "This is a low-priority task."
=======
        message = "This is low-priority task."
>>>>>>> c2155adfbe21c9fc880b0bade5719b037d4d801d
>>>>>>> 6415922f8124fcf5e5c392544de0a85ab0d2c49a
    case _:
        message = "Invalid priority level. Please enter high, medium, or low."
        print(message)
        exit()
<<<<<<< HEAD

=======
        
>>>>>>> 687aa96f612e2d0bb57f4dfaeabfb43d67303f5c
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
<<<<<<< HEAD
=======

# Step 3: Provide a Customized Reminder
<<<<<<< HEAD
print(f"Task Reminder: {task}")
print(message)
=======
print(f"Task Remindeer: {task}")
print(message)
>>>>>>> c2155adfbe21c9fc880b0bade5719b037d4d801d
<<<<<<< HEAD
>>>>>>> 6415922f8124fcf5e5c392544de0a85ab0d2c49a
=======
>>>>>>> 6415922f8124fcf5e5c392544de0a85ab0d2c49a
>>>>>>> 687aa96f612e2d0bb57f4dfaeabfb43d67303f5c
