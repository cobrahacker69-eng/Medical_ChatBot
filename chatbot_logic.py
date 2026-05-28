def analyze_symptoms(symptoms):

    symptoms = symptoms.lower()

    # ======================================================
    # FEVER + COUGH
    # ======================================================
    if "fever" in symptoms and "cough" in symptoms:
        return """
🩺 Possible Conditions:
• Viral Fever
• Flu
• COVID-19
• Respiratory Infection

📊 Risk Level:
Medium Risk

💊 Advice:
• Drink warm fluids
• Take proper rest
• Steam inhalation recommended

🚨 Emergency Signs:
• Difficulty breathing
• High fever above 103°F
"""

    # ======================================================
    # HEADACHE
    # ======================================================
    elif "headache" in symptoms:
        return """
🩺 Possible Conditions:
• Migraine
• Stress
• Dehydration
• Sinus Infection

📊 Risk Level:
Low to Medium Risk

💊 Advice:
• Sleep properly
• Stay hydrated
• Reduce screen exposure
"""

    # ======================================================
    # CHEST PAIN
    # ======================================================
    elif "chest pain" in symptoms:
        return """
🩺 Possible Conditions:
• Heart Attack
• Anxiety Attack
• Acid Reflux

📊 Risk Level:
High Risk

🚨 Seek immediate medical help.
"""

    # ======================================================
    # STOMACH PAIN
    # ======================================================
    elif "stomach pain" in symptoms:
        return """
🩺 Possible Conditions:
• Gastric Infection
• Food Poisoning
• Acidity
• Ulcer

📊 Risk Level:
Medium Risk

💊 Advice:
• Eat light food
• Avoid oily items
• Drink clean water
"""

    # ======================================================
    # DIABETES
    # ======================================================
    elif "frequent urination" in symptoms or "excessive thirst" in symptoms:
        return """
🩺 Possible Conditions:
• Diabetes
• High Blood Sugar

📊 Risk Level:
Medium to High Risk

💊 Advice:
• Reduce sugar intake
• Exercise regularly
• Monitor glucose level
"""

    # ======================================================
    # DENGUE
    # ======================================================
    elif "body pain" in symptoms and "high fever" in symptoms:
        return """
🩺 Possible Conditions:
• Dengue
• Malaria
• Viral Fever

📊 Risk Level:
High Risk

💊 Advice:
• Stay hydrated
• Blood test recommended

🚨 Watch for bleeding symptoms.
"""

    # ======================================================
    # ASTHMA
    # ======================================================
    elif "shortness of breath" in symptoms:
        return """
🩺 Possible Conditions:
• Asthma
• Allergy
• Lung Infection

📊 Risk Level:
High Risk

💊 Advice:
• Avoid dust and smoke
• Use inhaler if prescribed
"""

    # ======================================================
    # SKIN ALLERGY
    # ======================================================
    elif "skin rash" in symptoms or "itching" in symptoms:
        return """
🩺 Possible Conditions:
• Allergy
• Fungal Infection
• Heat Rash

📊 Risk Level:
Low Risk

💊 Advice:
• Keep skin dry
• Avoid scratching
"""

    # ======================================================
    # TYPHOID
    # ======================================================
    elif "weakness" in symptoms and "fever" in symptoms:
        return """
🩺 Possible Conditions:
• Typhoid
• Viral Infection

📊 Risk Level:
Medium Risk

💊 Advice:
• Eat healthy food
• Drink boiled water
"""

    # ======================================================
    # FOOD POISONING
    # ======================================================
    elif "vomiting" in symptoms and "diarrhea" in symptoms:
        return """
🩺 Possible Conditions:
• Food Poisoning
• Gastroenteritis

📊 Risk Level:
Medium Risk

💊 Advice:
• ORS recommended
• Stay hydrated
"""

    # ======================================================
    # HYPERTENSION
    # ======================================================
    elif "dizziness" in symptoms and "blurred vision" in symptoms:
        return """
🩺 Possible Conditions:
• High Blood Pressure
• Stress Disorder

📊 Risk Level:
Medium Risk

💊 Advice:
• Reduce salt intake
• Monitor blood pressure
"""

    # ======================================================
    # ANEMIA
    # ======================================================
    elif "fatigue" in symptoms and "pale skin" in symptoms:
        return """
🩺 Possible Conditions:
• Anemia
• Iron Deficiency

📊 Risk Level:
Medium Risk

💊 Advice:
• Eat iron-rich food
• Blood test advised
"""

    # ======================================================
    # KIDNEY STONE
    # ======================================================
    elif "back pain" in symptoms and "painful urination" in symptoms:
        return """
🩺 Possible Conditions:
• Kidney Stone
• Urinary Infection

📊 Risk Level:
High Risk

💊 Advice:
• Drink plenty of water
"""

    # ======================================================
    # DEPRESSION
    # ======================================================
    elif "sadness" in symptoms or "stress" in symptoms:
        return """
🩺 Possible Conditions:
• Stress
• Anxiety
• Depression

📊 Risk Level:
Medium Risk

💊 Advice:
• Take proper sleep
• Practice meditation
"""

    # ======================================================
    # COLD / ALLERGY
    # ======================================================
    elif "sneezing" in symptoms and "runny nose" in symptoms:
        return """
🩺 Possible Conditions:
• Cold
• Allergy

📊 Risk Level:
Low Risk

💊 Advice:
• Drink warm fluids
"""

    # ======================================================
    # EYE INFECTION
    # ======================================================
    elif "red eyes" in symptoms:
        return """
🩺 Possible Conditions:
• Eye Infection
• Conjunctivitis

📊 Risk Level:
Low Risk

💊 Advice:
• Avoid touching eyes
"""

    # ======================================================
    # PNEUMONIA
    # ======================================================
    elif "cough" in symptoms and "chest tightness" in symptoms:
        return """
🩺 Possible Conditions:
• Pneumonia
• Lung Infection

📊 Risk Level:
High Risk

💊 Advice:
• Medical consultation needed
"""

    # ======================================================
    # APPENDICITIS
    # ======================================================
    elif "lower right stomach pain" in symptoms:
        return """
🩺 Possible Conditions:
• Appendicitis

📊 Risk Level:
High Risk

🚨 Immediate medical attention required.
"""

    # ======================================================
    # ARTHRITIS
    # ======================================================
    elif "joint pain" in symptoms:
        return """
🩺 Possible Conditions:
• Arthritis
• Joint Inflammation

📊 Risk Level:
Medium Risk

💊 Advice:
• Gentle exercise
• Avoid heavy strain
"""

    # ======================================================
    # SINUSITIS
    # ======================================================
    elif "facial pain" in symptoms and "blocked nose" in symptoms:
        return """
🩺 Possible Conditions:
• Sinusitis

📊 Risk Level:
Low to Medium Risk

💊 Advice:
• Steam inhalation
• Warm fluids
"""

    # ======================================================
    # UTI
    # ======================================================
    elif "burning urination" in symptoms:
        return """
🩺 Possible Conditions:
• Urinary Tract Infection

📊 Risk Level:
Medium Risk

💊 Advice:
• Drink more water
• Maintain hygiene
"""

    # ======================================================
    # THYROID
    # ======================================================
    elif "weight gain" in symptoms and "fatigue" in symptoms:
        return """
🩺 Possible Conditions:
• Thyroid Disorder

📊 Risk Level:
Medium Risk

💊 Advice:
• Thyroid test recommended
"""

    # ======================================================
    # INSOMNIA
    # ======================================================
    elif "difficulty sleeping" in symptoms:
        return """
🩺 Possible Conditions:
• Insomnia
• Stress

📊 Risk Level:
Low to Medium Risk

💊 Advice:
• Avoid caffeine
• Sleep on time
"""

    # ======================================================
    # EAR INFECTION
    # ======================================================
    elif "ear pain" in symptoms:
        return """
🩺 Possible Conditions:
• Ear Infection

📊 Risk Level:
Low to Medium Risk

💊 Advice:
• Avoid inserting objects into ear
"""

    # ======================================================
    # DEHYDRATION
    # ======================================================
    elif "dry mouth" in symptoms and "dizziness" in symptoms:
        return """
🩺 Possible Conditions:
• Dehydration

📊 Risk Level:
Medium Risk

💊 Advice:
• Drink water and ORS
"""

    # ======================================================
    # MIGRAINE
    # ======================================================
    elif "sensitivity to light" in symptoms:
        return """
🩺 Possible Conditions:
• Migraine

📊 Risk Level:
Medium Risk

💊 Advice:
• Rest in dark room
"""

    # ======================================================
    # FALLBACK
    # ======================================================
    else:
        return """
🤖 More information required.

Please provide:
• Symptom duration
• Severity
• Age
• Additional symptoms

Example:
"I have fever and cough for 2 days."
"""