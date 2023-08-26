import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    min_length = int(min_length_entry.get())
    has_number = number_var.get()
    has_special = special_var.get()

    digits = string.digits
    letters = string.ascii_letters
    special = string.punctuation
    
    characters = letters
    if has_number:
        characters += digits
    if has_special:
        characters += special
        
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
            
        elif new_char in special:
            has_special = True
            
        meets_criteria = True
        if number_var.get():
            meets_criteria = has_number
            
        if special_var.get():
            meets_criteria = meets_criteria and has_special
            
    password_var.set(pwd)


root = tk.Tk()
root.title("Password Generator")


tk.Label(root, text="Minimum Password Length:").pack()
min_length_entry = tk.Entry(root)
min_length_entry.pack()

number_var = tk.BooleanVar()
number_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=number_var)
number_checkbox.pack()

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_var = tk.StringVar()
generated_password_label = tk.Label(root, textvariable=password_var)
generated_password_label.pack()

root.mainloop()
