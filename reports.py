import os

def generate_daily_report(day):
    fname = f"data/{day}.txt"
    
    if not os.path.exists(fname):
        return f"No data for {fname}"
    
    with open(fname, "r") as file:
        activities = [line.strip() for line in file.readlines()]

    report = f"--- Daily Report ({day}) ---\n"
    report += "\n".join(activities)
    return report

def generate_weekly_report(dates):
    report = "--- Weekly Report ---\n\n"
    for d in dates:
        report += generate_daily_report(d) + "\n\n"
    return report
