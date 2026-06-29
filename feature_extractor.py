import re
import math
from urllib.parse import urlparse

SUSPICIOUS_WORDS = {
    "login", "verify", "secure", "account",
    "update", "bank", "signin", "confirm",
    "password", "unlock"
}

SAFE_DOMAINS = {
    "google.com", "youtube.com", "microsoft.com",
    "apple.com", "github.com"
}

SUSPICIOUS_TLDS = {
    ".xyz", ".top", ".click", ".zip", ".loan", ".work", ".rest"
}

# ---------------- ENTROPY FUNCTION ----------------
def url_entropy(url):
    if not url:
        return 0
    prob = [float(url.count(c)) / len(url) for c in set(url)]
    return -sum(p * math.log2(p) for p in prob)

def extract_features(url):

    url = str(url)
    parsed = urlparse(url.lower())
    domain = parsed.netloc.lower()
    url_lower = url.lower()

    features = {}

    # ---------------- BASIC STRUCTURE ----------------
    features["url_length"] = len(url)
    features["domain_length"] = len(domain)
    features["num_dots"] = url.count(".")
    features["num_slashes"] = url.count("/")
    features["num_digits"] = sum(c.isdigit() for c in url)
    features["special_chars"] = sum(not c.isalnum() for c in url)

    # ---------------- SECURITY SIGNALS ----------------
    features["has_https"] = int(url.startswith("https"))
    features["has_ip"] = int(bool(re.search(r"\d+\.\d+\.\d+\.\d+", url)))
    features["has_at"] = int("@" in url)

    # ---------------- SUSPICIOUS WORDS ----------------
    features["suspicious_count"] = sum(
        word in url_lower for word in SUSPICIOUS_WORDS
    )

    features["contains_login"] = int("login" in url_lower)
    features["contains_secure"] = int("secure" in url_lower)
    features["contains_verify"] = int("verify" in url_lower)
    features["contains_bank"] = int("bank" in url_lower)

    # ---------------- DOMAIN STRUCTURE ----------------
    parts = domain.split(".")
    features["subdomains"] = max(len(parts) - 2, 0)

    # ---------------- SAFE DOMAIN ----------------
    features["is_safe_domain"] = int(any(safe in domain for safe in SAFE_DOMAINS))

    # ---------------- NEW HIGH-IMPACT FEATURES ----------------

    # URL randomness (VERY IMPORTANT for phishing detection)
    features["url_entropy"] = url_entropy(url)

    # Suspicious TLD detection
    features["suspicious_tld"] = int(any(tld in url_lower for tld in SUSPICIOUS_TLDS))

    # Short URL flag
    features["is_short_url"] = int(len(url) < 20)

    # Excessive subdomains (phishing indicator)
    features["many_subdomains"] = int(features["subdomains"] > 2)

    return features