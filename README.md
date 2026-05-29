# Medical AI Advisor Prototype

[![Python](https://img.shields.io/badge/Python-3.x-2f6690?style=for-the-badge)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_App-0f766e?style=for-the-badge)](https://flask.palletsprojects.com/)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-1d1d1d?style=for-the-badge)](https://vercel.com/)
[![Status](https://img.shields.io/badge/Status-Prototype-c58b2a?style=for-the-badge)](#important-disclaimer)

A polished Flask-based medical chatbot prototype built for academic demonstration, symptom triage flow presentation, and UI showcase purposes.

This project accepts symptom descriptions in natural language, checks for emergency warning patterns, and returns a structured care summary with likely concern areas, urgency level, red-flag symptoms, and follow-up questions.

## Live Demo

Add your deployed Vercel link here after deployment:

```text
https://your-project-name.vercel.app
```

## Overview

The goal of this prototype is to demonstrate how an AI-assisted healthcare interface could support:

- symptom intake through free-text input
- first-level triage guidance
- emergency escalation when dangerous symptoms are detected
- patient-friendly result presentation
- a dashboard-style product experience suitable for demos

## Key Features

- Clean dashboard UI for a more professional prototype presentation
- Symptom analysis with structured response sections
- Emergency keyword detection and escalation flow
- Result page with risk level, urgency, possible conditions, and care advice
- Demo-ready extra pages such as `Emergency`, `Reports`, and `Settings`
- Mobile-friendly responsive layout
- Vercel deployment support

## Screenshots

Add screenshots after deployment to make the GitHub page more impressive.

Suggested images:

- `Dashboard`
- `Symptom Analysis Result`
- `Emergency Escalation Page`
- `Reports Page`

Example section format:

```md
![Dashboard](./screenshots/dashboard.png)
![Result](./screenshots/result.png)
```

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- Vercel Python Functions

## Project Structure

```text
Medical_ChatBot/
├── api/
│   └── index.py
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   ├── base.html
│   ├── emergency.html
│   ├── index.html
│   ├── reports.html
│   ├── result.html
│   └── settings.html
├── app.py
├── chatbot_logic.py
├── emergency_detector.py
├── prompts.py
├── requirements.txt
└── vercel.json
```

## How It Works

1. The user enters symptoms in natural language.
2. The app checks whether any emergency indicators are present.
3. If an emergency signal is detected, the prototype shows urgent escalation guidance.
4. Otherwise, the app matches the symptom description to predefined triage patterns.
5. The result page displays:
   - likely condition categories
   - risk level
   - urgency
   - care advice
   - red-flag symptoms
   - follow-up questions

## Important Disclaimer

This project is a prototype for academic and demonstration use only.

It does **not** provide a real medical diagnosis, does **not** replace a licensed doctor, and should **not** be used for real clinical decision-making.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd Medical_ChatBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Flask app

```bash
python app.py
```

### 4. Open in browser

```text
http://127.0.0.1:5000
```

## Deploy on Vercel

This project is already configured for Vercel.

### Deployment Steps

1. Push the project to your GitHub repository.
2. Open [Vercel](https://vercel.com/).
3. Click `Add New Project`.
4. Import your GitHub repository.
5. Keep the framework preset as `Other`.
6. Click `Deploy`.

### Vercel Files Included

- `api/index.py` to expose the Flask app as a Python Function
- `vercel.json` to route all requests to the Flask entrypoint

## Use Cases

- Academic mini project demonstration
- AI in healthcare concept presentation
- Symptom triage workflow prototype
- Faculty viva or project review showcase
- Portfolio project for Flask and frontend integration

## Demo Presentation Tips

If your friend is showing this project to faculty or during a viva, this flow will work well:

1. Open the dashboard and explain the product idea.
2. Enter a normal symptom case such as `fever and cough for 2 days`.
3. Show the structured analysis result.
4. Enter an emergency example such as `chest pain and shortness of breath`.
5. Open the `Emergency` page to show escalation behavior.
6. Open `Reports` and `Settings` to make the prototype feel like a full product.

## Future Improvements

- connect to a real medical knowledge base
- add user authentication
- store case history in a database
- support multilingual input
- add doctor/hospital recommendation logic
- improve explainability with charts and case summaries

## Credits

- Original project by the repository owner
- Prototype refinement, UI polishing, and deployment preparation completed for demo readiness
