task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority. Please check your input."


if time_bound == "yes" and priority == "high":
    reminder += " that requires immediate attention today!"
elif time_bound == "yes":
    reminder += " and should be completed soon."
else:
    reminder += ". Consider completing it when you have free time."


print("\n" + reminder)

