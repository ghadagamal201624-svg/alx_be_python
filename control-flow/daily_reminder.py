task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Address it promptly.")
    case "medium":
        if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
                print(f"Reminder: '{task}' is a medium priority task. Schedule it for this week.")
    case "low":
        if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task with a deadline. Complete when convenient.")
        else:
                print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")