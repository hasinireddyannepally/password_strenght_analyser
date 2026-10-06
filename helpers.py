def get_strength_message(score):
    messages = {
        0: "Very weak password.",
        1: "Weak password.",
        2: "Medium-strength password.",
        3: "Strong password.",
        4: "Very strong password."
    }

    return messages.get(score, "Unknown strength.")