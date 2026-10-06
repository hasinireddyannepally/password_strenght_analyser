import re
from zxcvbn import zxcvbn


def analyze_password(password):
    """Analyze password strength using rules and zxcvbn."""

    if not password:
        return {
            "score": 0,
            "strength": "Very Weak",
            "length": 0,
            "uppercase": False,
            "lowercase": False,
            "numbers": False,
            "special": False,
            "feedback": ["Please enter a password."]
        }

    length = len(password)

    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    result = zxcvbn(password)

    zxcvbn_score = result["score"]

    if zxcvbn_score == 0:
        strength = "Very Weak"
    elif zxcvbn_score == 1:
        strength = "Weak"
    elif zxcvbn_score == 2:
        strength = "Medium"
    elif zxcvbn_score == 3:
        strength = "Strong"
    else:
        strength = "Very Strong"

    feedback = []

    if length < 8:
        feedback.append("Use at least 8 characters.")

    if not has_uppercase:
        feedback.append("Add uppercase letters.")

    if not has_lowercase:
        feedback.append("Add lowercase letters.")

    if not has_number:
        feedback.append("Add numbers.")

    if not has_special:
        feedback.append("Add special characters.")

    if not feedback:
        feedback.append("Your password has good characteristics.")

    return {
        "score": zxcvbn_score,
        "strength": strength,
        "length": length,
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "numbers": has_number,
        "special": has_special,
        "feedback": feedback
    }