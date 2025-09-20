import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

# ----------------- Grade Mapping -----------------
grade_map = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "E": 0.0
}
grade_options = list(grade_map.keys()) + ["None"]

# ----------------- Subject Data -----------------
subject_data = {
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

semester_order = [
    ("1st Year", "1st Semester"),
    ("1st Year", "2nd Semester"),
    ("2nd Year", "1st Semester"),
    ("2nd Year", "2nd Semester"),
    ("3rd Year", "1st Semester"),
    ("3rd Year", "2nd Semester"),
    ("4th Year", "1st Semester"),
    ("4th Year", "2nd Semester"),
]

semester_frames = {}  # Holds widgets per semester
semester_gpa_labels = {}  # Holds GPA label per semester

# ----------------- Functions -----------------
def calculate_gpa():
    try:
        sem_gpas = []
        for (year, sem), widgets in semester_frames.items():
            sem_points, sem_credits = 0, 0
            for subject_name, credit_label, grade_combo in widgets:
                credit = float(credit_label.cget("text"))
                grade = grade_combo.get()
                if grade == "None" or grade == "":
                    continue
                sem_points += credit * grade_map[grade]
                sem_credits += credit
            sem_gpa = (sem_points / sem_credits) if sem_credits > 0 else 0
            sem_gpas.append(sem_gpa)
            # Update only one label per semester
            semester_gpa_labels[(year, sem)].config(text=f"{sem_gpa:.3f}", fg="green" if sem_gpa>=2 else "red")
        final_gpa = sum(sem_gpas)/len(sem_gpas) if sem_gpas else 0
        label_cum.config(text=f"Final GPA: {final_gpa:.3f}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

def load_semesters():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    semester_frames.clear()
    semester_gpa_labels.clear()
    year = year_combo.get()
    sem = sem_combo.get()
    if not year or not sem:
        messagebox.showerror("Error", "Please select year and semester!")
        return
    target_index = semester_order.index((year, sem))
    for idx in range(target_index + 1):
        y, s = semester_order[idx]
        frame = tk.LabelFrame(scrollable_frame, text=f"{y} - {s}", bg="#f0f0f0", font=("Arial", 11, "bold"))
        frame.pack(fill="x", pady=5, padx=10, anchor="n")
        # Headers
        tk.Label(frame, text="Subject", bg="#f0f0f0", width=35, anchor="w").grid(row=0, column=0, padx=5, pady=2)
        tk.Label(frame, text="Credit", bg="#f0f0f0", width=7).grid(row=0, column=1, padx=5, pady=2)
        tk.Label(frame, text="Grade", bg="#f0f0f0", width=10).grid(row=0, column=2, padx=5, pady=2)
        tk.Label(frame, text="Sem GPA", bg="#f0f0f0", width=10).grid(row=0, column=3, padx=5, pady=2)
        subject_widgets = []
        subjects = subject_data.get((y, s), [])
        for i, (subject, credit) in enumerate(subjects, start=1):
            lbl_subject = tk.Label(frame, text=subject, anchor="w", bg="#f0f0f0", width=35)
            lbl_subject.grid(row=i, column=0, padx=5, pady=2, sticky="w")
            credit_label = tk.Label(frame, text=f"{credit}", bg="#f0f0f0", width=7)
            credit_label.grid(row=i, column=1, padx=5, pady=2)
            grade_combo = ttk.Combobox(frame, values=grade_options, width=10)
            grade_combo.set("None")
            grade_combo.grid(row=i, column=2, padx=5, pady=2)
            subject_widgets.append((subject, credit_label, grade_combo))
        # Empty GPA label for semester
        gpa_label = tk.Label(frame, text="--", bg="#f0f0f0", width=10)
        gpa_label.grid(row=1, column=3, padx=5, pady=2)
        semester_frames[(y, s)] = subject_widgets
        semester_gpa_labels[(y, s)] = gpa_label

def export_results():
    data = {}
    for (year, sem), widgets in semester_frames.items():
        data[f"{year}-{sem}"] = []
        for subject_name, credit_label, grade_combo in widgets:
            data[f"{year}-{sem}"].append({
                "subject": subject_name,
                "credit": credit_label.cget("text"),
                "grade": grade_combo.get()
            })
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Export Successful", "Results exported successfully!")

def import_results():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as f:
            data = json.load(f)
        for (year, sem), widgets in semester_frames.items():
            sem_key = f"{year}-{sem}"
            if sem_key in data:
                for widget, saved in zip(widgets, data[sem_key]):
                    _, _, grade_combo = widget
                    grade_combo.set(saved["grade"])
        messagebox.showinfo("Import Successful", "Results imported successfully!")

def reset_all():
    for widgets in semester_frames.values():
        for _, _, grade_combo in widgets:
            grade_combo.set("None")
    for lbl in semester_gpa_labels.values():
        lbl.config(text="--")
    label_cum.config(text="Final GPA: --")

# ----------------- GUI -----------------
root = tk.Tk()
root.title("🎓 GPA Calculator")
root.geometry("1000x750")
root.configure(bg="#e8f0f2")

# Top Frame
top_frame = tk.Frame(root, bg="#e8f0f2")
top_frame.pack(pady=10)
tk.Label(top_frame, text="Select Year:", bg="#e8f0f2", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
year_combo = ttk.Combobox(top_frame, values=["1st Year","2nd Year","3rd Year","4th Year"], width=12)
year_combo.grid(row=0, column=1, padx=5)
tk.Label(top_frame, text="Select Semester:", bg="#e8f0f2", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5)
sem_combo = ttk.Combobox(top_frame, values=["1st Semester","2nd Semester"], width=12)
sem_combo.grid(row=0, column=3, padx=5)
tk.Button(top_frame, text="Load Semesters", command=load_semesters, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=5)
tk.Button(top_frame, text="Export Results", command=export_results, bg="#FF9800", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=5, padx=5)
tk.Button(top_frame, text="Import Results", command=import_results, bg="#9C27B0", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=6, padx=5)
tk.Button(top_frame, text="Reset All", command=reset_all, bg="#f44336", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=7, padx=5)

# Scrollable Frame
container = tk.Frame(root, bg="#e8f0f2")
container.pack(fill="both", expand=True, padx=10, pady=10)
canvas = tk.Canvas(container, bg="#e8f0f2")
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#e8f0f2")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Bottom GPA Frame
bottom_frame = tk.Frame(root, bg="#e8f0f2")
bottom_frame.pack(pady=10)
tk.Button(bottom_frame, text="Calculate GPA", command=calculate_gpa, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
label_cum = tk.Label(bottom_frame, text="Final GPA: --", font=("Arial", 14, "bold"), fg="#FF5722", bg="#e8f0f2")
label_cum.pack(pady=5)

root.mainloop()
