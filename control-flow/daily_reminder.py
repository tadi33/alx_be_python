task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task and should be completed soon.")
        else:
            print(f"Note: '{task}' is a medium priority task. Complete it when you can.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but should be done eventually.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"'{task}' has an unknown priority. Please check your input.")
