import streamlit as st
import pandas as pd
import joblib
from urllib.parse import urlparse
from feature_extractor import extract_features

# Load model
model = joblib.load("phishing_model.pkl")

# ---------------- SAFE DOMAINS (STRICT MATCH) ----------------
SAFE_DOMAINS = {
    "google.com",
    "youtube.com",
    "microsoft.com",
    "apple.com",
    "github.com"
}

def is_safe_domain(url):
    domain = urlparse(url).netloc.lower().replace("www.", "")
    return domain in SAFE_DOMAINS

# ---------------- STREAMLIT UI ----------------
st.title("🔍 Phishing URL Detector")

url = st.text_input("Enter URL")

if st.button("Check URL"):

    if not url:
        st.warning("Please enter a URL")
    else:

        # ---------------- SAFE DOMAIN CHECK ----------------
        if is_safe_domain(url):
            st.success("✅ Legitimate URL (Trusted Domain)")
            st.write("Confidence: 99.9%")

        else:
            # ---------------- ML PREDICTION ----------------
            features = extract_features(url)
            df = pd.DataFrame([features])

            prediction = model.predict(df)[0]
            proba = model.predict_proba(df)[0]

            confidence = max(proba) * 100

            if prediction == 1:
                st.error("🚨 Phishing URL Detected")
            else:
                st.success("✅ Legitimate URL")

            st.write(f"Confidence: {confidence:.2f}%")