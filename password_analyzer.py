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


def analyze_password(password):
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

    # Strength rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\n" + "=" * 30)
    print(" PASSWORD ANALYZER ")
    print("=" * 30)

    print(f"\nPassword Strength: {strength}")
    print(f"Estimated Crack Time: {estimate_crack_time(score)}")

    suggestions = get_suggestions(password)

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("\nGreat password! 🎉")


# Run program
password = input("Enter your password: ")
analyze_password(password)