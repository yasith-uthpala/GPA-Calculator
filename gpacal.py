
grade_map = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "E": 0.0
}


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


def main():
    print("GPA Calculator CLI")
    print("This tool will calculate GPA for university students.\n")

    # Temporary test data
    grades = ["A", "B+"]
    credits = [3, 3]

    gpa = calculate_gpa(grades, credits)
    print("Sample GPA:", round(gpa, 3))
    print("Degree Class:", get_degree_class(gpa))


if __name__ == "__main__":
    main()
