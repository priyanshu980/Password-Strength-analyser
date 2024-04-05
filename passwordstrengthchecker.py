import re

def check_password_strength(password):
    # Check the length of the password 
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

    # Check the variety of characters in the password
    if not re.search("[a-z]", password):
        return "Weak"
    elif not re.search("[A-Z]", password):
        return "Weak"
    elif not re.search("[0-9]", password):
        return "Weak"
    elif not re.search("[!@#$%^&*()?]", password):
        return "Weak"

    # Check for consecutive characters or repeated characters
    if re.search(r"(.)\1{2,}", password):
        return "Weak"

    # Check for the use of dictionary words 
    if password in common_passwords:
        return "Weak"

    # Check for the use of personal information
    if re.search(r"[A-Za-z0-9]+", password):
        return "Weak"

    # The password is strong
    return "Strong"

# Get the password from the user 
password = input("Enter your password: ")

# Check the strength of the password
strength = check_password_strength(password)

# Print the strength of the password
print("Password Strength:", strength)
