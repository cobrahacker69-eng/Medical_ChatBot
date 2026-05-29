from flask import Flask, render_template, request

from chatbot_logic import analyze_symptoms
from emergency_detector import detect_emergency

app = Flask(__name__)

DEMO_REPORTS = [
    {
        "title": "Respiratory Triage",
        "summary": "Cough + fever cases were the most common sample input in testing.",
        "risk": "Medium",
        "volume": 68,
    },
    {
        "title": "Emergency Escalation",
        "summary": "Chest pain and breathing difficulty trigger urgent guidance instantly.",
        "risk": "High",
        "volume": 24,
    },
    {
        "title": "Follow-up Quality",
        "summary": "Fallback prompts ask for duration, severity, age, and red-flag symptoms.",
        "risk": "Low",
        "volume": 52,
    },
]

SETTINGS_PREVIEW = [
    {
        "title": "Symptom-based triage mode",
        "description": "Analyze free-text symptom input and organize it into structured care guidance.",
        "enabled": True,
    },
    {
        "title": "Emergency keyword escalation",
        "description": "Prioritize high-risk phrases such as chest pain and breathing difficulty.",
        "enabled": True,
    },
    {
        "title": "Patient-friendly advice formatting",
        "description": "Present likely concerns, urgency, and next steps in simple language.",
        "enabled": True,
    },
    {
        "title": "Prototype-safe medical disclaimer",
        "description": "Keep the interface clearly non-diagnostic and clinician-aware.",
        "enabled": True,
    },
]

QUICK_CASES = [
    {"label": "Respiratory", "text": "I have fever and cough for 2 days, and I feel weak."},
    {"label": "Emergency", "text": "I have chest pain and shortness of breath right now."},
    {"label": "Digestive", "text": "I have vomiting and diarrhea since morning and cannot eat properly."},
]

RECENT_ACTIVITY = [
    {"time": "2 min ago", "title": "Respiratory case reviewed", "meta": "Medium risk • Home monitoring"},
    {"time": "18 min ago", "title": "Emergency escalation triggered", "meta": "High risk • Immediate support"},
    {"time": "1 hr ago", "title": "Headache symptom check completed", "meta": "Low to medium risk"},
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        quick_cases=QUICK_CASES,
        recent_activity=RECENT_ACTIVITY,
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    symptoms = request.form.get("symptoms", "").strip()
    if not symptoms:
        return render_template("index.html", error="Please enter symptoms before analyzing.")

    emergency = detect_emergency(symptoms)
    analysis = analyze_symptoms(symptoms, emergency=emergency)

    return render_template("result.html", analysis=analysis, symptoms=symptoms)


@app.route("/emergency")
def emergency():
    emergency_support = {
        "when_to_call": [
            "Chest pain or pressure",
            "Trouble breathing or bluish lips",
            "Severe bleeding, collapse, or unconsciousness",
            "Sudden confusion, seizure, or one-sided weakness",
        ],
        "while_waiting": [
            "Stay with the patient and keep them calm.",
            "Do not give food or drink if consciousness is affected.",
            "Keep prescribed emergency medicines nearby if available.",
        ],
    }
    return render_template("emergency.html", emergency_support=emergency_support)


@app.route("/reports")
def reports():
    report_summary = {
        "total_cases": 144,
        "urgent_cases": 12,
        "common_pattern": "Respiratory symptoms",
    }
    return render_template("reports.html", reports=DEMO_REPORTS, report_summary=report_summary)


@app.route("/settings")
def settings():
    return render_template("settings.html", settings_preview=SETTINGS_PREVIEW)


if __name__ == "__main__":
    app.run(debug=False)
