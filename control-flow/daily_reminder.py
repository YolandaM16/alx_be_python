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
>>>>>>> 6415922f8124fcf5e5c392544de0a85ab0d2c49a