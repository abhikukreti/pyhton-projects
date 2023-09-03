import random
import string
import tkinter as tk

def generate_password(length=8, strength='medium'):
    characters = ''
    if strength == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == 'medium':
        characters = string.ascii_letters + string.digits
    elif strength == 'weak':
        characters = string.ascii_lowercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_button_click():
    choice = button_var.get()

    if choice == '1':
        password = generate_password(8, 'weak')
    elif choice == '2':
        password = generate_password(12, 'medium')
    elif choice == '3':
        password = generate_password(16, 'strong')
    else:
        print("Invalid choice. Generating medium strength password by default.")
        password = generate_password(12, 'medium')

    print("Generated password:", password)

# Create a Tkinter window
window = tk.Tk()

# Create a button widget
button_frame = tk.Frame(window)
button_frame.pack()

button_var = tk.StringVar()

weak_button = tk.Radiobutton(button_frame, text="Weak Password", variable=button_var, value='1', indicatoron=False)
weak_button.pack()

medium_button = tk.Radiobutton(button_frame, text="Medium Password", variable=button_var, value='2', indicatoron=False)
medium_button.pack()

strong_button = tk.Radiobutton(button_frame, text="Strong Password", variable=button_var, value='3', indicatoron=False)
strong_button.pack()

generate_button = tk.Button(window, text="Generate Password", command=on_button_click)
generate_button.pack()

# Start the Tkinter event loop
window.mainloop()