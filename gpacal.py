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

# ----------------- Department & Subject Data -----------------
departments = {
    "Bachelor of Information and Communication Technology Honours": {
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
    },
    "Bachelor of Biosystems Technology Honours in Agriculture": {
        ("1st Year", "1st Semester"): [
            ("Integrated English Language Skills for Technology (I)", 1),
            ("Workshop Practice", 1),
            ("Basic Mathematics", 2),
            ("Chemistry", 2),
            ("Physics", 3),
            ("Introduction to Hydrology", 2),
            ("Principles of Agronomy", 1),
            ("Introduction to Farming Systems", 2),
            ("Biology", 3),
        ],
        ("1st Year", "2nd Semester"): [
            ("Integrated English Language Skills for Technology (II)", 1),
            ("Technology and Historical Transformation", 1),
            ("Computer Applications", 2),
            ("Basic Soil Science", 2),
            ("Farm Tractors", 1),
            ("Introduction to Biosystems Technology", 2),
            ("Introductory Animal Husbandry", 2),
            ("Plantation and Field Crop Production", 2),
            ("Crop Nutrient Management", 3),
        ],
        ("2nd Year", "1st Semester"): [
            ("Integrated English Language Skills for Technology (III)", 1),
            ("Soil Fertility Management", 2),
            ("Agricultural Meteorology", 2),
            ("Farm Structures and Irrigation Systems", 3),
            ("Agricultural Machinery and Power", 3),
            ("Introduction to Bioprocess Technology", 2),
            ("Introduction to Agricultural Economics", 2),
            ("Plant Protection", 3),
        ],
        ("2nd Year", "2nd Semester"): [
            ("Integrated English Language Skills for Technology (IV)", 1),
            ("Soil and Water Conservation", 2),
            ("Farm Management", 3),
            ("Post-Harvest Technology", 3),
            ("Agricultural Biotechnology", 3),
            ("Animal Nutrition and Feeding", 3),
            ("Agricultural Waste Management", 2),
        ],
        ("3rd Year", "1st Semester"): [
            ("Integrated English Language Skills for Technology (V)", 1),
            ("Renewable Energy Systems", 3),
            ("Agro-Processing Technology", 3),
            ("Environmental Pollution and Control", 3),
            ("Agricultural Extension and Communication", 3),
            ("Agricultural Policy and Planning", 3),
            ("Entrepreneurship in Agriculture", 3),
        ],
        ("3rd Year", "2nd Semester"): [
            ("Integrated English Language Skills for Technology (VI)", 1),
            ("Climate Change and Agriculture", 3),
            ("Sustainable Agricultural Practices", 3),
            ("Soil and Water Management", 3),
            ("Agricultural Marketing", 3),
            ("Agricultural Finance", 3),
            ("Research Methodology in Agriculture", 3),
        ],
        ("4th Year", "1st Semester"): [
            ("Integrated English Language Skills for Technology (VII)", 1),
            ("Advanced Agricultural Biotechnology", 3),
            ("Agricultural Waste Utilization", 3),
            ("Advanced Irrigation Systems", 3),
            ("Agricultural Policy Analysis", 3),
            ("Project Management in Agriculture", 3),
        ],
        ("4th Year", "2nd Semester"): [
            ("Integrated English Language Skills for Technology (VIII)", 1),
            ("Industrial Training", 6),
            ("Final Year Project", 6),
        ],
    },
    "Bachelor of Biosystems Technology Honours in Environmental Technology": {
        # Level 1
        ("1st Year", "1st Semester"): [
            ("Integrated English Language Skills for Technology (I)", 1),
            ("Workshop Practice", 1),
            ("Basic Mathematics", 2),
            ("Biology", 2),
            ("Physics", 3),
            ("Technology and Environment", 1),
            ("Biosystems Technology for Sustainable Environment", 1),
            ("Introduction to Hydrology", 2),
            ("Concepts and Techniques in Ecology", 2),
            ("Chemistry", 3),
        ],
        ("1st Year", "2nd Semester"): [
            ("Integrated English Language Skills for Technology (II)", 1),
            ("Technology and Historical Transformation", 1),
            ("Computer Applications", 2),
            ("Basic Soil Science", 2),
            ("Biology for Environmental Technology", 3),
            ("Chemicals in the Environment", 3),
            ("Environmental Microbiology", 3),
        ],
        # Level 2
        ("2nd Year", "1st Semester"): [
            ("Primary English Communication Skills for Technology (I)", 1),
            ("Management of Technology", 2),
            ("Environmental Economics", 1),
            ("Coastal Management Technologies", 1),
            ("Environmental Conservation and Management Technologies", 2),
            ("Analytical Techniques for Water Analysis", 3),
            ("Tools and Techniques in Applied Ecology", 3),
            ("Water Treatment Technologies", 3),
        ],
        ("2nd Year", "2nd Semester"): [
            ("English Communication Skills for Technology (II)", 1),
            ("Green Technology", 1),
            ("Applied Groundwater Management Technology", 2),
            ("Climate Change, Adaptation and Mitigation Technology", 2),
            ("Introduction to Geographic Information System (GIS)", 2),
            ("Solid Waste Management Technology", 2),
            ("Sri Lankan Institutional Framework for Environmental Governance and Management", 2),
            ("Land Management Techniques", 3),
        ],
        # Level 3
        ("3rd Year", "1st Semester"): [
            ("Environmental Impact Assessment", 2),
            ("Environmental Policy and Legislation", 2),
            ("Environmental Biotechnology", 3),
            ("Environmental Pollution and Control", 3),
            ("Renewable Energy Systems", 3),
            ("Environmental Monitoring and Management", 3),
        ],
        ("3rd Year", "2nd Semester"): [
            ("Environmental Risk Assessment", 3),
            ("Sustainable Development", 3),
            ("Environmental Auditing", 3),
            ("Internship", 6),
        ],
        # Level 4
        ("4th Year", "1st Semester"): [
            ("Research Methodology", 3),
            ("Environmental Management Systems", 3),
            ("Environmental Project Management", 3),
            ("Environmental Entrepreneurship", 3),
            ("Final Year Project", 6),
        ],
        ("4th Year", "2nd Semester"): [
            ("Professional Ethics and Practices", 3),
            ("Environmental Consultancy", 3),
            ("Environmental Education and Awareness", 3),
        ],
    },
    "BET Honours in Instrumentation and Automation": {
    # Level 1
    ("1st Year", "1st Semester"): [
        ("Workshop Practice", 1),
        ("Basic Mathematics", 2),
        ("Physics", 3),
        ("Essentials of Electrical and Electronics Engineering", 2),
        ("Introduction to Instrumentation & Automation", 2),
        ("Computer Applications", 2),
        ("Programming I", 3),
    ],
    ("1st Year", "2nd Semester"): [
        ("Technology and Historical Transformation", 1),
        ("Engineering Drawing", 2),
        ("Chemistry", 2),
        ("Applied Mechanics", 2),
        ("Electronics Laboratory I", 1),
        ("Programming II", 3),
        ("Electrical Circuits", 3),
        ("Introduction to Process Control", 2),
    ],
    # Level 2
    ("2nd Year", "1st Semester"): [
        ("Management of Technology", 2),
        ("Measurements & Instrumentation", 2),
        ("Microcontrollers & Embedded Systems", 3),
        ("Database Management Systems", 2),
        ("Object-Oriented Programming", 3),
        ("Electronics Laboratory II", 1),
        ("Control Systems", 3),
    ],
    ("2nd Year", "2nd Semester"): [
        ("Green Technology", 1),
        ("Environmental Monitoring", 2),
        ("Digital Signal Processing", 2),
        ("Web Application Development", 2),
        ("Instrumentation & Automation Laboratory", 3),
        ("PLC & SCADA Systems", 3),
        ("Mobile Application Development", 3),
    ],
    # Level 3
    ("3rd Year", "1st Semester"): [
        ("Industrial Instrumentation", 3),
        ("Sensors and Transducers", 3),
        ("Electrical Machines & Drives", 3),
        ("Analytical Instrumentation", 3),
        ("Microprocessor Systems", 3),
        ("Advanced Control Systems", 3),
    ],
    ("3rd Year", "2nd Semester"): [
        ("Robotics and Automation", 3),
        ("Process Control Systems", 3),
        ("Computer Networks", 3),
        ("Industrial Training", 6),
    ],
    # Level 4
    ("4th Year", "1st Semester"): [
        ("Research Methodology", 3),
        ("Advanced Instrumentation Systems", 3),
        ("Industrial Automation Project", 6),
        ("Entrepreneurship", 3),
    ],
    ("4th Year", "2nd Semester"): [
        ("Professional Ethics & Practices", 3),
        ("Final Year Project", 8),
    ],
},

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

semester_frames = {}
semester_gpa_labels = {}

# ----------------- Functions -----------------
def calculate_gpa():
    try:
        sem_gpas = []
        for (year, sem), widgets in semester_frames.items():
            sem_points, sem_credits = 0, 0
            for subject_name, credit_label, grade_combo in widgets:
                credit = float(credit_label.cget("text"))
                grade = grade_combo.get()
                if grade in ["None", ""]:
                    continue
                sem_points += credit * grade_map[grade]
                sem_credits += credit
            sem_gpa = (sem_points / sem_credits) if sem_credits > 0 else 0
            sem_gpas.append(sem_gpa)
            semester_gpa_labels[(year, sem)].config(text=f"{sem_gpa:.3f}", fg="green" if sem_gpa>=2 else "red")
        final_gpa = sum(sem_gpas)/len(sem_gpas) if sem_gpas else 0
        label_cum.config(text=f"Final GPA: {final_gpa:.3f}")
        
        # Show degree class
        degree_class = get_degree_class(final_gpa)
        label_class.config(text=degree_class)
        
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

def get_degree_class(gpa):
    if gpa >= 3.7:
        return "🎉 Congratulations! You have a First Class Degree"
    elif gpa >= 3.3:
        return "🎉 Congratulations! You have a Second Upper Class Degree"
    elif gpa >= 3.0:
        return "You have a Second Lower Class Degree"
    else:
        return "Don’t worry, you don’t have a class, but still you can succeed!"

def load_semesters():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    semester_frames.clear()
    semester_gpa_labels.clear()
    year = year_combo.get()
    sem = sem_combo.get()
    dept = dept_combo.get()
    if not year or not sem or not dept:
        messagebox.showwarning("Warning", "Please select Degree, Year, and Semester")
        return
    subjects_data = departments.get(dept, {})
    target_index = semester_order.index((year, sem))
    for idx in range(target_index + 1):
        y, s = semester_order[idx]
        frame = tk.LabelFrame(scrollable_frame, text=f"{y} - {s}", bg="#f0f0f0", font=("Arial", 11, "bold"))
        frame.pack(fill="x", pady=5, padx=10, anchor="n")
        tk.Label(frame, text="Subject", bg="#f0f0f0", width=35, anchor="w").grid(row=0, column=0, padx=5, pady=2)
        tk.Label(frame, text="Credit", bg="#f0f0f0", width=7).grid(row=0, column=1, padx=5, pady=2)
        tk.Label(frame, text="Grade", bg="#f0f0f0", width=10).grid(row=0, column=2, padx=5, pady=2)
        tk.Label(frame, text="Sem GPA", bg="#f0f0f0", width=10).grid(row=0, column=3, padx=5, pady=2)
        subject_widgets = []
        subjects = subjects_data.get((y, s), [])
        for i, (subject, credit) in enumerate(subjects, start=1):
            lbl_subject = tk.Label(frame, text=subject, anchor="w", bg="#f0f0f0", width=35)
            lbl_subject.grid(row=i, column=0, padx=5, pady=2, sticky="w")
            credit_label = tk.Label(frame, text=str(credit), bg="#f0f0f0", width=7)
            credit_label.grid(row=i, column=1, padx=5, pady=2)
            grade_combo = ttk.Combobox(frame, values=grade_options, width=10)
            grade_combo.set("None")
            grade_combo.grid(row=i, column=2, padx=5, pady=2)
            subject_widgets.append((subject, credit_label, grade_combo))
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
    # Reset all grades
    for widgets in semester_frames.values():
        for _, _, grade_combo in widgets:
            grade_combo.set("None")
    # Reset semester GPA labels
    for lbl in semester_gpa_labels.values():
        lbl.config(text="--")
    # Reset final GPA
    label_cum.config(text="Final GPA: --")
    # Reset degree class
    label_class.config(text="")  # <-- This clears the degree class
    # Reset top selection comboboxes
    dept_combo.set("")
    year_combo.set("")
    sem_combo.set("")
    # Clear semester frames
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    semester_frames.clear()
    semester_gpa_labels.clear()

# ----------------- GUI -----------------
root = tk.Tk()
root.title("🎓 GPA Calculator")
root.state('zoomed')  # Full screen

# Top Frame
top_frame = tk.Frame(root, bg="#e8f0f2")
top_frame.pack(pady=10)
tk.Label(top_frame, text="Select Degree:", bg="#e8f0f2", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
dept_combo = ttk.Combobox(top_frame, values=list(departments.keys()), width=60)  # Increased width
dept_combo.grid(row=0, column=1, padx=5)
tk.Label(top_frame, text="Select Year:", bg="#e8f0f2", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5)
year_combo = ttk.Combobox(top_frame, values=["1st Year","2nd Year","3rd Year","4th Year"], width=12)
year_combo.grid(row=0, column=3, padx=5)
tk.Label(top_frame, text="Select Semester:", bg="#e8f0f2", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=5)
sem_combo = ttk.Combobox(top_frame, values=["1st Semester","2nd Semester"], width=12)
sem_combo.grid(row=0, column=5, padx=5)

# Buttons
tk.Button(top_frame, text="Load Subjects", command=load_semesters, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=6, padx=5)
tk.Button(top_frame, text="Export Results", command=export_results, bg="#FF9800", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=7, padx=5)
tk.Button(top_frame, text="Import Results", command=import_results, bg="#9C27B0", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=8, padx=5)
tk.Button(top_frame, text="Reset All", command=reset_all, bg="#f44336", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=9, padx=5)

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
canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

# Bottom GPA Frame
bottom_frame = tk.Frame(root, bg="#e8f0f2")
bottom_frame.pack(pady=10)
tk.Button(bottom_frame, text="Calculate GPA", command=calculate_gpa, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
label_cum = tk.Label(bottom_frame, text="Final GPA: --", font=("Arial", 14, "bold"), fg="#FF5722", bg="#e8f0f2")
label_cum.pack(pady=5)
label_class = tk.Label(bottom_frame, text="", font=("Arial", 14, "bold"), fg="#4CAF50", bg="#e8f0f2")
label_class.pack(pady=5)

root.mainloop()
