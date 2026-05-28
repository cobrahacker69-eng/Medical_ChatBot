from flask import Flask, render_template, request
from chatbot_logic import analyze_symptoms
from emergency_detector import detect_emergency

app = Flask(__name__)

# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():
    return render_template('index.html')

# =========================
# CHAT ANALYSIS
# =========================

@app.route('/analyze', methods=['POST'])
def analyze():

    symptoms = request.form['symptoms']

    emergency = detect_emergency(symptoms)

    if emergency:

        result = """
🚨 EMERGENCY DETECTED

Possible serious medical condition.

Please contact emergency services immediately.
"""

    else:

        result = analyze_symptoms(symptoms)

    return render_template(
        'result.html',
        result=result,
        symptoms=symptoms
    )

# =========================
# EMERGENCY PAGE
# =========================

@app.route('/emergency')
def emergency():

    return render_template('emergency.html')

# =========================
# REPORTS PAGE
# =========================

@app.route('/reports')
def reports():

    return render_template('reports.html')

# =========================
# SETTINGS PAGE
# =========================

@app.route('/settings')
def settings():

    return render_template('settings.html')

# =========================

if __name__ == '__main__':
    app.run(debug=True)