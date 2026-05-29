# Medical AI Advisor Prototype

This project is a polished Flask prototype for a symptom-checking assistant.
It is designed for academic demos, UI showcases, and basic triage-flow presentations.

## Demo Highlights

- Clean dashboard-style interface
- Structured symptom analysis cards
- Emergency escalation screen
- Demo reports page for presentation storytelling
- Settings preview to make the prototype feel product-ready

## Important Note

This is a prototype only.
It does not provide a real medical diagnosis and should not replace licensed medical advice.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`

## Deploy To Vercel

This repo is configured for Vercel Python Functions.

### Files used for Vercel

- `api/index.py`
- `vercel.json`
- `requirements.txt`

### Steps

1. Push this project to GitHub.
2. Go to [Vercel](https://vercel.com/).
3. Click `Add New Project`.
4. Import the GitHub repository.
5. Keep the framework preset as `Other`.
6. Click `Deploy`.

Vercel will route all requests through the Flask app automatically.
