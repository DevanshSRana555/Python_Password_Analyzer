import tkinter as tk

def get_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include numbers")
    if not any(not c.isalnum() for c in password):
        suggestions.append("Include special characters (!@#$ etc)")

    return suggestions


def estimate_crack_time(score):
    if score <= 2:
        return "Instantly"
    elif score <= 4:
        return "Minutes to hours"
    else:
        return "Years"


def analyze_password():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    result = f"Strength: {strength}\n"
    result += f"Crack Time: {estimate_crack_time(score)}\n\n"

    suggestions = get_suggestions(password)
    if suggestions:
        result += "Suggestions:\n"
        for s in suggestions:
            result += f"- {s}\n"
    else:
        result += "Great password! 🎉"

    output_label.config(text=result)


# GUI setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x300")

title = tk.Label(root, text="Password Analyzer", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Password", command=analyze_password)
check_btn.pack(pady=10)

output_label = tk.Label(root, text="", justify="left")
output_label.pack(pady=10)

root.mainloop()