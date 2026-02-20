import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Loading dataset...")

df = pd.read_csv("loan_approval_dataset.csv")

if "loan_id" in df.columns:
    df.drop(columns=["loan_id"], inplace=True)

df.columns = df.columns.str.strip()

# -----------------------------
# CLEAN DATA
# -----------------------------
df["education"] = df["education"].astype(str).str.strip().str.lower()
df["self_employed"] = df["self_employed"].astype(str).str.strip().str.lower()

# -----------------------------
# FIXED TARGET MAPPING (IMPORTANT)
# -----------------------------
df["loan_status"] = df["loan_status"].astype(str).str.strip().str.lower()

df["loan_status"] = df["loan_status"].map({
    "approved": 1,
    "rejected": 0
})

# -----------------------------
# ENCODE FEATURES ONLY
# -----------------------------
encoders = {}

for col in ["education", "self_employed"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# -----------------------------
# SPLIT
# -----------------------------
X = df.drop(columns=["loan_status"])
y = df["loan_status"]

columns = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# TRAIN
# -----------------------------
print("Training model...")

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# EVAL
# -----------------------------
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))

# -----------------------------
# SAVE
# -----------------------------
joblib.dump(model, "loan_model.pkl")
joblib.dump(encoders, "encoders.pkl")
joblib.dump(columns, "model_columns.pkl")

print("Model saved successfully.")
