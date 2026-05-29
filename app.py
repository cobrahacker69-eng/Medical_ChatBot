from flask import Flask, render_template, request

from chatbot_logic import analyze_symptoms
from emergency_detector import detect_emergency

app = Flask(__name__)

DEMO_REPORTS = [
    {
        "title": "Respiratory Triage",
        "summary": "Cough + fever cases were the most common sample input in testing.",
        "risk": "Medium",
    },
    {
        "title": "Emergency Escalation",
        "summary": "Chest pain and breathing difficulty trigger urgent guidance instantly.",
        "risk": "High",
    },
    {
        "title": "Follow-up Quality",
        "summary": "Fallback prompts ask for duration, severity, age, and red-flag symptoms.",
        "risk": "Low",
    },
]

SETTINGS_PREVIEW = [
    "Symptom-based triage mode",
    "Emergency keyword escalation",
    "Patient-friendly advice formatting",
    "Prototype-safe medical disclaimer",
]


@app.route("/")
def home():
    return render_template("index.html")


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
    return render_template("reports.html", reports=DEMO_REPORTS)


@app.route("/settings")
def settings():
    return render_template("settings.html", settings_preview=SETTINGS_PREVIEW)


if __name__ == "__main__":
    app.run(debug=True)
