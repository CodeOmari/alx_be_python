
task = input("Enter your task: ").strip()

priority = input("Priority (high/medium/low): ").strip().lower()

while priority not in ['high', 'medium', 'low']:
    print("Please enter a valid priority: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

while time_bound not in ['yes', 'no']:
    print("Please enter 'yes' or 'no'.")
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case 'high':
        message = f"'{task}' is a high priority task"
    case 'medium':
        message = f"'{task}' is a medium priority task"
    case 'low':
        message = f"'{task}' is a low priority task"

if time_bound == 'yes':
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."


print(f"Reminder: {message}")
