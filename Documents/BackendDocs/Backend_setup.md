# Backend — Setup Guide
---

## Prerequisites

- Python 3.10 or higher
- pip
- Git

Check versions:
```bash
python --version
pip --version
```

---

## Setup Steps

### 1. Navigate to backend folder
```bash
cd backend
```

### 2. Create and activate a virtual environment
```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
# Copy the example file
cp .env.example .env
```
Open `.env` and fill in your API keys.

### 5. Run the backend server
```bash
python app.py
```

Server runs at: `http://localhost:5000` : still in development mode, so you can make changes and see them reflected immediately.

---

## Verify It's Running

Open browser or use any API client and hit:
```
GET http://localhost:5000/
```
You should see: `Backend is running`

---

## Available Endpoint

| Method | Route | Description |
|---|---|---|
| POST | `/analyze` | Submit a URL for full phishing analysis |

**Request body:**
```json
{ "url": "http://suspicious-site.xyz" }
```

---

## Environment Variables Reference

| Variable | Required | Description |
|---|---|---|
| `FLASK_DEBUG` | No | Set to `true` for development |
| `PORT` | No | Port to run Flask on (default 5000) |
| `VIRUSTOTAL_API_KEY` | Yes | VirusTotal API key |
| `PHISHTANK_API_KEY` | Yes | PhishTank API key |

---