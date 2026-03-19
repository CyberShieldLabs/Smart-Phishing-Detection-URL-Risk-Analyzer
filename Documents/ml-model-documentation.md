
# Smart Phishing Detection & URL Risk Analyzer  
## ML Model Development Documentation  

---

# 1. Pre-Research

Phishing attacks have become one of the most common cyber threats where attackers create fake websites that look legitimate and trick users into sharing sensitive information. Traditional detection methods such as blacklist-based systems fail to detect new or zero-day phishing attacks.

Recent research papers and surveys show that:

- URL-based feature analysis is lightweight and effective.
- Machine Learning models can detect phishing without loading the full webpage.
- Ensemble models like Random Forest and LightGBM give high accuracy.

### Key Research Reference

**Machine Learning-Based Phishing Detection Using URL Features: A Comprehensive Review (2025)**  
- Focus: URL feature-based detection  
- Key Insight: URL-only models can detect phishing efficiently without visiting the site  
- Strong Models: Random Forest, SVM, Gradient Boosting  

---

# 2. Problem Definition

Phishing websites are designed to look like legitimate platforms, making it difficult for users to identify them manually. Even experienced users may fail to detect such attacks.

The problem is to build a system that can automatically classify a given URL as:

- Legitimate (0)
- Phishing (1)

---

# 3. Objective

- Build a machine learning model to detect phishing URLs.
- Achieve high accuracy and high recall (to avoid missing phishing).
- Use structured feature-based detection instead of raw text.
- Prepare the model for integration into a web-based system.

---

# 4. Input and Output

## Input
Structured features extracted from URLs and webpage properties.

## Output
- `0` → Legitimate  
- `1` → Phishing  

Later, output can be extended to:
- Probability (e.g., 85% phishing)
- Risk level (Low / Medium / High)

---

# 5. Dataset Selection

## Selected Dataset

**PhiUSIIL Phishing URL Dataset**  
https://www.kaggle.com/datasets/kaggleprollc/phishing-url-websites-dataset-phiusiil/data  

## Reason for Selection

- Large dataset (~235,000 rows)
- Contains both phishing and legitimate URLs
- Includes rich feature set (~50 features)
- Suitable for ML models like Random Forest and LightGBM

---

# 6. Feature Categories

The dataset contains around 50 features grouped as follows:

## 6.1 URL / Lexical Features
- URLLength  
- URLSimilarityIndex  
- CharContinuationRate  
- URLCharProb  
- NoOfSubDomain  
- NoOfLettersInURL  
- LetterRatioInURL  
- NoOfDegitsInURL  
- DegitRatioInURL  
- NoOfEqualsInURL  
- NoOfQMarkInURL  
- NoOfAmpersandInURL  
- NoOfOtherSpecialCharsInURL  
- SpacialCharRatioInURL  
- IsDomainIP  
- IsHTTPS  

---

## 6.2 Domain Features
- DomainLength  
- TLDLegitimateProb  
- TLDLength  
- DomainTitleMatchScore  
- URLTitleMatchScore  
- Bank  
- Pay  
- Crypto  

---

## 6.3 Obfuscation Features
- HasObfuscation  
- NoOfObfuscatedChar  
- ObfuscationRatio  

---

## 6.4 Web Content Features
- LineOfCode  
- LargestLineLength  
- HasTitle  
- HasFavicon  
- Robots  
- HasDescription  
- HasCopyrightInfo  
- NoOfImage  
- NoOfCSS  
- NoOfJS  

---

## 6.5 Behavioral Features
- IsResponsive  
- NoOfURLRedirect  
- NoOfSelfRedirect  
- NoOfPopup  
- NoOfiFrame  
- HasExternalFormSubmit  
- HasSocialNet  
- HasSubmitButton  
- HasHiddenFields  
- HasPasswordField  
- NoOfSelfRef  
- NoOfEmptyRef  
- NoOfExternalRef  

---

## 6.6 Target Label
- label  

---

# 7. Data Preprocessing

## Step 1: Check Data Distribution

```python
import pandas as pd

df = pd.read_csv("Dataset.csv")
print(df['label'].value_counts())
````

### Reason

To understand dataset balance and detect class imbalance.

---

## Step 2: Remove Unwanted Columns

Removed:

* FILENAME
* URL
* Domain
* Title
* TLD

```python
columns_to_drop = ['FILENAME', 'URL', 'Domain', 'Title', 'TLD']
df = df.drop(columns=columns_to_drop, errors='ignore')
```

### Reason

* These are text/categorical fields
* Not useful for initial ML model
* Reduce noise and improve performance

---

## Step 3: Separate Classes

```python
legit_df = df[df['label'] == 0]
phishing_df = df[df['label'] == 1]
```

### Reason

To enable controlled balancing of dataset.

---

## Step 4: Balance Dataset (50/50)

```python
min_size = min(len(legit_df), len(phishing_df))

legit_sample = legit_df.sample(n=min_size, random_state=42)
phishing_sample = phishing_df.sample(n=min_size, random_state=42)
```

### Reason

* Prevent model bias
* Ensure equal learning from both classes
* Improve recall and fairness

---

## Step 5: Combine + Alternate (0,1,0,1)

```python
rows = []
for i in range(min_size):
    rows.append(legit_sample.iloc[i])
    rows.append(phishing_sample.iloc[i])

balanced_df = pd.DataFrame(rows)
```

### Reason

* Easier debugging and visualization
* Clear dataset structure

---

## Step 6: Shuffle Dataset

```python
balanced_df = balanced_df.sample(frac=1, random_state=42)
```

### Reason

* Remove pattern bias (0,1,0,1)
* Ensure proper ML learning

---

## Step 7: Train / Validation / Test Split

```python
from sklearn.model_selection import train_test_split

train_df, temp_df = train_test_split(
    balanced_df, test_size=0.3, stratify=balanced_df['label'], random_state=42
)

val_df, test_df = train_test_split(
    temp_df, test_size=0.5, stratify=temp_df['label'], random_state=42
)
```

### Final Split

* Train → 70%
* Validation → 15%
* Test → 15%

### Reason

* Train → learning
* Validation → tuning
* Test → final evaluation

---

# 8. Model Selection (Based on Research)

## Selected Models

### 1. Random Forest

* Ensemble model
* High accuracy
* Handles feature interactions well
* Used as baseline model

### 2. LightGBM

* Advanced boosting model
* Faster and more accurate for large datasets
* Used as final optimized model

---

# 9. Summary

* Dataset selected and analyzed
* Features categorized
* Unwanted columns removed
* Dataset balanced (50/50)
* Data shuffled
* Train/Validation/Test split created
* Model selection finalized (RF + LightGBM)

---
...
...
...

##### © 2026 Kunal Harshad Patil  
For more learning resources and updates, connect with me:  
[GitHub](https://github.com/kunal8670) • [LinkedIn](https://www.linkedin.com/in/kunal-patil-8733b528a/)

---

