# Smart Phishing URL Analyzer - Testing Commands

**Project:** Smart Phishing URL Analyzer  
**Date:** May 2026  
**Total Commands:** 41 Ready-to-Paste Tests

---

## Table of Contents

1. [Category A: Legitimate URLs](#category-a-legitimate-urls-)
2. [Category B: Suspicious Misspellings](#category-b-suspicious-misspellings-)
3. [Category C: Suspicious TLDs](#category-c-suspicious-tlds-)
4. [Category D: Suspicious Patterns](#category-d-suspicious-patterns-)
5. [Category E: Long & Complex URLs](#category-e-long--complex-urls-)
6. [Category F: Special Characters & Unicode](#category-f-special-characters--unicode-)
7. [Category G: IP-Based URLs](#category-g-ip-based-urls-)
8. [Category H: Throttling/Rate Limit Tests](#category-h-throttlinglrate-limit-tests)

---

## CATEGORY A: Legitimate URLs ✅

These are known safe domains for baseline testing.

### Test 1: Google
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.google.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: Microsoft
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.microsoft.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: Amazon
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.amazon.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: GitHub
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.github.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 5: Stack Overflow
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.stackoverflow.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 6: Wikipedia
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.wikipedia.org"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 7: YouTube
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.youtube.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY B: Suspicious Misspellings ⚠️

Typosquatting attacks - misspelled famous domains.

### Test 1: Misspelled Google (gogle)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.gogle.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: Misspelled Microsoft (micros0ft)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.micros0ft.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: Misspelled Amazon (amaz0n)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.amaz0n.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: Google with Numbers (g00gle-security)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.g00gle-security.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 5: Facebook Verify (fake)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.facebook-verify.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 6: PayPal Misspelled (paypa1)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.paypa1.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 7: Google Login (suspicious)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.go0gle-login.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY C: Suspicious TLDs ⚠️

Domains using suspicious top-level domains known for phishing.

### Test 1: Google Verify (.tk)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://google-verify.tk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: Microsoft Login (.ml)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://microsoft-login.ml"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: Amazon Account (.ga)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://amazon-account.ga"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: PayPal Secure (.cf)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://paypal-secure.cf"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 5: Bank Login (.cc)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://bank-login.cc"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 6: Apple ID Verify (.xyz)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://apple-id-verify.xyz"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY D: Suspicious Patterns ⚠️

URLs with suspicious patterns and tricks used in phishing attacks.

### Test 1: Domain Chaining (google.com.verify.tk)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://google.com.verify.tk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: Bit.ly Shortener (securelogin)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://bit.ly/securelogin123"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: TinyURL Shortener (amazonlogin)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://tinyurl.com/amazonlogin"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: Double @ Symbol (google.com@microsoft.com)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://google.com@microsoft.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 5: Encoded @ Symbol
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://google.com%40microsoft.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY E: Long & Complex URLs ⚠️

Complex URLs with parameters that might hide phishing intent.

### Test 1: Google Search with Redirect
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.google.com/search?q=login&redirect=https://fake-google.tk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: Amazon with OpenID
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://amazon.com/ap/signin?openid.ns=http://specs.openid.net/auth/2.0&returnto=https://malicious.tk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: Gmail with Long Parameters
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?email=admin@bank.tk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: Google Accounts with Phishing Redirect
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://accounts.google.com/ServiceLoginAuth?service=mail&continue=https://phishing-site.tk"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY F: Special Characters & Unicode ⚠️

URLs with encoded characters and Unicode tricks used to bypass detection.

### Test 1: Cyrillic Characters (gооgle)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.gооgle.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: URL Encoded (g%6fgle)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.g%6fgle.com"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: Path Traversal Encoded
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.google.com%2f..%2f..%2fadmin"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: Session ID Injection
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "https://www.google.com%3bjsessionid=1234567890"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY G: IP-Based URLs ⚠️

URLs using IP addresses instead of domain names (common in phishing).

### Test 1: Local IP (172.16.0.1)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "http://172.16.0.1/admin"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 2: Local IP with Port (192.168.0.1:8080)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "http://192.168.0.1:8080/login"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 3: Banking on Local Network
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "http://10.0.0.1/banking"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

### Test 4: Localhost (127.0.0.1)
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = @{url = "http://127.0.0.1:5000/predict"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
```

---

## CATEGORY H: Throttling/Rate Limit Tests

Tests for API performance and rate limiting behavior.

### Test 1: 5 Rapid Requests (No Delay)
```powershell
for ($i = 1; $i -le 5; $i++) {
    Write-Host "Request $i"
    $headers = @{"Content-Type" = "application/json"}
    $body = @{url = "https://www.google.com"} | ConvertTo-Json
    Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
}
```

### Test 2: 10 Requests with 100ms Delay
```powershell
for ($i = 1; $i -le 10; $i++) {
    Write-Host "Request $i - $(Get-Date)"
    $headers = @{"Content-Type" = "application/json"}
    $body = @{url = "https://www.google.com"} | ConvertTo-Json
    Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
    Start-Sleep -Milliseconds 100
}
```

### Test 3: 20 Requests with 500ms Delay
```powershell
for ($i = 1; $i -le 20; $i++) {
    Write-Host "Request $i - $(Get-Date)"
    $headers = @{"Content-Type" = "application/json"}
    $body = @{url = "https://www.amazon.com"} | ConvertTo-Json
    Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
    Start-Sleep -Milliseconds 500
}
```

### Test 4: Concurrent Requests (All at Once)
```powershell
$urls = @("https://www.google.com", "https://www.microsoft.com", "https://www.amazon.com", "https://www.github.com", "https://www.youtube.com")

$jobs = @()
foreach ($url in $urls) {
    $job = Start-Job -ScriptBlock {
        param($url)
        $headers = @{"Content-Type" = "application/json"}
        $body = @{url = $url} | ConvertTo-Json
        Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -Headers $headers -Body $body
    } -ArgumentList $url
    $jobs += $job
}

Wait-Job $jobs
Get-Job | Receive-Job
Remove-Job $jobs
```

---

## Summary Table

| Category | Tests | Purpose | Expected Result |
|----------|-------|---------|-----------------|
| **A** | 7 | Legitimate sites (baseline) | Should flag as SAFE |
| **B** | 7 | Misspelled domains (typosquatting) | Should flag as PHISHING |
| **C** | 6 | Suspicious TLDs | Should flag as PHISHING |
| **D** | 5 | Suspicious patterns | Should flag as PHISHING |
| **E** | 4 | Long/complex URLs | Should flag as PHISHING |
| **F** | 4 | Special characters/Unicode | Should flag as PHISHING |
| **G** | 4 | IP-based URLs | Should flag as SUSPICIOUS |
| **H** | 4 | Rate limiting/throttling | Performance metrics |

**Total: 41 Ready-to-Paste Commands** 🚀

---

## How to Use This File

1. **Copy any command** from the appropriate category
2. **Paste it directly** into your PowerShell terminal
3. **Press Enter** to execute the command
4. **Check the response** for the prediction results

### Expected Response Format
```json
{
  "clean_url": "https://www.example.com",
  "domain": "example.com",
  "feature_count": 24,
  "features": [14, 10, 0, 3, 0, 12, 0.857, ...],
  "prediction": 0
}
```

- `prediction: 0` = **LEGITIMATE** ✅
- `prediction: 1` = **PHISHING** ⚠️

---

## Notes

- Keep your Flask server running in the background
- Use a separate PowerShell window for testing
- Server must be accessible at `http://127.0.0.1:5000/`
- Each test is independent and can be run separately

---