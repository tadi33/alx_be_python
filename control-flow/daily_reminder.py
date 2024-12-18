task = input("enter your task: ")
priority = input("priority(high/medium/low: )")
time_bound = input("is it time_bound?(yes/no: )")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")

    case "low":
        if time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")