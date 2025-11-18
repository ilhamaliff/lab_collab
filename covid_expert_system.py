import tkinter as tk
from tkinter import messagebox
from clipspy import Environment

# Setup CLIPS environment
env = Environment()

# Rule base
env.build("""
(deftemplate symptom
    (slot fever)
    (slot cough)
)

(defrule covid-positive
    (symptom (fever yes) (cough yes))
    =>
    (assert (diagnosis "High chance of Covid-19. Please get tested.")))

(defrule covid-negative
    (symptom (fever no) (cough no))
    =>
    (assert (diagnosis "Symptoms do not match Covid-19.")))
""")

# GUI
root = tk.Tk()
root.title("Covid-19 Expert System")

tk.Label(root, text="Do you have fever? (yes/no)").pack()
entry_fever = tk.Entry(root)
entry_fever.pack()

tk.Label(root, text="Do you have cough? (yes/no)").pack()
entry_cough = tk.Entry(root)
entry_cough.pack()

def diagnose():
    fever = entry_fever.get().lower()
    cough = entry_cough.get().lower()

    env.reset()
    env.assert_string(f'(symptom (fever {fever}) (cough {cough}))')
    env.run()

    # Fetch result
    result = env.facts()[-1]
    message = result.slot_value("diagnosis")
    messagebox.showinfo("Diagnosis Result", str(message))

tk.Button(root, text="Check", command=diagnose).pack()
root.mainloop()
