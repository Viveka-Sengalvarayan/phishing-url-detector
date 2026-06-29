import pandas as pd
from feature_extractor import extract_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

print("Loading dataset...")

df = pd.read_csv("phishing_site_urls.csv")

# Optional: reduce dataset for speed
df = df.sample(n=50000, random_state=42)

print("Checking labels...")
print(df["Label"].value_counts())

print("Extracting features...")

feature_list = []

for url in df["URL"]:
    feature_list.append(extract_features(str(url)))

X = pd.DataFrame(feature_list)

# Convert labels
y = df["Label"].map({
    "good": 0,
    "bad": 1
})

print("Resetting index to avoid mismatch...")

# IMPORTANT FIX (prevents your error)
X = X.reset_index(drop=True)
y = y.reset_index(drop=True)

# Remove invalid labels
valid_mask = y.notnull()

X = X.loc[valid_mask].reset_index(drop=True)
y = y.loc[valid_mask].astype(int).reset_index(drop=True)

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced_subsample"
)

model.fit(X_train, y_train)

print("Evaluating model...")

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("Saving model...")

joblib.dump(model, "phishing_model.pkl")

print("Training complete! Model saved as phishing_model.pkl")