# 📁 Backend Architecture (Module-Based Design)

```id="arch_struct"
backend/
│
├── app.py                          # API entry point
│
├── modules/
│   ├── __init__.py
│   ├── pipeline.py                 #  main orchestrator
│
│   ├── validator.py                # Input Validation Module
│   ├── feature_extractor.py        # Feature Extraction Engine
│
│   ├── ml_engine.py                # Machine Learning Detection
│   ├── threat_intel.py             # Threat Intelligence Check
│
│   ├── evaluator.py                # Final Risk Evaluation
│   ├── scorer.py                   # Risk Score Generation
│
│   ├── response_builder.py         # Final JSON response formatting
│
├── models/
│   ├── phishing_url_model.pkl
│   ├── feature_columns.pkl
│
├── config/
│   ├── settings.py                 # API keys, thresholds
│
├── utils/
│   ├── helpers.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
└── README.md
```

---

# 🧠 Module Mapping to Flow Digram 

| Diagram Module        | Backend File         |
| --------------------- | -------------------- |
| Input Validation      | validator.py         |
| Feature Extraction    | feature_extractor.py |
| ML Detection          | ml_engine.py         |
| Threat Intelligence   | threat_intel.py      |
| Prediction Score      | ml_engine.py         |
| Reputation Result     | threat_intel.py      |
| Final Risk Evaluation | evaluator.py         |
| Risk Score Generation | scorer.py            |
| Result Dashboard      | response_builder.py  |

---

# 🔥 Module Responsibilities

---

## 🔹 validator.py

* Accept JSON input
* Validate and clean URL

---

## 🔹 feature_extractor.py

* Convert URL → feature vector
* (Your 23 features)

---

## 🔹 ml_engine.py

* Load model
* Predict:

  * label (0/1)
  * probability

---

## 🔹 threat_intel.py

* Check URL using:

  * OpenPhish
  * URLhaus
  * PhishTank
* Return:

  * malicious / safe
  * source confidence

---

## 🔹 evaluator.py

* Combine:

  * ML result
  * Threat intelligence result
* Decide final risk

---

## 🔹 scorer.py

* Generate:

  * Risk score (0–100)
  * Risk level:

    * Low
    * Medium
    * High

---

## 🔹 response_builder.py

* Format final JSON response
* Send to frontend

---

## 🔹 pipeline.py (CORE 🔥)

```text
Controls full system flow:
validate → extract → ML → threat → evaluate → score → response
```

---

# 🧠 IMPORTANT DESIGN DECISION

```text id="key_insight"
Pipeline is NOT linear only  
ML + Threat Intel run in parallel conceptually
```

But in code:

```text id="impl"
We call both → then combine results
```

---

# 🔄 FINAL SYSTEM FLOW 

```id="flow_final"
User Input
   ↓
Validation
   ↓
Feature Extraction
   ↓
ML Engine ───────┐
                 ├──→ Evaluator → Scorer → Response
Threat Intel ────┘
```

---

# 🐳 Docker Compatibility

* Entire backend runs inside container
* All modules bundled
* Easy deployment

---

