import tkinter as tk
import subprocess

def launch_app1():
    subprocess.Popen(["python", "Drawing\drawing.py"])

def launch_app2():
    subprocess.Popen(["python", "sign_detection\inference_classifier.py"])

# Create the main window
root = tk.Tk()
root.title("Sign Sense")

# Set the window size to 800x600 pixels
root.geometry("400x200")

# Create a Label widget to display text
text_label = tk.Label(root, text="SignSense", font=("Helvetica", 16, "bold"))
text_label.pack(padx=20, pady=20)  # Add padding around the label

# Create buttons to launch the Python scripts
button1 = tk.Button(root, text="Launch Drawing", command=launch_app1)
button1.pack(padx=10, pady=5)

button2 = tk.Button(root, text="Launch Sign Detection", command=launch_app2)
button2.pack(padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
