# 🏦 AI Loan Eligibility Predictor

An end-to-end AI-powered fintech web application that predicts whether a user is eligible for a loan using machine learning, explainable AI, and an intelligent financial chatbot.

This project demonstrates a production-style system combining:

• Machine Learning model training  
• Explainable AI (SHAP feature impact)  
• Risk scoring engine  
• Full-stack React + Flask architecture  
• LLM-powered financial assistant chatbot  

---

## 🌐 Live Demo

Frontend: https://YOUR-FRONTEND-LINK  
Backend API: https://YOUR-BACKEND-LINK  

---

## 🚀 Features

### 🤖 AI Loan Prediction
- RandomForestClassifier trained on financial dataset
- Predicts loan approval based on income, CIBIL, assets, loan amount, etc.
- Returns approval decision with confidence score

### 📊 Explainable AI (SHAP)
- Shows top factors affecting prediction
- Makes model transparent and interpretable
- Visual feature-impact bar chart

### 🎯 Risk Scoring System
- Converts model confidence into:
  - Low Risk
  - Medium Risk
  - High Risk
- Displayed visually in UI

### 🧠 Smart Explanation Engine
- Human-readable explanation of approval/rejection
- Detects weak financial indicators
- Provides actionable improvement suggestions

### 💬 AI Financial Chatbot
- Uses LLM to answer user queries
- Understands user's specific prediction
- Gives personalized loan advice
- Mimics real banking assistant behavior

### 🎨 Modern Fintech UI
- Built with React + TypeScript + Tailwind
- Glassmorphism design
- Smooth animations
- Interactive charts and indicators
- Responsive layout

---

## 🏗️ Tech Stack

### Frontend
- React (Vite)
- TypeScript
- TailwindCSS
- Recharts
- Lucide Icons

### Backend
- Flask API
- scikit-learn
- SHAP explainability
- Pandas / NumPy
- joblib model persistence
- OpenAI API (chatbot)

### Deployment
- Frontend → Vercel
- Backend → Render / Railway / Cloud VM
- Source Control → GitHub

---

## 📂 Project Structure
# 🏦 AI Loan Eligibility Predictor

An end-to-end AI-powered fintech web application that predicts whether a user is eligible for a loan using machine learning, explainable AI, and an intelligent financial chatbot.

This project demonstrates a production-style system combining:

• Machine Learning model training  
• Explainable AI (SHAP feature impact)  
• Risk scoring engine  
• Full-stack React + Flask architecture  
• LLM-powered financial assistant chatbot  

---

## 🌐 Live Demo

Frontend: https://YOUR-FRONTEND-LINK  
Backend API: https://YOUR-BACKEND-LINK  

---

## 🚀 Features

### 🤖 AI Loan Prediction
- RandomForestClassifier trained on financial dataset
- Predicts loan approval based on income, CIBIL, assets, loan amount, etc.
- Returns approval decision with confidence score

### 📊 Explainable AI (SHAP)
- Shows top factors affecting prediction
- Makes model transparent and interpretable
- Visual feature-impact bar chart

### 🎯 Risk Scoring System
- Converts model confidence into:
  - Low Risk
  - Medium Risk
  - High Risk
- Displayed visually in UI

### 🧠 Smart Explanation Engine
- Human-readable explanation of approval/rejection
- Detects weak financial indicators
- Provides actionable improvement suggestions

### 💬 AI Financial Chatbot
- Uses LLM to answer user queries
- Understands user's specific prediction
- Gives personalized loan advice
- Mimics real banking assistant behavior

### 🎨 Modern Fintech UI
- Built with React + TypeScript + Tailwind
- Glassmorphism design
- Smooth animations
- Interactive charts and indicators
- Responsive layout

---

## 🏗️ Tech Stack

### Frontend
- React (Vite)
- TypeScript
- TailwindCSS
- Recharts
- Lucide Icons

### Backend
- Flask API
- scikit-learn
- SHAP explainability
- Pandas / NumPy
- joblib model persistence
- OpenAI API (chatbot)

### Deployment
- Frontend → Vercel
- Backend → Render / Railway / Cloud VM
- Source Control → GitHub

