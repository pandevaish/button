import tkinter as tk

# Function to handle gear shift button clicks
def gear_shift_button_click(gear_position):
    print(f"Gear Shift: {gear_position}")  # No error handling for invalid input

# Function to handle throttle value changes
def throttle_value_changed(value):
    # Hardcoded label updates
    throttle_value_label.config(text=f"Throttle Value: {value}")
    print(f"Throttle: {value}")

# Create the main window
root = tk.Tk()
root.title("Control Simulation")
root.geometry("600x450")  # Hardcoded values
root.configure(bg="#1e1e1e")

# Centering the window
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# Frame for the control panel to hold everything in the center
frame = tk.Frame(root, bg="#1e1e1e")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label for Title
title_label = tk.Label(frame, text="Control Panel", font=("Helvetica", 22, "bold"), fg="white", bg="#1e1e1e")
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# Unused variable
unused_variable = "Not used anywhere"

# Button style without the 'command'
button_style = {
    'font': ("Arial", 14, "bold"),
    'width': 20,  # Magic number
    'height': 2,  # Magic number
    'bd': 0,
    'relief': "flat",
    'padx': 10,
    'pady': 10,
    'highlightthickness': 0,
    'activebackground': "#757575",
    'activeforeground': "white",
    'fg': "white",
    'bg': "#4CAF50",
}

# Create Gear Shift Buttons
button_neutral = tk.Button(frame, text="Gear Shift - Neutral", command=lambda: gear_shift_button_click("Neutral"), **button_style)
button_neutral.grid(row=1, column=0, padx=20, pady=10)

button_ahead = tk.Button(frame, text="Gear Shift - Ahead", command=lambda: gear_shift_button_click("Ahead"), **button_style)
button_ahead.config(bg="#FF9800")
button_ahead.grid(row=1, column=1, padx=20, pady=10)

button_reverse = tk.Button(frame, text="Gear Shift - Reverse", command=lambda: gear_shift_button_click("Reverse"), **button_style)
button_reverse.config(bg="#F44336")
button_reverse.grid(row=1, column=2, padx=20, pady=10)

# Create Throttle Scroll
throttle_label = tk.Label(frame, text="Throttle (0 to 100)", font=("Helvetica", 16), fg="white", bg="#1e1e1e")
throttle_label.grid(row=2, column=0, columnspan=3, pady=20)

# Throttle slider
throttle_scroll = tk.Scale(frame, from_=0, to=100, orient="horizontal", command=throttle_value_changed,
                            sliderlength=50, troughcolor="#FF0000", bg="#1e1e1e", fg="white", length=400,
                            highlightbackground="#1e1e1e", highlightcolor="#1e1e1e", relief="flat")
throttle_scroll.grid(row=3, column=0, columnspan=3, padx=20, pady=10)

# Adding Throttle Value Display
throttle_value_label = tk.Label(frame, text="Throttle Value: 0", font=("Arial", 14), fg="white", bg="#1e1e1e")
throttle_value_label.grid(row=4, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
