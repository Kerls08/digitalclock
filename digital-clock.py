import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.resizable(False, False)

# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S')  # Format the time as HH:MM:SS
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Call this function again after 1 second

# Create a label for the clock
time_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
time_label.pack(expand=True, fill='both')

# Initialize the clock
update_time()

# Run the application
root.mainloop()
