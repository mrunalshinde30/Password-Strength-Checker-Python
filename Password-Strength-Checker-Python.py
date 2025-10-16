import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    if strength == 4:
        return "Strong password 💪"
    elif strength == 3:
        return "Moderate password 👍"
    else:
        return "Weak password ⚠️"

password = input("Enter your password: ")
print(check_password_strength(password))
