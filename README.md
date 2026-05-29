# Medical AI Advisor Prototype

[![Python](https://img.shields.io/badge/Python-3.x-2f6690?style=for-the-badge)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_App-0f766e?style=for-the-badge)](https://flask.palletsprojects.com/)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-1d1d1d?style=for-the-badge)](https://vercel.com/)

A Flask-based medical chatbot prototype for symptom input, emergency detection, and structured triage-style guidance.

## Overview

This project lets a user describe symptoms in natural language and receive a structured response that includes:

- possible condition categories
- risk level
- urgency
- care advice
- red-flag symptoms
- follow-up questions

The app also includes separate pages for emergency guidance, reports, and settings to make the prototype more complete for presentation.

## Features

- Symptom input using free-text form
- Emergency keyword detection
- Structured medical response layout
- Separate dashboard, result, emergency, reports, and settings pages
- Responsive interface
- Vercel-ready configuration

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript

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

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Deploy on Vercel

This project includes:

- `api/index.py`
- `vercel.json`

Deployment steps:

1. Push the project to GitHub.
2. Open [Vercel](https://vercel.com/).
3. Import the GitHub repository.
4. Keep the framework preset as `Other`.
5. Deploy the project.

## Disclaimer

This project is a prototype for academic and demonstration purposes only.

It does not provide a real medical diagnosis and should not be used as a replacement for professional medical advice.

## Credits

- Original repository by the project owner
- Prototype refinement and deployment setup added for demo readiness
