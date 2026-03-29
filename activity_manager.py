import os
import datetime
from collections import Counter

def add_activity():
    """Add an activity with timestamp and description."""

    day=input("Enter date (YYYY-MM-DD): ")
    time=input("Enter time: ")
    activity=input("Enter activity: ")
    notes=input("Enter notes: ")

    os.makedirs("data", exist_ok=True)
    fname = f"data/{day}.txt"

    entry = f"{time} | {activity} | {notes}"
    
    with open(fname, "a") as file:
        file.write(entry + "\n")
    print(f"Activity saved to {fname}")

def read_activities_daywise(day):
    """Read all activities from a file."""
    fname = f"data/{day}.txt"
    if not os.path.exists(fname):
        print("No activities recorded yet in this file.")
    else:    
        print("Activities:")
        with open(fname, "r") as file:
            for line in file.readlines():
                print(line.strip())

def read_activities():
    """Read all activities from a file."""
      
    print("All Activities: \n")

    for file in os.listdir("data"):
        with open(f"data/{file}", "r") as file:
            print(f"{file.name} - Activities:")
            print("--------------------------")
            for line in file.readlines():
                print(line.strip())
            
            print("\n")
def search_activity(keyword):
    """Search for keyword in activity or description."""
    for file in os.listdir("data"):
        with open(f"data/{file}", "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    #print(f"{file} -> {line.strip()}")
                    print(f"{line.strip()}")

def update_activity(day, lineno, text):
    """Update an activity entry."""
    filename = f"data/{day}.txt"
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    lines[lineno - 1] = text + "\n"

    with open(filename, "w") as file:
        file.writelines(lines)

    print("Activity updated.")

def analyze_activities():
    """Analyze activity frequency across all files."""
    counter = Counter()
    
    for fname in os.listdir("data"):
        if fname.endswith(".txt"):
            with open(f"data/{fname}", "r") as file:
                for line in file:
                    parts = line.split("|")
                    if len(parts) >= 2:
                        activity = parts[1].strip()
                        counter[activity] += 1
    
    print("Activity Frequency Across All Files:")
    for act, count in counter.most_common():
        print(f"{act}: {count}") 
