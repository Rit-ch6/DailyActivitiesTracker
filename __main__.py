from activity_manager import add_activity, analyze_activities, read_activities, search_activity, update_activity
from reports import generate_daily_report, generate_weekly_report
from datetime import date, datetime, timedelta

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
            from_date=input("Enter start date (YYYY-MM-DD): ")
            from_date_object = datetime.strptime(from_date, "%Y-%m-%d").date()
            to_date=input("Enter end date (YYYY-MM-DD): ")
            to_date_object = datetime.strptime(to_date, "%Y-%m-%d").date()

            date_list = []
            current = from_date_object
            while current <= to_date_object:
                date_list.append(current)
                current += timedelta(days=1)   
            print(generate_weekly_report(date_list))
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
