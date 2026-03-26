# Frontend ↔ Backend — Connection Documentation

---

## Table of Contents

- [Frontend ↔ Backend — Connection Documentation](#frontend--backend--connection-documentation)
  - [Table of Contents](#table-of-contents)
  - [1. Overview](#1-overview)
  - [2. Running Both Together](#2-running-both-together)
  - [3. How Frontend Calls the Backend](#3-how-frontend-calls-the-backend)
  - [4. API Contract](#4-api-contract)
    - [Request](#request)
    - [Success Response](#success-response)
    - [Error Response](#error-response)
    - [Risk Level Mapping](#risk-level-mapping)
  - [5. CORS Configuration](#5-cors-configuration)
  - [6. Environment Variables — Both Sides](#6-environment-variables--both-sides)
  - [7. Common Connection Issues](#7-common-connection-issues)

---

## 1. Overview

The frontend and backend are two separate applications that run independently and communicate over HTTP.

still in development, the frontend runs on `http://localhost:5173` and the backend runs on `http://localhost:5000`. The frontend sends API requests to the backend to analyze URLs, and the backend processes these requests and returns JSON responses.

```

User Browser
     ↓
React Frontend (http://localhost:5173)
     ↓  POST /analyze
Flask Backend (http://localhost:5000)
     ↓
Pipeline → ML Model + Threat Intel
     ↓
JSON Response
     ↑
React Frontend renders result
```

---

## 2. Running Both Together

Both servers must be running at the same time for the application to work. Open two separate terminal windows.

**Terminal 1 — Backend:**
```bash
cd backend
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
python app.py
```
Backend runs at: `http://localhost:5000`

**Terminal 2 — Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs at: `http://localhost:5173` still in development mode, so you can make changes and see them reflected immediately.

---

## 3. How Frontend Calls the Backend

The frontend sends the URL to the backend via a single POST request. This is handled in `src/api/analyzeURL.js`.

**Flow:**
```
URLInputForm (user submits URL)
      ↓
useURLAnalysis hook (TanStack Query mutation)
      ↓
analyzeURL.js (axios POST)
      ↓
POST http://localhost:5000/analyze
      ↓
Flask backend processes and returns JSON
      ↓
TanStack Query receives response
      ↓
Zustand store saves result
      ↓
Dashboard components render
```

The backend URL is read from the frontend environment variable `VITE_BACKEND_URL` defined in `frontend/.env`.

---

## 4. API Contract

This is the agreed request and response format between frontend and backend. Neither side should change field names without informing the other.

---

### Request

```
POST http://localhost:5000/analyze
Content-Type: application/json
```

```json
{
  "url": "http://secure-login-paypal-update.xyz"
}
```

---

### Success Response

```json
{
  "url": "http://secure-login-paypal-update.xyz",
  "timestamp": "2026-03-26T10:30:00Z",

  "validation": {
    "is_valid": true,
    "protocol": "http",
    "domain": "secure-login-paypal-update.xyz"
  },

  "features": {
    "url_length": 38,
    "hyphen_count": 3,
    "suspicious_keywords": ["login", "secure", "paypal", "update"],
    "tld": ".xyz",
    "has_ip_address": false,
    "has_at_symbol": false,
    "subdomain_count": 0,
    "is_https": false,
    "special_char_count": 3
  },

  "ml_prediction": {
    "score": 82,
    "label": "phishing",
    "confidence": "high"
  },

  "threat_intelligence": {
    "virustotal": {
      "found": false,
      "malicious_count": 0,
      "total_engines": 90
    },
    "phishtank": {
      "found": true,
      "verified": true
    },
    "openphish": {
      "found": false
    }
  },

  "risk": {
    "score": 75,
    "level": "Suspicious",
    "reasons": [
      "Suspicious keywords detected: login, secure, paypal",
      "Multiple hyphens in domain",
      "Unusual top-level domain (.xyz)",
      "Non-HTTPS connection",
      "Found in PhishTank database"
    ]
  }
}
```

---

### Error Response

```json
{
  "url": "http://secure-login-paypal-update.xyz",
  "timestamp": "2026-03-26T10:30:00Z",
  "error": true,
  "message": "Analysis failed at feature extraction stage."
}
```

---

### Risk Level Mapping

| Score Range | Level | Frontend Color |
|---|---|---|
| 0 – 30 | Safe | Green |
| 31 – 70 | Suspicious | Yellow |
| 71 – 100 | Malicious | Red |

---

## 5. CORS Configuration

CORS (Cross-Origin Resource Sharing) must be configured on the backend to allow the frontend to make requests. Without this the browser will block all API calls.

**Backend `app.py` — already configured:**
```python
from flask_cors import CORS
CORS(app, origins=["http://localhost:5173"])
```

**For production deployment:** replace `http://localhost:5173` with the actual deployed frontend URL.

---

## 6. Environment Variables — Both Sides

**Frontend — `frontend/.env`:**
```
VITE_BACKEND_URL=http://localhost:5000
VITE_VIRUSTOTAL_API_KEY=your_key_here
VITE_PHISHTANK_API_KEY=your_key_here
VITE_OPENPHISH_FEED_URL=https://openphish.com/feed.txt
```

**Backend — `backend/.env`:**
```
FLASK_DEBUG=true
PORT=5000
VIRUSTOTAL_API_KEY=your_key_here
PHISHTANK_API_KEY=your_key_here
```

> Both `.env` files are in `.gitignore` and must never be committed. Use the `.env.example` files as templates.

---

## 7. Common Connection Issues

| Issue | Cause | Fix |
|---|---|---|
| `Network Error` in browser | Backend not running | Start backend with `python app.py` |
| `CORS error` in browser console | CORS not configured on backend | Make sure `flask-cors` is installed and `CORS(app)` is in `app.py` |
| `404 Not Found` | Wrong endpoint URL | Confirm frontend is calling `/analyze` not `/predict` |
| `undefined` API response | Field name mismatch | Check response field names match the agreed JSON contract |
| Frontend not connecting after `.env` change | Vite caches env vars | Stop dev server and run `npm run dev` again |
| Backend returns `500` error | Pipeline module error | Check backend terminal for the Python traceback |

---