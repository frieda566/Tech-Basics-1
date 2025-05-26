from sys import argv
import csv
import random

filename = "Technical Basics I_2025 - Sheet1.csv"
students = []
weeks = [f"week{i}" for i in range(1, 14) if i != 6]

# Step 1
def read_csv(filename):
    global students
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            students = list(reader)
            print("✅ File loaded successfully.")
    except FileNotFoundError:
        print("❌ Error: File '{filename}' not found.")
        exit()
    pass

# Step 2
def populate_scores():
    for student in students:
        for week in weeks:
            current_value = student.get(week, '').strip()
            if current_value == '' or current_value == '-':
                student[week] = str(random.randint(0, 3))
            elif not current_value.isdigit():
                student[week] = str(random.randint(0, 3))
    pass

# Step 3
def calculate_all():
    for student in students:
        scores = [student.get(week, '0') for week in weeks]
        student["Total Points"] = calculate_total(scores)
        student["Average Points"] = calculate_average(scores)
    pass

def calculate_total(scores):
    total = 0
    try:
        valid_scores = [int(s) for s in scores if s.strip().isdigit()]
        total = sum(sorted(valid_scores, reverse=True)[:10])
    except:
        total = 0
    return total

def calculate_average(scores):
    average =  0
    try:
        valid_scores = [int(s) for s in scores if s.strip().isdigit()]
        if valid_scores:
            average = round(sum(valid_scores) / len(valid_scores), 2)
    except:
        average = 0
    return average

# After the update let's save the data as a new csv file

def write_csv(filename):
    if not students:
        print("❌ No data to write.")
        return

    fieldnames = list(students[0].keys())

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    pass

# Bonus

def print_analysis():
    # print average scores for stream A, B and every week
    stream_scores = {'A': [], 'B': []}
    week_averages = {week: [] for week in weeks}

    for student in students:
        stream = student.get("Stream", "").strip().upper()
        avg = float(student.get("Average Points", 0))
        if stream in stream_scores:
            stream_scores[stream].append(avg)

        for week in weeks:
            try:
                week_averages[week].append(int(student[week]))
            except:
                continue

    print("\n📊 Average Points by Stream")
    print("-" * 30)
    for stream, scores in stream_scores.items():
        avg = round(sum(scores) / len(scores), 2) if scores else 0
        print(f"Stream '{stream}' has {avg} points.")

    print("\n📅 Average Points by Week")
    print("-" * 30)
    for week in sorted(weeks, key=lambda w: int(w[4:])):
        scores = week_averages[week]
        avg = round(sum(scores) / len(scores), 2) if scores else 0
        print(f"Week '{week}' has {avg} points.")
    pass

if __name__ == "__main__":

    print("Open file:", filename)

    read_csv(filename)

    populate_scores()
    calculate_all()

    user_name = "[Frieda]"

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("🎉New file written:", newname)

    print_analysis()

# Run the file with `python grade_calculator.py sheet.csv`