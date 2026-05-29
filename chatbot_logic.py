from prompts import DISCLAIMER, FALLBACK_QUESTIONS, SYMPTOM_PATTERNS


def _default_response(symptoms):
    return {
        "title": "More information is needed",
        "risk_level": "Undetermined",
        "urgency": "Needs more detail",
        "summary": (
            "The current symptom description is too broad for a helpful prototype-level triage result."
        ),
        "possible_conditions": ["Unable to estimate yet"],
        "care_advice": [
            "Share the main symptom, how long it has been present, and how severe it feels.",
            "Mention age group, relevant medical history, and any medicines already taken.",
        ],
        "red_flags": [
            "Breathing difficulty",
            "Severe pain",
            "Fainting or confusion",
            "Bleeding that does not stop",
        ],
        "follow_up_questions": FALLBACK_QUESTIONS,
        "matched_pattern": "No strong symptom cluster matched",
        "disclaimer": DISCLAIMER,
        "input_summary": symptoms,
    }


def analyze_symptoms(symptoms, emergency=False):
    normalized = symptoms.lower().strip()
    matches = []

    for pattern in SYMPTOM_PATTERNS:
        if all(keyword in normalized for keyword in pattern["keywords_all"]) and all(
            any(option in normalized for option in group) for group in pattern["keywords_any"]
        ):
            matches.append(pattern)

    if not matches:
        response = _default_response(symptoms)
    else:
        best_match = max(matches, key=lambda item: item["priority"])
        response = {
            "title": best_match["title"],
            "risk_level": best_match["risk_level"],
            "urgency": best_match["urgency"],
            "summary": best_match["summary"],
            "possible_conditions": best_match["possible_conditions"],
            "care_advice": best_match["care_advice"],
            "red_flags": best_match["red_flags"],
            "follow_up_questions": best_match["follow_up_questions"],
            "matched_pattern": ", ".join(best_match["matched_keywords"]),
            "disclaimer": DISCLAIMER,
            "input_summary": symptoms,
        }

    if emergency:
        response["title"] = "Emergency support recommended"
        response["risk_level"] = "Critical"
        response["urgency"] = "Immediate medical attention"
        response["summary"] = (
            "The symptom description contains red-flag terms that should be treated as a medical emergency."
        )
        response["care_advice"] = [
            "Contact local emergency services or go to the nearest emergency department now.",
            "Do not drive yourself if you feel faint, breathless, or have severe chest symptoms.",
            "Keep another person nearby if possible.",
        ]
        response["red_flags"] = [
            "Chest pain or pressure",
            "Shortness of breath",
            "Severe bleeding",
            "Loss of consciousness",
        ]

    return response
