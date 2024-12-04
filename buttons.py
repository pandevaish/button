import tkinter as tk

# Function to handle gear shift button clicks
def gear_shift_button_click(gear_position):
    print(f"Gear Shift: {gear_position}")

# Function to handle throttle value changes
def throttle_value_changed(value):
    throttle_value_label.config(text=f"Throttle Value: {value}")  # Update the label to show the current value
    print(f"Throttle: {value}")

# Create the main window
root = tk.Tk()
root.title("Control Simulation")

# Set window size and background color
root.geometry("600x450")
root.configure(bg="#1e1e1e")

# Centering the window
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# Frame for the control panel to hold everything in the center
frame = tk.Frame(root, bg="#1e1e1e")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label for Title
title_label = tk.Label(frame, text="Control Panel", font=("Helvetica", 22, "bold"), fg="white", bg="#1e1e1e")
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# Button style without the 'command'
button_style = {
    'font': ("Arial", 14, "bold"),
    'width': 20,
    'height': 2,
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

# Create Gear Shift Buttons with rounded corners and large size
button_neutral = tk.Button(frame, text="Gear Shift - Neutral", command=lambda: gear_shift_button_click("Neutral"), **button_style)
button_neutral.grid(row=1, column=0, padx=20, pady=10)

button_ahead = tk.Button(frame, text="Gear Shift - Ahead", command=lambda: gear_shift_button_click("Ahead"), **button_style)
button_ahead.config(bg="#FF9800")
button_ahead.grid(row=1, column=1, padx=20, pady=10)

button_reverse = tk.Button(frame, text="Gear Shift - Reverse", command=lambda: gear_shift_button_click("Reverse"), **button_style)
button_reverse.config(bg="#F44336")
button_reverse.grid(row=1, column=2, padx=20, pady=10)

# Create Throttle Scroll (Slider) with colorful style and rounded appearance
throttle_label = tk.Label(frame, text="Throttle (0 to 100)", font=("Helvetica", 16), fg="white", bg="#1e1e1e")
throttle_label.grid(row=2, column=0, columnspan=3, pady=20)

# Throttle slider with a red color and larger size
throttle_scroll = tk.Scale(frame, from_=0, to=100, orient="horizontal", command=throttle_value_changed,
                            sliderlength=50, troughcolor="#FF0000", bg="#1e1e1e", fg="white", length=400,
                            highlightbackground="#1e1e1e", highlightcolor="#1e1e1e", relief="flat")
throttle_scroll.grid(row=3, column=0, columnspan=3, padx=20, pady=10)

# Customize the slider appearance
throttle_scroll.config(
    sliderlength=50,  # Larger slider handle
    width=20,         # Thicker slider bar
    troughcolor="#FF0000",  # Red color for the trough
    activebackground="#FF0000",  # Red color for the active part of the slider
    fg="#FFFFFF",     # White color for the slider handle
    bg="#1e1e1e"      # Dark background
)

# Adding Throttle Value Display
throttle_value_label = tk.Label(frame, text="Throttle Value: 0", font=("Arial", 14), fg="white", bg="#1e1e1e")
throttle_value_label.grid(row=4, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
