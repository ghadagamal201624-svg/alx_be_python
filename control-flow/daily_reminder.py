task = input("Enter your taske:")
priority = input("Enter the priority level (high, medium, low):")
time_bound= input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Address it promptly.")
    case "medium":
        if time_bound == "yes":
                print(f"'{task}' is a medium priority task that should be completed today.")
        else:
                print(f"'{task}' is a medium priority task. Schedule it for this week.")
    case "low":
        if time_bound == "yes":
                print(f"'{task}' is a low priority task with a deadline. Complete when convenient.")
        else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