---

## 📂 Project Structure
# 🏦 AI Loan Eligibility Predictor

An end-to-end AI-powered fintech web application that predicts whether a user is eligible for a loan using machine learning, explainable AI, and an intelligent financial chatbot.

This project demonstrates a production-style system combining:

• Machine Learning model training  
• Explainable AI (SHAP feature impact)  
• Risk scoring engine  
• Full-stack React + Flask architecture  
• LLM-powered financial assistant chatbot  

---

## 🌐 Live Demo

Frontend: https://YOUR-FRONTEND-LINK  
Backend API: https://YOUR-BACKEND-LINK  

---

## 🚀 Features

### 🤖 AI Loan Prediction
- RandomForestClassifier trained on financial dataset
- Predicts loan approval based on income, CIBIL, assets, loan amount, etc.
- Returns approval decision with confidence score

### 📊 Explainable AI (SHAP)
- Shows top factors affecting prediction
- Makes model transparent and interpretable
- Visual feature-impact bar chart

### 🎯 Risk Scoring System
- Converts model confidence into:
  - Low Risk
  - Medium Risk
  - High Risk
- Displayed visually in UI

### 🧠 Smart Explanation Engine
- Human-readable explanation of approval/rejection
- Detects weak financial indicators
- Provides actionable improvement suggestions

### 💬 AI Financial Chatbot
- Uses LLM to answer user queries
- Understands user's specific prediction
- Gives personalized loan advice
- Mimics real banking assistant behavior

### 🎨 Modern Fintech UI
- Built with React + TypeScript + Tailwind
- Glassmorphism design
- Smooth animations
- Interactive charts and indicators
- Responsive layout

---

## 🏗️ Tech Stack

### Frontend
- React (Vite)
- TypeScript
- TailwindCSS
- Recharts
- Lucide Icons

### Backend
- Flask API
- scikit-learn
- SHAP explainability
- Pandas / NumPy
- joblib model persistence
- OpenAI API (chatbot)

### Deployment
- Frontend → Vercel
- Backend → Render / Railway / Cloud VM
- Source Control → GitHub

---

## 📂 Project Structure
fintech-3d-vision
│
├── frontend/ # React UI
│ ├── src/components
│ ├── src/services
│ ├── src/config
│ └── pages
│
├── backend/ # Flask ML API
│ ├── app.py
│ ├── train_model.py
│ ├── loan_model.pkl
│ ├── encoders.pkl
│ └── model_columns.pkl
│
└── README.md


---

## ⚙️ How It Works

1. User enters financial details in UI
2. React sends request to Flask backend
3. Backend:
   - preprocesses input
   - loads trained model
   - predicts approval
   - calculates risk score
   - generates SHAP explanation
4. UI displays:
   - approval result
   - confidence %
   - risk level
   - feature impact chart
5. Chatbot can answer questions about the decision

---

## 🧪 Model Training

The training pipeline:

- Dataset cleaning
- Label encoding
- Train-test split
- RandomForestClassifier training
- Model saved using joblib

Training script:

---

## ⚙️ How It Works

1. User enters financial details in UI
2. React sends request to Flask backend
3. Backend:
   - preprocesses input
   - loads trained model
   - predicts approval
   - calculates risk score
   - generates SHAP explanation
4. UI displays:
   - approval result
   - confidence %
   - risk level
   - feature impact chart
5. Chatbot can answer questions about the decision

---

## 🧪 Model Training

The training pipeline:

- Dataset cleaning
- Label encoding
- Train-test split
- RandomForestClassifier training
- Model saved using joblib

Training script:
backend/train_model.py


---

## 📈 Future Improvements

- Bank-grade credit scoring logic
- Model retraining dashboard
- Multiple ML models comparison
- Document upload verification
- Fraud detection module
- Production authentication layer

---

## 👨‍💻 Author

**Ayush**

AI / ML Enthusiast  
Building real-world AI systems with explainability and production deployment.

GitHub: https://github.com/YOUR_USERNAME  
LinkedIn: Add your link here

---

## ⭐ If you like this project

Give it a star — it helps a lot.