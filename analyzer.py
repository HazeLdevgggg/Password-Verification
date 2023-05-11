import random
import string
import tkinter as tk

def check_password_strength(password):
    """Fonction qui vérifie la force d'un mot de passe"""
    if len(password) < 8:
        return "Faible"
    has_letter = False
    has_uppercase = False
    has_special_char = False
    for char in password:
        if char.isalpha():
            has_letter = True
            if char.isupper():
                has_uppercase = True
        elif char in string.punctuation:
            has_special_char = True
    if has_letter and has_uppercase and has_special_char:
        return "Forte"
    else:
        return "Moyenne"

def generate_password():
    length = random.randint(12, 16) 
    uppercase = random.randint(1, 3) 
    lowercase = random.randint(1, 3) 
    digits = random.randint(1, 3) 
    symbols = length - uppercase - lowercase - digits 
    password = ""
    password += ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase))
    password += ''.join(random.choice(string.ascii_lowercase) for _ in range(lowercase))
    password += ''.join(random.choice(string.digits) for _ in range(digits))
    password += ''.join(random.choice(string.punctuation) for _ in range(symbols))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def analyze_password():
    password = password_entry.get()
    strength = check_password_strength(password)
    strength_label.config(text="Force du mot de passe: " + strength)
    if strength == "Faible":
        new_password = generate_password()
        new_password_label.config(text="Nouveau mot de passe: " + new_password)
    else:
        new_password_label.config(text="")

    if strength == "Moyenne":
        new_password = generate_password()
        new_password_label.config(text="Nouveau mot de passe: " + new_password)
    else:
        new_password_label.config(text="")

window = tk.Tk()
window.title("Analyseur de mot de passe")
window.geometry("400x200")

password_label = tk.Label(window, text="Entrez votre mot de passe:")
password_entry = tk.Entry(window)
analyze_button = tk.Button(window, text="Analyser", command=analyze_password)
strength_label = tk.Label(window, text="")
new_password_label = tk.Label(window, text="")

password_label.pack()
password_entry.pack()
analyze_button.pack()
strength_label.pack()
new_password_label.pack()

window.mainloop()
