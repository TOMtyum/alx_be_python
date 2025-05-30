task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please complete it as soon as possible."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that needs to be completed today."
        else:
            reminder += ". Try to finish it this week."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that should be done today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = f"Invalid priority level for task '{task}'."

# Provide a Customized Reminder
print("Reminder:", reminder)

