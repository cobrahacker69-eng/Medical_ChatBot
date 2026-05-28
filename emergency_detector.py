def detect_emergency(symptoms):

    emergency_keywords = [
        "chest pain",
        "shortness of breath",
        "unconscious",
        "severe bleeding",
        "heart attack"
    ]

    symptoms = symptoms.lower()

    for word in emergency_keywords:
        if word in symptoms:
            return True

    return False