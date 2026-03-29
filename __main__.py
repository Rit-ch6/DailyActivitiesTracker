from activity_manager import add_activity, analyze_activities, read_activities, search_activity, update_activity
from reports import generate_daily_report, generate_weekly_report

def menu():
    while True:
        print("\n--- Activity File Manager ---")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. Search Activity")
        print("4. Update Activity")
        print("5. Analyze All Files")
        print("6. Generate Daily Report")
        print("7. Generate Weekly Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_activity()
        elif choice == "2":
            read_activities()
        elif choice == "3":            
            keyword = input("Enter keyword to search: ")
            search_activity(keyword)
        elif choice == "4":
            day=input("Enter date (YYYY-MM-DD): ")
            lineno=int(input("Enter Line Number: "))
            text=input("Enter new test (time(hh:mm) | activity | description) format: ")
            update_activity(day, lineno, text)
        elif choice == "5":
            analyze_activities()
        elif choice == "6":
            day=input("Enter date (YYYY-MM-DD): ")
            print(generate_daily_report(day))
        elif choice == "7":
            dates=["2026-03-27", "activities_2026-03-27"]
            print(generate_weekly_report(dates))
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
