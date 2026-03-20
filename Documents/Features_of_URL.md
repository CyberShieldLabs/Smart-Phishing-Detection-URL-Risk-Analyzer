# Feature Extraction for URL-Based Phishing Detection Model

---

## Overview

This model uses **URL-based features only**, making it lightweight, fast, and suitable for real-time phishing detection.

The selected features focus on:
- URL structure
- Character patterns
- Suspicious symbols
- Security indicators

---

## Feature Categories

---

## 1. Length-Based Features

| Feature | Description |
|--------|------------|
| URLLength | Total length of the full URL |
| DomainLength | Length of the domain name |
| TLDLength | Length of the top-level domain |

---

## 2. Domain-Based Features

| Feature | Description |
|--------|------------|
| IsDomainIP | 1 if domain is IP address, else 0 |
| NoOfSubDomain | Number of subdomains |

---

## 3. Character & Pattern Features

| Feature | Description |
|--------|------------|
| CharContinuationRate | Measures repeated/continuous characters |
| URLCharProb | Probability score of character randomness |

---

## 4. Obfuscation Features

| Feature | Description |
|--------|------------|
| HasObfuscation | 1 if obfuscation exists |
| NoOfObfuscatedChar | Count of obfuscated characters |
| ObfuscationRatio | Ratio of obfuscated characters |

---

## 5. Letter & Digit Distribution

| Feature | Description |
|--------|------------|
| NoOfLettersInURL | Count of letters |
| LetterRatioInURL | Ratio of letters |
| NoOfDegitsInURL | Count of digits |
| DegitRatioInURL | Ratio of digits |

---

## 6. Special Character Features

| Feature | Description |
|--------|------------|
| NoOfEqualsInURL | Count of '=' |
| NoOfQMarkInURL | Count of '?' |
| NoOfAmpersandInURL | Count of '&' |
| NoOfOtherSpecialCharsInURL | Count of other symbols |
| SpacialCharRatioInURL | Ratio of special characters |

---

## 7. Security Feature

| Feature | Description |
|--------|------------|
| IsHTTPS | 1 if HTTPS is used, else 0 | 

*Training-Serving Skew*

---

## 8. Keyword-Based Indicators

| Feature | Description |
|--------|------------|
| Bank | 1 if banking-related keyword present |
| Pay | 1 if payment keyword present |
| Crypto | 1 if crypto-related keyword present |

---

## Output Label

| Label | Meaning |
|------|--------|
| 0 | Legitimate URL |
| 1 | Phishing URL |

---

## Example Input & Output Format

Each row represents one URL converted into numerical features.

```text
URLLength  DomainLength  IsDomainIP  CharContinuationRate  URLCharProb  TLDLength  NoOfSubDomain  HasObfuscation  NoOfObfuscatedChar  ObfuscationRatio  NoOfLettersInURL  LetterRatioInURL  NoOfDegitsInURL  DegitRatioInURL  NoOfEqualsInURL  NoOfQMarkInURL  NoOfAmpersandInURL  NoOfOtherSpecialCharsInURL  SpacialCharRatioInURL  IsHTTPS  Bank  Pay  Crypto  label

19  13  0  1  0.082002449  3  1  0  0  0  7  0.368  0  0  0  0  0  1  0.053  0  0  0  0  0
26  19  0  1  0.060233585  2  1  0  0  0  13  0.5  0  0  0  0  0  1  0.038  1  0  0  0  1
````

---


## Summary

* Total Features Used: **23**
* Output: Binary classification (0 or 1)
* Format: Structured numerical dataset

---

## Conclusion

This feature extraction approach ensures:

* Fast processing
* Real-time usability
* Clear and structured input for ML models

It forms the backbone of the phishing detection system.

---
##### © 2026 Kunal Harshad Patil  
For more learning resources and updates, connect with me:  
[GitHub](https://github.com/kunal8670) • [LinkedIn](https://www.linkedin.com/in/kunal-patil-8733b528a/)

---





