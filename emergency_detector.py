EMERGENCY_KEYWORDS = [
    "chest pain",
    "shortness of breath",
    "difficulty breathing",
    "unconscious",
    "severe bleeding",
    "heart attack",
    "stroke",
    "seizure",
    "bluish lips",
]


def detect_emergency(symptoms):
    normalized = symptoms.lower()
    return any(keyword in normalized for keyword in EMERGENCY_KEYWORDS)
