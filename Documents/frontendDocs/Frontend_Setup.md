# Smart Phishing Detection & URL Risk Analyzer
## Frontend — File Structure, Installation & Setup Guide

> **Project:** Smart Phishing Detection & URL Risk Analyzer (Web-Based)
> **Bundler:** Vite
> **Framework:** React.js
> **Node Version Required:** >= 18.0.0

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Complete File Structure](#2-complete-file-structure)
3. [File & Folder Purpose Reference](#3-file--folder-purpose-reference)
4. [Cloning the Repository](#4-cloning-the-repository)
5. [Installing Dependencies](#5-installing-dependencies)
6. [Environment Variables Setup](#6-environment-variables-setup)
7. [Running the Project](#7-running-the-project)
8. [Building for Production](#8-building-for-production)
9. [Common Errors & Fixes](#9-common-errors--fixes)
10. [Dependency Reference](#10-dependency-reference)

---

## 1. Prerequisites

Before setting up this project on your device, make sure the following are installed.

---

### 1.1 Node.js

This project requires **Node.js version 18 or higher**.

Check your current version:
```bash
node --version
```

If not installed or version is below 18, download from: https://nodejs.org

> Recommended: Use the **LTS (Long Term Support)** version for stability.

---

### 1.2 npm

npm comes bundled with Node.js. Check your version:
```bash
npm --version
```

Minimum required: npm version 8 or higher.

---

### 1.3 Git

Git is required to clone the repository.

Check if installed:
```bash
git --version
```

Download from: https://git-scm.com if not installed.

---

### 1.4 Code Editor

Recommended: **Visual Studio Code**
Download from: https://code.visualstudio.com

Recommended VS Code extensions for this project:
- ESLint
- Prettier - Code formatter
- Tailwind CSS IntelliSense
- ES7+ React/Redux/React-Native snippets

---

## 2. Complete File Structure

This is the complete file and folder structure of the frontend after setup.

```
phishing-detector-frontend/
│
├── public/
│   ├── favicon.ico                   # Browser tab icon
│   └── robots.txt                    # Search engine crawling rules
│
├── src/
│   │
│   ├── api/                          # All external API call functions
│   │   ├── index.js                  # Re-exports all API functions from one place
│   │   ├── analyzeURL.js             # POST request to your backend for full analysis
│   │   ├── virusTotal.js             # VirusTotal API — URL reputation check
│   │   ├── phishTank.js              # PhishTank API — phishing database check
│   │   └── openPhish.js              # OpenPhish API — real-time phishing feed check
│   │
│   ├── assets/                       # Static assets bundled by Vite
│   │   ├── images/
│   │   │   └── logo.svg              # App logo
│   │   └── icons/                    # Any custom SVG icons
│   │
│   ├── components/                   # All reusable UI components
│   │   │
│   │   ├── common/                   # Shared components used across all pages
│   │   │   ├── Navbar.jsx            # Top navigation bar
│   │   │   ├── Footer.jsx            # Bottom footer with credits and links
│   │   │   ├── Loader.jsx            # Loading spinner component
│   │   │   ├── ErrorMessage.jsx      # Styled error display box
│   │   │   └── Badge.jsx             # Risk level badge (Safe / Suspicious / Malicious)
│   │   │
│   │   ├── url-input/                # URL submission UI
│   │   │   ├── URLInputForm.jsx      # Input field + form logic using react-hook-form
│   │   │   ├── URLInputForm.test.jsx # Unit tests for input validation
│   │   │   └── SubmitButton.jsx      # Analyze button with loading state
│   │   │
│   │   ├── dashboard/                # Analysis result visualization
│   │   │   ├── RiskDashboard.jsx     # Parent container for all result sections
│   │   │   ├── RiskScoreGauge.jsx    # Circular/arc gauge showing risk % (Recharts)
│   │   │   ├── RiskReasonsList.jsx   # Bullet list of risk reasons from JSON
│   │   │   └── AnalyzedURLCard.jsx   # Card showing URL, timestamp, risk badge
│   │   │
│   │   ├── features/                 # Feature extraction result display
│   │   │   ├── FeatureBreakdown.jsx  # Section wrapper for feature table
│   │   │   ├── FeatureTable.jsx      # Table showing all extracted URL features
│   │   │   └── FeatureBadge.jsx      # Per-feature indicator badge (normal/suspicious)
│   │   │
│   │   ├── threat/                   # Threat intelligence result display
│   │   │   ├── ThreatIntelPanel.jsx  # Panel showing all threat source results
│   │   │   ├── ThreatSourceCard.jsx  # Card per source: VirusTotal, PhishTank, OpenPhish
│   │   │   └── ThreatStatusIcon.jsx  # Found (red warning) or Not Found (green check)
│   │   │
│   │   └── history/                  # Analysis history components
│   │       ├── HistoryList.jsx       # Full list of past analyses
│   │       ├── HistoryItem.jsx       # Single entry: URL, badge, score, date, actions
│   │       └── ClearHistoryButton.jsx # Clears all history with confirmation
│   │
│   ├── pages/                        # Route-level page components
│   │   ├── Home.jsx                  # Landing page — introduction and CTA
│   │   ├── Analyzer.jsx              # Main analysis page — input + result dashboard
│   │   ├── Result.jsx                # Detailed result view from history
│   │   ├── History.jsx               # Page showing all past analyses
│   │   └── NotFound.jsx              # 404 page for unknown routes
│   │
│   ├── hooks/                        # Custom React hooks
│   │   ├── useURLAnalysis.js         # TanStack Query mutation hook for analysis API call
│   │   ├── useURLValidation.js       # Reusable client-side URL validation logic
│   │   └── useHistory.js             # Read/write/delete from history in Zustand store
│   │
│   ├── store/                        # Zustand global state stores
│   │   ├── analysisStore.js          # Stores current result + history (persisted)
│   │   └── uiStore.js                # Stores UI state: loading, modals, visibility
│   │
│   ├── utils/                        # Pure helper/utility functions
│   │   ├── urlHelpers.js             # URL parsing, truncation, formatting
│   │   ├── riskHelpers.js            # Score to risk level conversion function
│   │   ├── formatDate.js             # Human-readable timestamp formatting
│   │   └── constants.js             # App-wide constants: risk thresholds, labels, colors
│   │
│   ├── schema/                       # Zod input validation schemas
│   │   └── urlSchema.js              # URL validation schema used by react-hook-form
│   │
│   ├── config/                       # App-wide configuration
│   │   ├── apiConfig.js              # API base URLs and keys (reads from .env)
│   │   └── queryClient.js            # TanStack Query client configuration
│   │
│   ├── styles/                       # Global CSS
│   │   └── index.css                 # Tailwind CSS base, components, utilities imports
│   │
│   ├── routes/                       # Routing configuration
│   │   └── AppRoutes.jsx             # All react-router-dom route definitions
│   │
│   ├── App.jsx                       # Root app component — wraps providers and routes
│   └── main.jsx                      # Vite entry point — mounts App to DOM
│
├── .env                              # Your actual environment variables (NEVER commit this)
├── .env.example                      # Template showing required env variables (safe to commit)
├── .gitignore                        # Files and folders excluded from Git
├── index.html                        # HTML entry point (Vite injects React here)
├── package.json                      # Project metadata and dependency list
├── package-lock.json                 # Exact locked versions of all installed packages
├── vite.config.js                    # Vite bundler configuration
├── tailwind.config.js                # Tailwind CSS configuration
├── postcss.config.js                 # PostCSS configuration (required for Tailwind)
├── eslint.config.js                  # ESLint rules for code quality
└── README.md                         # Project readme
```

---

## 3. File & Folder Purpose Reference

| File / Folder | What It Does |
|---|---|
| `src/api/` | Contains all functions that make HTTP requests. Never make API calls directly inside components. |
| `src/components/` | All UI building blocks. Each subfolder is a feature area. |
| `src/pages/` | One file per route. Pages import and arrange components. They do not contain business logic. |
| `src/hooks/` | Custom hooks abstract API calls and store access away from components. |
| `src/store/` | Zustand stores hold shared state. `analysisStore` is persisted to localStorage. |
| `src/utils/` | Pure functions with no side effects. Can be used anywhere. |
| `src/schema/` | Zod schemas define and enforce input validation rules. |
| `src/config/` | Configuration objects. API keys and TanStack Query setup live here. |
| `src/routes/` | All route definitions in one place. Makes routing easy to manage and extend. |
| `.env` | Holds your real API keys and URLs. Never push this to GitHub. |
| `.env.example` | A copy of `.env` with placeholder values. Safe to commit. Tells team members what variables they need. |
| `vite.config.js` | Configures Vite: port, build settings, path aliases. |
| `tailwind.config.js` | Tells Tailwind where to scan for class names (content paths). |

---

## 4. Cloning the Repository

### Step 1 — Clone the repo

```bash
git clone https://github.com/your-username/phishing-detector-frontend.git
```

### Step 2 — Navigate into the project folder

```bash
cd phishing-detector-frontend
```

### Step 3 — Switch to your working branch

Since each team member works on their own branch:

```bash
git checkout your-branch-name
```

Example:
```bash
git checkout frontend-dev
```

---

## 5. Installing Dependencies

### Step 1 — Create the Vite React project (only for initial setup)

> Skip this step if you are cloning an existing repo that already has `package.json`.

```bash
npm create vite@latest phishing-detector-frontend -- --template react
cd phishing-detector-frontend
```

---

### Step 2 — Create all required source folders

Run this single command from the project root to create the entire folder structure at once:

```bash
mkdir -p src/api src/assets/images src/assets/icons src/components/common src/components/url-input src/components/dashboard src/components/features src/components/threat src/components/history src/pages src/hooks src/store src/utils src/schema src/config src/styles src/routes
```

---

### Step 3 — Install production dependencies

```bash
npm install react-router-dom axios @tanstack/react-query zustand react-hook-form zod @hookform/resolvers lucide-react framer-motion recharts react-hot-toast
```

What each package does:

| Package | Purpose |
|---|---|
| `react-router-dom` | Client-side routing between pages |
| `axios` | HTTP client for API calls |
| `@tanstack/react-query` | Server state management — fetch, cache, sync |
| `zustand` | Lightweight global state management |
| `react-hook-form` | Performant form handling |
| `zod` | Schema-based input validation |
| `@hookform/resolvers` | Connects Zod schema to react-hook-form |
| `lucide-react` | Clean SVG icon library |
| `framer-motion` | UI animations and transitions |
| `recharts` | Chart library for risk score gauge |
| `react-hot-toast` | Toast notification system |

---

### Step 4 — Install development dependencies

```bash
npm install -D tailwindcss postcss autoprefixer eslint prettier eslint-plugin-react
```

| Package | Purpose |
|---|---|
| `tailwindcss` | Utility-first CSS framework |
| `postcss` | CSS transformation tool (required by Tailwind) |
| `autoprefixer` | Adds vendor prefixes to CSS automatically |
| `eslint` | Code linting to catch errors |
| `prettier` | Automatic code formatting |
| `eslint-plugin-react` | React-specific ESLint rules |

---

### Step 5 — Initialize Tailwind CSS

```bash
npx tailwindcss init -p
```

This creates two files: `tailwind.config.js` and `postcss.config.js`.

Now update `tailwind.config.js` to tell Tailwind where your files are:

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

### Step 6 — Add Tailwind directives to your CSS

Open `src/styles/index.css` (or `src/index.css`) and replace its contents with:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Make sure this file is imported in `src/main.jsx`:

```javascript
import './styles/index.css'
```

---

### Step 7 — Verify all packages installed correctly

```bash
npm list --depth=0
```

You should see all installed packages listed without errors.

---

## 6. Environment Variables Setup

### Step 1 — Create your `.env` file

In the root of the project (same level as `package.json`), create a file named `.env`:

```bash
touch .env
```

### Step 2 — Add your environment variables

Open `.env` and add the following:

```
# Backend API
VITE_BACKEND_URL=http://localhost:5000

# VirusTotal API
# Get your key at: https://www.virustotal.com/gui/my-apikey
VITE_VIRUSTOTAL_API_KEY=your_virustotal_api_key_here

# PhishTank API
# Register and get key at: https://www.phishtank.com/api_register.php
VITE_PHISHTANK_API_KEY=your_phishtank_api_key_here
```

### Step 3 — Create the `.env.example` file

This file is safe to commit to GitHub. It tells team members what variables they need without exposing real keys:

```
# Backend API
VITE_BACKEND_URL=http://localhost:5000

# VirusTotal API
# Get your key at: https://www.virustotal.com/gui/my-apikey
VITE_VIRUSTOTAL_API_KEY=

# PhishTank API
# Register at: https://www.phishtank.com/api_register.php
VITE_PHISHTANK_API_KEY=
```

### Step 4 — Make sure `.env` is in `.gitignore`

Open `.gitignore` and confirm these lines are present:

```
.env
.env.local
.env.*.local
```

> **CRITICAL:** Never commit your `.env` file with real API keys. If you accidentally push it, regenerate your API keys immediately.

### Important Notes on Vite Environment Variables

- All variables **must start with `VITE_`** to be accessible in the browser
- Access them in code using: `import.meta.env.VITE_VARIABLE_NAME`
- After changing `.env`, you must **restart the dev server** for changes to take effect
- These variables are embedded in the build at compile time — they are visible in the browser bundle

---

## 7. Running the Project

### Start the development server

```bash
npm run dev
```

The app will be available at:
```
http://localhost:5173
```

> Vite uses port 5173 by default. If that port is in use, Vite will automatically try the next available port.

### To change the default port

Open `vite.config.js` and add:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,       // Change to any port you want
    open: true,       // Automatically opens browser on start
  }
})
```

---

## 8. Building for Production

### Create a production build

```bash
npm run build
```

This generates a `dist/` folder containing optimized static files ready for deployment.

### Preview the production build locally

```bash
npm run preview
```

This serves the `dist/` folder locally so you can test the production build before deploying.

### What the build produces

```
dist/
├── index.html
├── assets/
│   ├── index-[hash].js     # Bundled and minified JavaScript
│   └── index-[hash].css    # Bundled and minified CSS
```

---

## 9. Common Errors & Fixes

---

### Error: `'vite' is not recognized as a command`

**Cause:** Dependencies not installed.

**Fix:**
```bash
npm install
```

---

### Error: `Cannot find module 'react-router-dom'` (or any other package)

**Cause:** Package not installed.

**Fix:**
```bash
npm install react-router-dom
```

---

### Error: Environment variable is `undefined` in the browser

**Cause:** Variable name does not start with `VITE_`, or dev server was not restarted after `.env` change.

**Fix:**
1. Make sure the variable name starts with `VITE_`
2. Stop the dev server with `Ctrl + C`
3. Run `npm run dev` again

---

### Error: Tailwind classes not applying

**Cause:** `tailwind.config.js` content paths are wrong, or CSS file is not imported.

**Fix:**
1. Check `tailwind.config.js` content array includes `"./src/**/*.{js,ts,jsx,tsx}"`
2. Make sure `index.css` with Tailwind directives is imported in `main.jsx`

---

### Error: `Module not found: Error: Can't resolve './styles/index.css'`

**Cause:** CSS import path in `main.jsx` does not match the actual file location.

**Fix:** Check the import path in `main.jsx`:
```javascript
import './styles/index.css'   // if file is in src/styles/
// OR
import './index.css'          // if file is directly in src/
```

---

### Error: CORS error when calling backend API

**Cause:** Backend is not configured to allow requests from `http://localhost:5173`.

**Fix:** Ask your backend teammate to add `http://localhost:5173` to their CORS allowed origins.

---

### Error: `localStorage is not defined`

**Cause:** This would only happen in server-side rendering environments. Vite React is client-side only, so this should not occur. If it does, check that Zustand persist is configured correctly.

---

## 10. Dependency Reference

Complete list of all dependencies with versions for reference.

### Production Dependencies

```json
{
  "react": "^18.x",
  "react-dom": "^18.x",
  "react-router-dom": "^6.x",
  "axios": "^1.x",
  "@tanstack/react-query": "^5.x",
  "zustand": "^4.x",
  "react-hook-form": "^7.x",
  "zod": "^3.x",
  "@hookform/resolvers": "^3.x",
  "lucide-react": "^0.x",
  "framer-motion": "^11.x",
  "recharts": "^2.x",
  "react-hot-toast": "^2.x"
}
```

### Development Dependencies

```json
{
  "vite": "^5.x",
  "@vitejs/plugin-react": "^4.x",
  "tailwindcss": "^3.x",
  "postcss": "^8.x",
  "autoprefixer": "^10.x",
  "eslint": "^8.x",
  "prettier": "^3.x",
  "eslint-plugin-react": "^7.x"
}
```

---

### Quick Setup Summary (All Steps in Order)

```bash
# 1. Clone and enter the project
git clone https://github.com/your-username/phishing-detector-frontend.git
cd phishing-detector-frontend

# 2. Install all dependencies
npm install

# 3. Create .env file and add your API keys
cp .env.example .env
# then open .env and fill in your actual keys

# 4. Start the development server
npm run dev

# 5. Open in browser
# http://localhost:5173
```

---

*© 2026 Samarjeet Sambhaji Sabale — Smart Phishing Detection & URL Risk Analyzer*
