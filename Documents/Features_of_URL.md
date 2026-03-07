#  Main URL Features That Indicate Phishing

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

## 4. Sum other Features
| # | Feature Name | Category | Description | Example |
|---|--------------|----------|-------------|---------|
| 1 | URL Length | Lexical | Total length of the URL string | https://secure-paypal-login.com/verify |
| 2 | Domain Length | Lexical | Length of the domain name | paypal-secure-login.com |
| 3 | Path Length | Structural | Length of path after domain | /account/verify/login |
| 4 | Number of Dots | Lexical | Count of '.' in URL | login.paypal.secure.verify.ru |
| 5 | Number of Hyphens | Lexical | '-' characters in domain | paypal-login-security.com |
| 6 | Number of Subdomains | Structural | Subdomains before main domain | login.secure.verify.example.com |
| 7 | Number of Digits | Lexical | Count of numeric characters | login123-secure.com |
| 8 | Presence of @ Symbol | Lexical | '@' can hide real domain | http://paypal.com@malicious.ru |
| 9 | Presence of IP Address | Host | Domain replaced with IP | http://192.168.1.1/login |
|10 | HTTPS Usage | Security | Whether HTTPS is used | https://bank-login.com |
|11 | Suspicious Keywords | Lexical | Words like login, verify, secure | paypal-verify-account.com |
|12 | URL Entropy | Statistical | Randomness of characters | xj3kq-secure-login.top |
|13 | Token Count | Structural | Number of tokens in URL | /account/verify/update |
|14 | Longest Token Length | Lexical | Length of longest word in URL | secureloginverification |
|15 | Shortest Token Length | Lexical | Length of smallest token | a |
|16 | Number of Parameters | Structural | Query parameters count | ?id=123&session=abc |
|17 | Presence of Redirect | Structural | URL contains redirect patterns | redirect=login |
|18 | Presence of Encoding | Lexical | Encoded characters | %20 %3A %2F |
|19 | Special Character Count | Lexical | Count of symbols | ! $ % & |
|20 | Digit Ratio | Statistical | Ratio of digits to letters | login123456.com |
|21 | Uppercase Ratio | Statistical | Ratio of uppercase letters | LOGINverify.com |
|22 | Path Depth | Structural | Number of '/' segments | /a/b/c/login |
|23 | TLD Type | Domain | Top-level domain used | .xyz .ru .top |
|24 | Domain Age | Host | Age of domain registration | newly registered domain |
|25 | Domain Expiration | Host | Time until domain expiry | 1 month left |
|26 | DNS Record Presence | Host | Whether DNS exists | valid DNS entry |
|27 | WHOIS Availability | Host | Domain WHOIS information | hidden WHOIS |
|28 | Registrar Reputation | Host | Known suspicious registrar | cheap unknown registrar |
|29 | URL Shortener | Lexical | Shortened URLs used | bit.ly/xyz123 |
|30 | Repeated Characters | Lexical | Repeated letters or numbers | secureeee-login.com |
|31 | Unusual Port | Structural | Non-standard port numbers | :8080 :4444 |
|32 | File Extension | Structural | Suspicious file extension | login.php |
|33 | Domain Entropy | Statistical | Random domain patterns | xkqz-login-secure.top |
|34 | Keyword Density | Lexical | Frequency of phishing keywords | verify-login-account |
|35 | Brand Name Presence | Lexical | Brand impersonation | paypal-login-security |
|36 | URL Complexity Score | Statistical | Combined complexity measure | long complex phishing URL |




##### © 2026 Kunal Harshad Patil