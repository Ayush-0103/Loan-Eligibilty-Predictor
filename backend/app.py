from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import shap
import numpy as np
import os
from dotenv import load_dotenv
from openai import OpenAI
from flask import send_file
from io import BytesIO


# -----------------------------
# LOAD ENV + OPENAI
# -----------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app)

# -----------------------------
# LOAD MODEL FILES
# -----------------------------
model = joblib.load("loan_model.pkl")
encoders = joblib.load("encoders.pkl")
columns = joblib.load("model_columns.pkl")

explainer = shap.TreeExplainer(model)

# Store last prediction for chatbot context
last_prediction_context = {}

# -----------------------------
# ROOT
# -----------------------------
@app.route("/")
def home():
    return "Backend running"

# -----------------------------
# HELPER: CLEAN + ENCODE INPUT
# -----------------------------
def preprocess_input(data_dict):

    df = pd.DataFrame([data_dict])

    numeric_cols = [
        'no_of_dependents','income_annum','loan_amount','loan_term',
        'cibil_score','residential_assets_value','commercial_assets_value',
        'luxury_assets_value','bank_asset_value'
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    raw = df.copy()

    # Encode categorical safely
    for col in df.columns:
        if col in encoders:
            df[col] = df[col].astype(str).str.strip().str.lower()
            known = [c.lower().strip() for c in encoders[col].classes_]
            df[col] = df[col].apply(lambda x: x if x in known else known[0])
            df[col] = encoders[col].transform(df[col])

    # Ensure missing columns filled
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    df = df[columns]

    return df, raw


# -----------------------------
# HELPER: HUMAN EXPLANATION
# -----------------------------
def generate_explanation(prediction, raw):

    text = []
    advice = []

    # safely extract values
    cibil = float(raw.get("cibil_score", [0])[0])
    income = float(raw.get("income_annum", [0])[0])
    loan = float(raw.get("loan_amount", [0])[0])

    total_assets = (
        float(raw.get("residential_assets_value", [0])[0]) +
        float(raw.get("commercial_assets_value", [0])[0]) +
        float(raw.get("luxury_assets_value", [0])[0]) +
        float(raw.get("bank_asset_value", [0])[0])
    )

    # -----------------------------
    # APPROVED CASE
    # -----------------------------
    if prediction == 0:

        if cibil >= 750:
            text.append("Excellent credit score strongly supported approval.")
        elif cibil >= 700:
            text.append("Good credit score improved approval chances.")

        if income >= loan * 2:
            text.append("Income comfortably supports loan repayment.")
        elif income >= loan:
            text.append("Income level is adequate for repayment.")

        if total_assets > loan:
            text.append("Strong asset coverage reduced perceived lending risk.")

        # fallback if nothing triggered
        if not text:
            text.append("Your financial profile meets lending criteria.")

    # -----------------------------
    # REJECTED CASE
    # -----------------------------
    else:

        if cibil < 600:
            text.append("Very low credit score increased default risk.")
            advice.append("Improve CIBIL score above 700 before reapplying.")

        elif cibil < 650:
            text.append("Credit score is below preferred lending threshold.")
            advice.append("Pay dues on time to raise your score.")

        if loan > income * 2:
            text.append("Requested loan is too high relative to income.")
            advice.append("Consider applying for a smaller loan amount.")

        elif loan > income:
            text.append("Loan amount is high compared to annual income.")
            advice.append("Increasing income or reducing loan size may help.")

        if total_assets < loan:
            text.append("Limited asset backing weakens repayment security.")
            advice.append("Adding collateral or assets may improve approval.")

        # fallback
        if not text:
            text.append("The model detected higher repayment risk in your profile.")
            advice.append("Review credit score, income stability and collateral.")

    # -----------------------------
    # FINAL STRUCTURED TEXT
    # -----------------------------
    explanation = " ".join(text)

    if advice:
        explanation += " Suggested actions: " + " ".join(advice)

    return explanation



# -----------------------------
# HELPER: SHAP FEATURE IMPORTANCE
# -----------------------------
def get_shap_features(df):

    shap_vals = explainer.shap_values(df)

    if isinstance(shap_vals, list):
        shap_vals = shap_vals[1]

    shap_vals = np.array(shap_vals).flatten()
    abs_vals = np.abs(shap_vals)

    min_len = min(len(columns), len(abs_vals))

    shap_df = pd.DataFrame({
        "feature": columns[:min_len],
        "impact": abs_vals[:min_len]
    }).sort_values(by="impact", ascending=False).head(5)

    labels = shap_df["feature"].tolist()
    values = shap_df["impact"].round(4).tolist()

    return labels, values


# -----------------------------
# PREDICT ROUTE
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    data = request.form.to_dict()

    df, raw = preprocess_input(data)

    # Prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0].max()

    result = "Loan Approved" if prediction == 0 else "Loan Rejected"

    # Risk calculation
    risk = (
        "High Risk" if probability < 0.6
        else "Medium Risk" if probability < 0.8
        else "Low Risk"
    )

    # Human readable explanation
    explanation_text = generate_explanation(prediction, raw)

    # SHAP chart
    labels, values = get_shap_features(df)

    # Save context for chatbot
    global last_prediction_context
    last_prediction_context = {
        "prediction": result,
        "risk": risk,
        "confidence": round(probability * 100, 2),
        "inputs": raw.to_dict(orient="records")[0],
        "top_features": labels
    }

    return jsonify({
        "prediction_text": result,
        "confidence": round(probability * 100, 2),
        "risk_level": risk,
        "explanation_text": explanation_text,
        "chart_labels": labels,
        "chart_values": values
    })

@app.route("/report", methods=["POST"])
def generate_report():

    global last_prediction_context

    if not last_prediction_context:
        return jsonify({"error": "No prediction available"}), 400

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Loan Eligibility Analysis Report")
    y -= 40

    p.setFont("Helvetica", 11)

    p.drawString(50, y, f"Prediction: {last_prediction_context['prediction']}")
    y -= 20
    p.drawString(50, y, f"Risk Level: {last_prediction_context['risk']}")
    y -= 20
    p.drawString(50, y, f"Confidence: {last_prediction_context['confidence']}%")
    y -= 40

    p.setFont("Helvetica-Bold", 13)
    p.drawString(50, y, "User Inputs")
    y -= 25

    p.setFont("Helvetica", 10)

    for key, val in last_prediction_context["inputs"].items():
        p.drawString(60, y, f"{key.replace('_',' ').title()}: {val}")
        y -= 18

        if y < 80:
            p.showPage()
            p.setFont("Helvetica", 10)
            y = 750

    y -= 20
    p.setFont("Helvetica-Bold", 13)
    p.drawString(50, y, "Key Influencing Factors")
    y -= 25

    p.setFont("Helvetica", 10)

    for feat in last_prediction_context["top_features"]:
        p.drawString(60, y, f"- {feat.replace('_',' ').title()}")
        y -= 18

    y -= 20
    p.setFont("Helvetica-Bold", 13)
    p.drawString(50, y, "Improvement Suggestions")
    y -= 25

    p.setFont("Helvetica", 10)

    # smart suggestions
    inputs = last_prediction_context["inputs"]

    if inputs["cibil_score"] < 700:
        p.drawString(60, y, "- Improve CIBIL score above 700")
        y -= 18

    if inputs["loan_amount"] > inputs["income_annum"]:
        p.drawString(60, y, "- Reduce loan amount relative to income")
        y -= 18

    total_assets = (
        inputs["residential_assets_value"] +
        inputs["commercial_assets_value"] +
        inputs["luxury_assets_value"] +
        inputs["bank_asset_value"]
    )

    if total_assets < inputs["loan_amount"]:
        p.drawString(60, y, "- Increase collateral/assets before applying")
        y -= 18

    if y < 80:
        p.showPage()

    p.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Loan_Report.pdf",
        mimetype="application/pdf"
    )


# -----------------------------
# REAL LLM CHATBOT
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}
    user_msg = data.get("message", "")

    global last_prediction_context

    context_text = ""
    if last_prediction_context:
        context_text = f"""
Loan Result:
Prediction: {last_prediction_context['prediction']}
Risk Level: {last_prediction_context['risk']}
Confidence: {last_prediction_context['confidence']}%
User Inputs: {last_prediction_context['inputs']}
Important Features: {last_prediction_context['top_features']}
"""

    prompt = f"""
You are a professional bank loan advisor.

Explain clearly, simply, and give actionable advice.

{context_text}

User question: {user_msg}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
