
# 1️⃣ Latest Research Papers on URL-Based Phishing Detection

### 1. Recent survey on URL-based phishing detection (2025)

* **Topic:** ML detection using only URL features
* **Key idea:** URL-only analysis is lightweight and can detect **zero-day phishing attacks** without visiting the webpage. ([ResearchGate][1])

Good starting point for research.

Search title:
**“Machine Learning-Based Phishing Detection Using URL Features: A Comprehensive Review” (2025)**

---

### 2. Real-Time Phishing URL Detection Using ML (2025)

* Uses **235k URLs with 54 features**
* Uses ML models like **Random Forest, SVM, XGBoost**. ([MDPI][2])

Search title:
**“Real-Time Phishing URL Detection Using Machine Learning”**

---

### 3. Feature-Based Phishing URL Detection (2025)

* Uses **lexical, host-based, and content features**
* Multiple ML classifiers used for detection. ([ETASR][3])

Search title:
**“A Feature-Based Methodology for Detecting Phishing URLs”**

---

### 4. Character-level CNN + ML ensemble (2025)

* Uses **36 URL features**
* Accuracy **~99.8%** using CNN + LightGBM. ([arXiv][4])

Search title:
**“Phishing Detection System: Ensemble Approach Using Character-Level CNN”**

---

# 2️⃣ Main URL Features That Indicate Phishing

Most research divides features into **3 categories**.

---

## 1. Lexical Features (URL text structure)

These are **very important for ML models**.

Examples:

* URL length
* Number of dots
* Number of subdomains
* Presence of **@ symbol**
* Presence of **- (hyphen)** in domain
* Number of digits in URL
* Suspicious keywords

  * login
  * verify
  * secure
  * update
* Repeated characters
* Encoding (`%20`, `%3A`)

Example phishing URL:

```
https://paypal-login-secure.verify-user.ru/account
```

Problems:

* too many subdomains
* suspicious words
* wrong TLD

Research shows lexical features alone can detect many phishing URLs. ([ScienceDirect][5])

---

## 2. Host-Based Features

These require **domain lookup / DNS analysis**.

Examples:

* Domain age
* WHOIS registration
* DNS records
* IP address instead of domain
* Hosting country
* Domain expiration

Example:

```
http://192.168.2.44/login
```

Using IP instead of domain is suspicious.

---

## 3. Statistical / Structural Features

These analyze **patterns in URL structure**.

Examples:

* Token count
* Entropy of characters
* TLD type (.xyz, .top, .ru often used)
* URL path depth
* ratio of digits to letters

---

# 3️⃣ Free Datasets You Should Use (Important for your ML module)

Good **free phishing databases**:

### Phishing URLs

* **PhishTank**
* **OpenPhish**
* **URLHaus**

### Legitimate URLs

* **Alexa Top 1M**
* **Tranco list**
* **Majestic Million**

Researchers commonly combine phishing datasets with legitimate domain lists. ([ScienceDirect][6])

---

# 4️⃣ Well-Known Researchers / Experts

Look at papers by these researchers:

* **Bhavani Thuraisingham** – cybersecurity ML research
* **B. B. Gupta** – phishing detection research
* **S. Garera** – malicious URL detection
* **Prateek Saxena** – web security research

These authors appear frequently in phishing detection papers.

---

# 5️⃣ Best GitHub Projects to Study

Search for:

```
phishing url detection machine learning github
```

Good repos usually include:

* feature extraction scripts
* datasets
* trained models
* evaluation

---

# 6️⃣ Features You Should Implement in Your Project

For your **React + Python ML Phish Detection Engine**, start with:

Minimum features (easy):

```
url_length
num_dots
num_hyphens
num_subdomains
has_ip
has_at_symbol
num_digits
tld
suspicious_words
path_depth
```

Then feed into:

```
RandomForest
XGBoost
LogisticRegression
```

---

# 7️⃣ Suggested Architecture for Your Project

```
React Frontend
     ↓
API request
     ↓
Python FastAPI / Flask
     ↓
URL Feature Extraction
     ↓
ML Model
     ↓
Threat Intelligence Check
     ↓
Return JSON result
```

---



##### © 2026 Kunal Harshad Patil