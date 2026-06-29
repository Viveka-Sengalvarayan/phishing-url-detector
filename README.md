# 🔍 Phishing URL Detector

A machine learning-based web application that classifies URLs as **Phishing** or **Legitimate** using engineered URL features and a Random Forest classifier.

---

## 📖 Overview

Phishing websites often imitate trusted websites to steal sensitive information such as usernames, passwords, and banking credentials.

This project analyzes URL characteristics and predicts whether a URL is legitimate or phishing using Machine Learning.

---

## ✨ Features

- URL Feature Extraction
- Machine Learning Classification
- Random Forest Algorithm
- Confidence Score
- Trusted Domain Validation
- Interactive Streamlit Web Interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
phishing-url-detector/
│
├── app.py
├── feature_extractor.py
├── train_url_model.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/phishing-url-detector.git
```

Move into the project

```bash
cd phishing-url-detector
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Train the model

```bash
python train_url_model.py
```

Start the Streamlit application

```bash
python -m streamlit run app.py
```

---

## 📷 Screenshots

### Home Page

<img width="1915" height="1080" alt="Screenshot 2026-06-29 215655" src="https://github.com/user-attachments/assets/c5f68bcc-f902-4e40-9a74-3efe109a6211" />


### Prediction Result

Legitimate URL 

<img width="1913" height="1082" alt="Screenshot 2026-06-29 215734" src="https://github.com/user-attachments/assets/b0964f73-78e2-475a-9f3d-97a615afba67" />

Phishing URL

<img width="1912" height="1085" alt="Screenshot 2026-06-29 215717" src="https://github.com/user-attachments/assets/554f7c12-4657-486c-8824-68829e5c6614" />

---

## 📊 Machine Learning

Algorithm:
- Random Forest Classifier

Features Used:
- URL Length
- Domain Length
- HTTPS Detection
- IP Address Detection
- Suspicious Keywords
- Number of Subdomains
- URL Entropy
- Suspicious Top-Level Domains (TLDs)

---

## 📌 Example

Input

```
https://google.com
```

Output

```
Prediction : Legitimate
Confidence : 99.9%
```

Input

```
http://secure-login-google.com
```

Output

```
Prediction : Phishing
Confidence : 89%
```

---

## 🔮 Future Improvements

- Improve model accuracy using advanced feature engineering
- Integrate real-time phishing threat intelligence APIs
- Deploy the application online
- Support additional machine learning models for comparison

---

## 👤 Author

**Viveka Sengalvarayan**

Cybersecurity Student | Python Developer | Machine Learning Enthusiast

---

If you found this project useful, consider giving it a ⭐ on GitHub.
