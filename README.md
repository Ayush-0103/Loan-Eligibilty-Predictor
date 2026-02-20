<h1>🏦 AI Loan Eligibility Predictor</h1>

<p>
An end-to-end <b>AI-powered fintech web application</b> that predicts whether a user is eligible for a loan using machine learning, explainable AI, and an intelligent financial chatbot.
</p>

<p>This project demonstrates a <b>production-style system</b> combining:</p>
<ul>
<li>Machine Learning model training</li>
<li>Explainable AI (SHAP feature impact)</li>
<li>Risk scoring engine</li>
<li>Full-stack React + Flask architecture</li>
<li>LLM-powered financial assistant chatbot</li>
</ul>

<hr>

<h2>🌐 Live Demo</h2>
<p>
Frontend: https://YOUR-FRONTEND-LINK<br>
Backend API: https://YOUR-BACKEND-LINK
</p>

<hr>

<h2>🚀 Features</h2>

<h3>🤖 AI Loan Prediction</h3>
<ul>
<li>RandomForestClassifier trained on financial dataset</li>
<li>Predicts loan approval using income, CIBIL score, assets, loan amount, etc.</li>
<li>Returns approval decision with confidence score</li>
</ul>

<h3>📊 Explainable AI (SHAP)</h3>
<ul>
<li>Displays top factors affecting prediction</li>
<li>Makes model transparent and interpretable</li>
<li>Visual feature-impact bar chart</li>
</ul>

<h3>🎯 Risk Scoring System</h3>
<ul>
<li>Low Risk</li>
<li>Medium Risk</li>
<li>High Risk</li>
</ul>
<p>Displayed visually in the UI.</p>

<h3>🧠 Smart Explanation Engine</h3>
<ul>
<li>Human-readable approval/rejection explanation</li>
<li>Detects weak financial indicators</li>
<li>Provides actionable improvement suggestions</li>
</ul>

<h3>💬 AI Financial Chatbot</h3>
<ul>
<li>Uses LLM to answer user queries</li>
<li>Understands user’s prediction context</li>
<li>Provides personalized loan advice</li>
<li>Mimics real banking assistant behavior</li>
</ul>

<h3>🎨 Modern Fintech UI</h3>
<ul>
<li>React + TypeScript + Tailwind</li>
<li>Glassmorphism design</li>
<li>Smooth animations</li>
<li>Interactive charts and indicators</li>
<li>Responsive layout</li>
</ul>

<hr>

<h2>🏗️ Tech Stack</h2>

<h3>Frontend</h3>
<ul>
<li>React (Vite)</li>
<li>TypeScript</li>
<li>TailwindCSS</li>
<li>Recharts</li>
<li>Lucide Icons</li>
</ul>

<h3>Backend</h3>
<ul>
<li>Flask API</li>
<li>scikit-learn</li>
<li>SHAP explainability</li>
<li>Pandas / NumPy</li>
<li>joblib model persistence</li>
<li>OpenAI API (chatbot)</li>
</ul>

<h3>Deployment</h3>
<ul>
<li>Frontend → Vercel</li>
<li>Backend → Render / Railway / Cloud VM</li>
<li>Source Control → GitHub</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
fintech-3d-vision
│
├── frontend/                 # React UI
│   ├── src/components
│   ├── src/services
│   ├── src/config
│   └── pages
│
├── backend/                  # Flask ML API
│   ├── app.py
│   ├── train_model.py
│   ├── loan_model.pkl
│   ├── encoders.pkl
│   └── model_columns.pkl
│
└── README.md
</pre>

<hr>

<h2>⚙️ How It Works</h2>

<ol>
<li>User enters financial details in UI</li>
<li>React sends request to Flask backend</li>
</ol>

<p><b>Backend workflow:</b></p>
<ul>
<li>Preprocesses input</li>
<li>Loads trained model</li>
<li>Predicts approval</li>
<li>Calculates risk score</li>
<li>Generates SHAP explanation</li>
</ul>

<p><b>Frontend displays:</b></p>
<ul>
<li>Approval result</li>
<li>Confidence percentage</li>
<li>Risk level</li>
<li>Feature-impact chart</li>
</ul>

<p>The chatbot can also answer questions about the decision.</p>

<hr>

<h2>🧪 Model Training</h2>

<p>Training pipeline includes:</p>
<ul>
<li>Dataset cleaning</li>
<li>Label encoding</li>
<li>Train-test split</li>
<li>RandomForestClassifier training</li>
<li>Model persistence using joblib</li>
</ul>

<p><b>Run training script:</b></p>

<pre>python backend/train_model.py</pre>

<hr>

<h2>📈 Future Improvements</h2>
<ul>
<li>Bank-grade credit scoring logic</li>
<li>Model retraining dashboard</li>
<li>Multiple ML model comparison</li>
<li>Document upload verification</li>
<li>Fraud detection module</li>
<li>Production authentication layer</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Ayush</b><br>
AI / ML Enthusiast<br>
Building real-world AI systems with explainability and production deployment.
</p>

<p>
GitHub: https://github.com/YOUR_USERNAME<br>
LinkedIn: Add your link here
</p>

<hr>

<h2>⭐ If you like this project</h2>
<p>Give it a star — it really helps.</p>
