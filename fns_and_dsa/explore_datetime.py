from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print it in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a future date
def calculate_future_date():
    try:
        # Prompt the user to enter the number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date
        future_date = datetime.now() + timedelta(days=number_of_days)
        # Print the future date in "YYYY-MM-DD" format
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

# Main function to execute the tasks
def main():
    display_current_datetime()
    calculate_future_date()

# Run the program
if __name__ == "__main__":
    main()