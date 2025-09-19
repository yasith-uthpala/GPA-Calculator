import tkinter as tk
from tkinter import ttk, messagebox

# Grade to GPA mapping
grade_map = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "E": 0.0
}

semester_order = [
    ("1st Year", "1st Semester"),
    ("1st Year", "2nd Semester"),
    ("2nd Year", "1st Semester"),
    ("2nd Year", "2nd Semester"),
    ("3rd Year", "1st Semester"),
    ("3rd Year", "2nd Semester"),
    ("4th Year", "1st Semester"),
    ("4th Year", "2nd Semester")
]

semester_frames = {}

def calculate_gpa():
    try:
        total_points = 0
        total_credits = 0
        for (year, sem), widgets in semester_frames.items():
            sem_points = 0
            sem_credits = 0
            for subject_entry, credit_entry, grade_combo in widgets:
                if not credit_entry.get() or not grade_combo.get():
                    continue
                credit = float(credit_entry.get())
                grade = grade_combo.get()
                if grade not in grade_map:
                    messagebox.showerror("Error", f"Invalid grade for {subject_entry.get()}")
                    return
                sem_points += credit * grade_map[grade]
                sem_credits += credit
            total_points += sem_points
            total_credits += sem_credits
        cum_gpa = total_points / total_credits if total_credits > 0 else 0
        label_cum.config(text=f"Cumulative GPA: {cum_gpa:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

def load_semesters():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    semester_frames.clear()

    year = year_combo.get()
    sem = sem_combo.get()
    if not year or not sem:
        messagebox.showerror("Error", "Please select year and semester!")
        return

    target_index = semester_order.index((year, sem))
    
    for idx in range(target_index + 1):
        y, s = semester_order[idx]
        frame = tk.LabelFrame(scrollable_frame, text=f"{y} - {s}")
        frame.pack(fill="x", pady=5, padx=10)

        # Ask user how many subjects in this semester
        tk.Label(frame, text="Number of Subjects:").grid(row=0, column=0, padx=5, pady=5)
        num_subjects_var = tk.StringVar()
        num_subjects_entry = tk.Entry(frame, width=5, textvariable=num_subjects_var)
        num_subjects_entry.grid(row=0, column=1, padx=5, pady=5)

        def create_subject_rows(entry_var=num_subjects_var, frame=frame, y=y, s=s):
            try:
                for widget_row in frame.grid_slaves():
                    if int(widget_row.grid_info()["row"]) > 0:  # remove previous rows
                        widget_row.destroy()
                n = int(entry_var.get())
                subject_widgets = []
                for i in range(n):
                    tk.Label(frame, text=f"Subject {i+1}").grid(row=i+1, column=0, padx=5, pady=5)
                    subject_entry = tk.Entry(frame, width=15)
                    subject_entry.grid(row=i+1, column=1, padx=5, pady=5)

                    credit_entry = tk.Entry(frame, width=5)
                    credit_entry.grid(row=i+1, column=2, padx=5, pady=5)

                    grade_combo = ttk.Combobox(frame, values=list(grade_map.keys()), width=5)
                    grade_combo.grid(row=i+1, column=3, padx=5, pady=5)

                    subject_widgets.append((subject_entry, credit_entry, grade_combo))

                semester_frames[(y, s)] = subject_widgets
            except:
                messagebox.showerror("Error", "Please enter a valid number of subjects")

        btn_create = tk.Button(frame, text="Set Subjects", command=create_subject_rows)
        btn_create.grid(row=0, column=2, padx=5, pady=5)

# Main window
root = tk.Tk()
root.title("GPA Calculator")
root.geometry("650x600")

# Year/Sem selection
tk.Label(root, text="Select Year:").pack(pady=5)
year_combo = ttk.Combobox(root, values=["1st Year", "2nd Year", "3rd Year", "4th Year"])
year_combo.pack(pady=5)

tk.Label(root, text="Select Semester:").pack(pady=5)
sem_combo = ttk.Combobox(root, values=["1st Semester", "2nd Semester"])
sem_combo.pack(pady=5)

btn_load = tk.Button(root, text="Load Semesters", command=load_semesters)
btn_load.pack(pady=10)

# Scrollable frame setup
container = tk.Frame(root)
container.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Calculate + result
btn_calc = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
btn_calc.pack(pady=10)

label_cum = tk.Label(root, text="Cumulative GPA: --", font=("Arial", 14), fg="blue")
label_cum.pack(pady=5)

root.mainloop()
