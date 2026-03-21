# Smart Phishing Detection & URL Risk Analyzer
## Frontend — Overview & Working Documentation

> **Project:** Smart Phishing Detection & URL Risk Analyzer (Web-Based)
> **Frontend Role:** UI, User Interaction, API Handling, Result Visualization

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Tech Stack](#2-tech-stack)
3. [Application Pages](#3-application-pages)
4. [Component Architecture](#4-component-architecture)
5. [Data Flow & Pipeline](#5-data-flow--pipeline)
6. [API Handling](#6-api-handling)
7. [State Management](#7-state-management)
8. [JSON Data Structure](#8-json-data-structure)
9. [URL Validation](#9-url-validation)
10. [Risk Scoring Logic](#10-risk-scoring-logic)
11. [Result Visualization Dashboard](#11-result-visualization-dashboard)
12. [History Feature](#12-history-feature)
13. [Error Handling](#13-error-handling)
14. [Security Considerations](#14-security-considerations)

---

## 1. Project Overview

The frontend is a web-based React application that acts as the interface between the user and the phishing detection engine.

The frontend is responsible for:

- Accepting a URL from the user
- Validating the URL structure on the client side before any API call
- Sending the URL to the backend and receiving the analysis result
- Displaying a clear visual risk assessment to the user
- Maintaining a local history of previously analyzed URLs

The frontend does not run any machine learning model. It communicates with the backend which handles ML prediction and returns results in a standardized JSON format.

---

## 2. Tech Stack

| Category | Technology | Purpose |
|---|---|---|
| UI Framework | React.js (Vite) | Component-based UI |
| Styling | Tailwind CSS | Utility-first responsive styling |
| Routing | react-router-dom | Page navigation |
| API Calls | Axios | HTTP requests to backend and threat APIs |
| Server State | TanStack Query | Fetch, cache, and sync API responses |
| Global State | Zustand | Store current result and history |
| Persistence | Zustand persist middleware | Save history to localStorage |
| Form Handling | react-hook-form | URL input form management |
| Validation | Zod + @hookform/resolvers | URL schema validation |
| Charts | Recharts | Risk score visualization |
| Icons | lucide-react | Security-themed iconography |
| Animations | framer-motion | Smooth UI transitions |
| Notifications | react-hot-toast | Toast alerts for errors and success |

---

## 3. Application Pages

---

### 3.1 Home Page — `/`

Landing page that introduces the tool. Contains a headline, brief description of the purpose, a call-to-action button to the Analyzer, and a simple three-step explanation of how the system works.

---

### 3.2 Analyzer Page — `/analyzer`

Core page of the application. Contains the URL input form. Once the user submits a URL, the analysis runs and the full result dashboard appears below the input on the same page.

---

### 3.3 Result Page — `/result/:id`

Shows the detailed result of a specific past analysis. Pulls data from the Zustand history store using the entry ID — no new API call is made.

---

### 3.4 History Page — `/history`

Shows a list of all past URL analyses stored in the browser. Each entry displays the URL, risk badge, risk score, and timestamp. Users can view a full result, delete individual entries, or clear all history.

---

### 3.5 Not Found Page — `/*`

Standard 404 page shown for any unknown route. Contains a back-to-home button.

---

## 4. Component Architecture

Components are organized by feature area. Each folder contains only components related to that specific section of the UI.

---

### 4.1 Common — `src/components/common/`

Shared components used across all pages.

| Component | Purpose |
|---|---|
| `Navbar.jsx` | Top navigation bar with links to all pages |
| `Footer.jsx` | Footer with project name, author, and social links |
| `Loader.jsx` | Animated spinner shown during API calls |
| `ErrorMessage.jsx` | Reusable styled error display box |
| `Badge.jsx` | Color-coded risk level badge — Safe, Suspicious, Malicious |

---

### 4.2 URL Input — `src/components/url-input/`

| Component | Purpose |
|---|---|
| `URLInputForm.jsx` | Main input form with validation using react-hook-form and Zod |
| `SubmitButton.jsx` | Analyze button that shows a loading state and is disabled during requests |

---

### 4.3 Dashboard — `src/components/dashboard/`

| Component | Purpose |
|---|---|
| `RiskDashboard.jsx` | Parent container that arranges all result sections |
| `RiskScoreGauge.jsx` | Arc gauge showing the numeric risk score as a percentage |
| `RiskReasonsList.jsx` | List of human-readable reasons explaining the risk score |
| `AnalyzedURLCard.jsx` | Card showing the analyzed URL, timestamp, and risk badge |

---

### 4.4 Features — `src/components/features/`

| Component | Purpose |
|---|---|
| `FeatureBreakdown.jsx` | Section wrapper for the feature extraction results |
| `FeatureTable.jsx` | Table showing all extracted URL features and their values |
| `FeatureBadge.jsx` | Per-feature indicator showing normal or suspicious status |

---

### 4.5 Threat Intelligence — `src/components/threat/`

| Component | Purpose |
|---|---|
| `ThreatIntelPanel.jsx` | Parent panel showing all threat source results together |
| `ThreatSourceCard.jsx` | Individual card per source: VirusTotal, PhishTank, OpenPhish |
| `ThreatStatusIcon.jsx` | Icon showing Found (red) or Not Found (green) per source |

---

### 4.6 History — `src/components/history/`

| Component | Purpose |
|---|---|
| `HistoryList.jsx` | Renders the full list of past analyses |
| `HistoryItem.jsx` | Single row showing URL, badge, score, date, and action buttons |
| `ClearHistoryButton.jsx` | Clears all history with a confirmation step |

---

## 5. Data Flow & Pipeline

```
User submits URL
      ↓
Client-side Zod validation
      ↓ (invalid → show inline error, stop)
      ↓ (valid → continue)
Axios sends URL to backend
      ↓
Backend returns unified JSON
      ↓
TanStack Query caches the response (5 min)
      ↓
Zustand stores current result + appends to history
      ↓
Zustand persist saves history to localStorage
      ↓
Components read from Zustand and render the dashboard
```

---

## 6. API Handling

All API calls are centralized in `src/api/`. Components never call APIs directly — they go through custom hooks which use TanStack Query internally.

| File | Responsibility |
|---|---|
| `analyzeURL.js` | POST to backend — main analysis entry point |
| `virusTotal.js` | GET to VirusTotal URL reputation API |
| `phishTank.js` | POST to PhishTank phishing database |
| `openPhish.js` | GET to OpenPhish real-time feed |
| `index.js` | Re-exports all API functions from one place |

All base URLs and keys are read from environment variables via `src/config/apiConfig.js`. Nothing is hardcoded.

> **Note:** VirusTotal free API is limited to 4 requests per minute. This should be rate-limited and proxied from the backend — not called directly from the browser.

---

## 7. State Management

Two Zustand stores manage all shared state.

---

### 7.1 Analysis Store — `src/store/analysisStore.js`

Stores the current analysis result and full history of past analyses. Persisted to localStorage automatically. Capped at 50 entries — oldest is dropped when limit is exceeded.

---

### 7.2 UI Store — `src/store/uiStore.js`

Manages UI-only state such as loading indicators and modal visibility. Not persisted to localStorage.

---

## 8. JSON Data Structure

This is the standardized JSON the frontend expects from the backend. **This schema must be agreed upon with the backend team before development starts on either side.**

```json
{
  "url": "http://secure-login-paypal-update.xyz",
  "timestamp": "2026-03-21T10:30:00Z",

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

## 9. URL Validation

Client-side validation runs via Zod before any API call is triggered. Errors show inline below the input field.

| Check | Example | Result |
|---|---|---|
| Empty input | (blank) | Invalid |
| Missing protocol | paypal-login.com | Invalid |
| Valid HTTP URL | http://secure-login.xyz | Valid |
| Valid HTTPS URL | https://paypal.com | Valid |
| Exceeds 2048 characters | very long URL | Invalid |

---

## 10. Risk Scoring Logic

The risk score is a number 0–100 returned from the backend. The frontend maps it to a level and color defined in `src/utils/constants.js`.

| Score Range | Level | Color |
|---|---|---|
| 0 – 30 | Safe | Green |
| 31 – 70 | Suspicious | Yellow |
| 71 – 100 | Malicious | Red |

---

## 11. Result Visualization Dashboard

The dashboard presents the full JSON result visually, split into five sections.

**Section 1 — URL Summary Card**
Analyzed URL, date/time of analysis, and a large colored risk level badge.

**Section 2 — Risk Score Gauge**
Arc gauge built with Recharts showing the score from 0–100. Arc color reflects the risk level.

**Section 3 — Risk Reasons**
Bulleted list of reasons pulled from `risk.reasons` in the JSON response.

**Section 4 — Feature Breakdown Table**
All extracted URL features with values and a per-feature badge indicating normal or suspicious.

**Section 5 — Threat Intelligence Panel**
Three cards for VirusTotal, PhishTank, and OpenPhish showing whether the URL was found in each database.

---

## 12. History Feature

All past analyses are stored in the browser via localStorage using Zustand persist.

**What is stored per entry:** full JSON result, timestamp, risk level and score.

**Behavior:**
- Max 50 entries — oldest dropped when exceeded
- Browser-local only — does not sync across devices
- Viewing a past result loads from store — no new API call made
- Clearing browser localStorage will wipe all history

---

## 13. Error Handling

| Scenario | Behavior |
|---|---|
| Invalid URL format | Inline error shown below input, no API call made |
| Network failure | TanStack Query retries once, then shows error toast |
| Backend error response | Error message shown in ErrorMessage component |
| VirusTotal rate limit | Toast: "Threat check unavailable. Try again shortly." |
| Unexpected error | Fallback toast: "Analysis failed. Please try again." |

---

## 14. Security Considerations

| Concern | Approach |
|---|---|
| API keys in browser | Sensitive keys like VirusTotal proxied through backend — never called from browser directly |
| XSS via URL content | Analyzed URLs always rendered as plain text, never as HTML |
| Open redirect | Frontend never auto-redirects user to the analyzed URL |
| localStorage data | Only analysis metadata stored — no credentials or sensitive data |
| CORS | Backend must whitelist only the frontend domain in production |

---

*© Samarjeet Sambhaji Sabale — Smart Phishing Detection & URL Risk Analyzer*
