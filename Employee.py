import tkinter as tk
from tkinter import ttk, messagebox


# =========================
# Submit Function
# =========================
def submit_form():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    department = department_combo.get()
    employee_id = employee_id_entry.get()

    # Check empty fields
    if (first_name == "" or last_name == "" or mobile == "" or
            email == "" or gender == "" or department == "" or
            employee_id == ""):

        messagebox.showwarning(
            "Warning",
            "Please fill all the fields."
        )
        return

    # Display submitted information
    submitted_info = (
        "Employee Registration Details\n\n"
        f"Employee ID : {employee_id}\n"
        f"First Name  : {first_name}\n"
        f"Last Name   : {last_name}\n"
        f"Mobile No.  : {mobile}\n"
        f"Email       : {email}\n"
        f"Gender      : {gender}\n"
        f"Department  : {department}"
    )

    messagebox.showinfo(
        "Submitted Information",
        submitted_info
    )


# =========================
# Main Window
# =========================
root = tk.Tk()
root.title("Employee Registration Form")
root.geometry("700x650")
root.resizable(False, False)

# Background
root.configure(bg="#e8f6f7")


# =========================
# Main Frame
# =========================
main_frame = tk.Frame(
    root,
    bg="#e8f6f7",
    padx=40,
    pady=25
)

main_frame.pack(fill="both", expand=True)


# =========================
# Title
# =========================
title_label = tk.Label(
    main_frame,
    text="Employee Registration Form",
    font=("Arial", 24, "bold"),
    bg="#e8f6f7",
    fg="#34495e"
)

title_label.pack(pady=(5, 30))


# =========================
# Form Frame
# =========================
form_frame = tk.Frame(
    main_frame,
    bg="#e8f6f7"
)

form_frame.pack()


# =========================
# First Name
# =========================
tk.Label(
    form_frame,
    text="First Name:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=0, column=0, sticky="w", padx=10, pady=10)

first_name_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=40
)

first_name_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


# =========================
# Last Name
# =========================
tk.Label(
    form_frame,
    text="Last Name:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=1, column=0, sticky="w", padx=10, pady=10)

last_name_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=40
)

last_name_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


# =========================
# Mobile Number
# =========================
tk.Label(
    form_frame,
    text="Mobile Number:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=2, column=0, sticky="w", padx=10, pady=10)

mobile_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=40
)

mobile_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)


# =========================
# Email
# =========================
tk.Label(
    form_frame,
    text="Email:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=3, column=0, sticky="w", padx=10, pady=10)

email_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=40
)

email_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=10
)


# =========================
# Gender
# =========================
tk.Label(
    form_frame,
    text="Gender:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=4, column=0, sticky="w", padx=10, pady=10)

gender_var = tk.StringVar()

gender_frame = tk.Frame(
    form_frame,
    bg="#e8f6f7"
)

gender_frame.grid(
    row=4,
    column=1,
    sticky="w",
    padx=10,
    pady=10
)

tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    font=("Arial", 11),
    bg="#e8f6f7"
).pack(side="left", padx=5)

tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    font=("Arial", 11),
    bg="#e8f6f7"
).pack(side="left", padx=5)

tk.Radiobutton(
    gender_frame,
    text="Other",
    variable=gender_var,
    value="Other",
    font=("Arial", 11),
    bg="#e8f6f7"
).pack(side="left", padx=5)


# =========================
# Department
# =========================
tk.Label(
    form_frame,
    text="Department:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=5, column=0, sticky="w", padx=10, pady=10)

department_combo = ttk.Combobox(
    form_frame,
    font=("Arial", 11),
    width=38,
    state="readonly"
)

department_combo["values"] = (
    "IT",
    "HR",
    "Finance",
    "Marketing",
    "Sales",
    "Management"
)

department_combo.grid(
    row=5,
    column=1,
    padx=10,
    pady=10
)


# =========================
# Employee ID
# =========================
tk.Label(
    form_frame,
    text="Employee ID:",
    font=("Arial", 12),
    bg="#e8f6f7",
    fg="#34495e"
).grid(row=6, column=0, sticky="w", padx=10, pady=10)

employee_id_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=40
)

employee_id_entry.grid(
    row=6,
    column=1,
    padx=10,
    pady=10
)


# =========================
# Submit Button
# =========================
submit_button = tk.Button(
    main_frame,
    text="Submit",
    font=("Arial", 13, "bold"),
    bg="#3498db",
    fg="white",
    width=18,
    height=2,
    relief="flat",
    cursor="hand2",
    command=submit_form
)

submit_button.pack(pady=30)


# =========================
# Run Application
# =========================
root.mainloop()