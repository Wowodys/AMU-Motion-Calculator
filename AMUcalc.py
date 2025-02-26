import tkinter as tk
from tkinter import messagebox

def calculate_extruder_rotation_distance():
    """Calculate extruder rotation distance"""
    try:
        previous_rotation_distance = float(previous_rotation_entry.get())
        actual_extrude_distance = float(actual_extrude_entry.get())
        requested_extrude_distance = float(requested_extrude_entry.get())
        
        if requested_extrude_distance == 0:
            messagebox.showerror("Input Error", "Requested extrude distance cannot be zero.")
            return
        
        extruder_rotation_distance = (previous_rotation_distance * actual_extrude_distance) / requested_extrude_distance
        extruder_result_label.config(text=f"Extruder Rotation Distance: {extruder_rotation_distance:.2f} mm")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

def calculate_rotation_distance():
    """Calculate rotation distance based on belt pitch and pulley teeth"""
    try:
        belt_pitch = float(belt_pitch_entry.get())
        num_teeth = int(teeth_entry.get())
        rotation_distance = belt_pitch * num_teeth
        rotation_result_label.config(text=f"Rotation Distance: {rotation_distance:.2f} mm")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for belt pitch and number of teeth.")

def calculate_lead_screw_rotation_distance():
    """Calculate lead screw driven axis rotation distance"""
    try:
        screw_pitch = float(screw_pitch_entry.get())
        num_threads = int(threads_entry.get())
        rotation_distance = screw_pitch * num_threads
        lead_screw_result_label.config(text=f"Lead-Screw Rotation Distance: {rotation_distance:.2f} mm")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for screw pitch and number of threads.")

# Create main window
root = tk.Tk()
root.title("AMU Calculator")
root.geometry("500x550")  # Increased window height

# Extruder Rotation Distance Section
extruder_frame = tk.LabelFrame(root, text="Extruder Rotation Distance Calculation", padx=10, pady=10, bd=3, relief="solid")
extruder_frame.pack(padx=10, pady=10, fill="both")

tk.Label(extruder_frame, text="Previous Rotation Distance:").grid(row=0, column=0, sticky='w', pady=2)
previous_rotation_entry = tk.Entry(extruder_frame)
previous_rotation_entry.grid(row=0, column=1, pady=2)

tk.Label(extruder_frame, text="Actual Extrude Distance:").grid(row=1, column=0, sticky='w', pady=2)
actual_extrude_entry = tk.Entry(extruder_frame)
actual_extrude_entry.grid(row=1, column=1, pady=2)

tk.Label(extruder_frame, text="Requested Extrude Distance:").grid(row=2, column=0, sticky='w', pady=2)
requested_extrude_entry = tk.Entry(extruder_frame)
requested_extrude_entry.grid(row=2, column=1, pady=2)

tk.Button(extruder_frame, text="Calculate", command=calculate_extruder_rotation_distance).grid(row=3, columnspan=2, pady=5)
extruder_result_label = tk.Label(extruder_frame, text="Extruder Rotation Distance:", bd=1, relief="solid")
extruder_result_label.grid(row=4, columnspan=2, pady=2)

# Belt-Driven Axis Rotation Distance Section
belt_frame = tk.LabelFrame(root, text="Belt-Driven Axis Rotation Distance Calculation", padx=10, pady=10, bd=3, relief="solid")
belt_frame.pack(padx=10, pady=10, fill="both")

tk.Label(belt_frame, text="Belt Pitch (mm):").grid(row=0, column=0, sticky='w', pady=2)
belt_pitch_entry = tk.Entry(belt_frame)
belt_pitch_entry.grid(row=0, column=1, pady=2)

tk.Label(belt_frame, text="Number of Teeth:").grid(row=1, column=0, sticky='w', pady=2)
teeth_entry = tk.Entry(belt_frame)
teeth_entry.grid(row=1, column=1, pady=2)

tk.Button(belt_frame, text="Calculate", command=calculate_rotation_distance).grid(row=2, columnspan=2, pady=5)
rotation_result_label = tk.Label(belt_frame, text="Rotation Distance:", bd=1, relief="solid")
rotation_result_label.grid(row=3, columnspan=2, pady=2)

# Lead-Screw Driven Axis Rotation Distance Section
lead_screw_frame = tk.LabelFrame(root, text="Lead-Screw Driven Axis Rotation Distance Calculation", padx=10, pady=10, bd=3, relief="solid")
lead_screw_frame.pack(padx=10, pady=10, fill="both")

tk.Label(lead_screw_frame, text="Screw Pitch (mm):").grid(row=0, column=0, sticky='w', pady=2)
screw_pitch_entry = tk.Entry(lead_screw_frame)
screw_pitch_entry.grid(row=0, column=1, pady=2)

tk.Label(lead_screw_frame, text="Number of Threads:").grid(row=1, column=0, sticky='w', pady=2)
threads_entry = tk.Entry(lead_screw_frame)
threads_entry.grid(row=1, column=1, pady=2)

tk.Button(lead_screw_frame, text="Calculate", command=calculate_lead_screw_rotation_distance).grid(row=2, columnspan=2, pady=5)
lead_screw_result_label = tk.Label(lead_screw_frame, text="Lead-Screw Rotation Distance:", bd=1, relief="solid")
lead_screw_result_label.grid(row=3, columnspan=2, pady=2)

root.mainloop()
