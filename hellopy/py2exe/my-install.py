'''
see https://www.geeksforgeeks.org/python-gui-tkinter/
'''

import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_left_click(event):
    print(f"Left click at ({event.x}, {event.y})")

def on_right_click(event):
    print(f"Right click at ({event.x}, {event.y})")

def on_mouse_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

root = tk.Tk()
root.title("Color Options in Tkinter")

# Create a button with active background and foreground colors
button = tk.Button(root, text="Click Me", activebackground="blue", activeforeground="white")

# Create a label with background and foreground colors
label = tk.Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black")
label0 = tk.Label(root, text="")

# Create an Entry widget with selection colors
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")

'''
button.pack()
label.pack()
entry.pack()
'''

button.grid(row=0, column=0)
label0.grid(row=0, column=1)
label.grid(row=0, column=2)
entry.grid(row=1, column=0, columnspan=3)


root.bind("<KeyPress>", on_key_press)
root.bind("<Button-1>", on_left_click)
root.bind("<Button-3>", on_right_click)
# root.bind("<Motion>", on_mouse_motion)

root.geometry("300x200")
root.mainloop()