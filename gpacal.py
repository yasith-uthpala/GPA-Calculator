# ----------------- Grade Mapping -----------------
grade_map = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "E": 0.0
}

# ----------------- ICT Degree Data -----------------
ict_subjects = {
    ("1st Year", "1st Semester"): [
        ("Workshop Practice", 1),
        ("Basic Mathematics", 2),
        ("Physics", 3),
        ("Essentials ICT and Social Computing", 1),
        ("Introduction to Computer Systems and Operating Systems", 2),
        ("Application Laboratory I", 3),
        ("Programming I", 3),
    ],
    ("1st Year", "2nd Semester"): [
        ("Technology and Historical Transformation", 1),
        ("Computer Applications", 2),
        ("Information System Modeling", 2),
        ("Web Application Development", 2),
        ("Application Laboratory II", 3),
        ("Database Management Systems I", 3),
        ("Object Oriented Programming", 3),
    ],
    ("2nd Year", "1st Semester"): [
        ("Management of Technology", 2),
        ("Database Management Systems II", 2),
        ("Discrete Mathematics", 2),
        ("IT project Management", 2),
        ("Software Engineering", 2),
        ("Multimedia and Web Design", 3),
        ("Computer Networks", 3),
    ],
    ("2nd Year", "2nd Semester"): [
        ("Statistical Data Analysis", 2),
        ("IT Systems Acquisition", 2),
        ("Agile Software Development", 3),
        ("Graphic Design and Creative Development", 3),
        ("Mobile Application Development", 3),
        ("Programming II", 3),
    ],
    ("3rd Year", "1st Semester"): [
        ("Enterprise Resource Planning Systems", 2),
        ("ICT Innovation", 2),
        ("Information Systems Management", 2),
        ("Introduction to Software Quality Assurance", 2),
        ("Introduction to Information Systems Security", 2),
        ("Professional Practice in ICT", 2),
        ("Bioinformatics", 2),
        ("Introduction to GIS and Remote Sensing", 3),
    ],
    ("3rd Year", "2nd Semester"): [
        ("Development Economics", 1),
        ("Environmental Law", 2),
        ("Occupational Health and Safety", 2),
        ("Sociology and Values for a Technological Society", 2),
        ("Internship/ Industrial Training", 6),
    ],
    ("4th Year", "1st Semester"): [
        ("Intellectual Property Rights", 1),
        ("Innovation and Entrepreneurship", 2),
        ("Digital Forensics", 2),
        ("Selected Topics in ICT", 2),
        ("Data Analytics and Business Intelligence", 3),
        ("Programming III", 3),
        ("Systems and Network Administration", 3),
    ],
    ("4th Year", "2nd Semester"): [
        ("Human Computer Interaction", 3),
        ("Software Quality Management and Test Automation", 3),
        ("Individual/Group Project", 8),
    ],
}

# ----------------- GPA Logic -----------------
def calculate_gpa(grades, credits):
    total_points = 0
    total_credits = 0

    for i in range(len(grades)):
        grade = grades[i]
        credit = credits[i]

        if grade in grade_map:
            total_points += grade_map[grade] * credit
            total_credits += credit

    if total_credits == 0:
        return 0.0

    return total_points / total_credits


def get_degree_class(gpa):
    if gpa >= 3.7:
        return "First Class"
    elif gpa >= 3.3:
        return "Second Upper Class"
    elif gpa >= 3.0:
        return "Second Lower Class"
    else:
        return "No Class"


def choose_option(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print("Invalid choice, try again.")


# ----------------- Main Program -----------------
def main():
    print("GPA Calculator CLI - ICT Degree")
    print("-------------------------------\n")

    # 1) Ask for Year
    years = sorted(set(year for (year, sem) in ict_subjects.keys()))
    year = choose_option("Select Year:", years)

    #Ask for Semester 
    sems_for_year = sorted(set(sem for (y, sem) in ict_subjects.keys() if y == year))
    semester = choose_option("Select Semester:", sems_for_year)

    key = (year, semester)
    if key not in ict_subjects:
        print("No subjects found for that selection.")
        return

    subjects = ict_subjects[key]

    print(f"\nLoading subjects for {year} - {semester}...\n")

    grades = []
    credits = []

    for name, credit in subjects:
        grade = input(f"{name} ({credit} credits): ").strip().upper()
        grades.append(grade)
        credits.append(credit)

    gpa = calculate_gpa(grades, credits)

    print("\n----------------- RESULT -----------------")
    print(f"Year / Semester : {year} - {semester}")
    print("Final GPA       :", round(gpa, 3))
    print("Degree Class    :", get_degree_class(gpa))


if __name__ == "__main__":
    main()
