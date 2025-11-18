import tkinter as tk
from tkinter import messagebox

# Simple rule mapping replacing clipspy rules
RULES = {
    ("yes", "yes"): "High chance of Covid-19. Please get tested.",
    ("no", "no"): "Symptoms do not match Covid-19.",
    ("yes", "no"): "Fever only — consider monitoring and testing if symptoms progress.",
    ("no", "yes"): "Cough only — could be other causes; consider testing if concerned."
}

# GUI
root = tk.Tk()
root.title("Covid-19 Expert System")

tk.Label(root, text="Do you have fever? (yes/no)").pack(padx=8, pady=(8,0))
entry_fever = tk.Entry(root)
entry_fever.pack(padx=8, pady=(0,8))

tk.Label(root, text="Do you have cough? (yes/no)").pack(padx=8, pady=(4,0))
entry_cough = tk.Entry(root)
entry_cough.pack(padx=8, pady=(0,8))

def diagnose():
    fever = entry_fever.get().strip().lower()
    cough = entry_cough.get().strip().lower()

    if fever not in ("yes", "no") or cough not in ("yes", "no"):
        messagebox.showerror("Input error", "Please enter 'yes' or 'no' for both questions.")
        return

    message = RULES.get((fever, cough))
    if message:
        messagebox.showinfo("Diagnosis Result", message)
    else:
        messagebox.showinfo("Diagnosis Result", "No diagnosis produced.")

tk.Button(root, text="Check", command=diagnose).pack(pady=12)
root.mainloop()
