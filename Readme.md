# Smart Phishing Detection & URL Risk Analyzer

A web-based system that analyzes URLs and evaluates potential phishing risks to help users identify suspicious or malicious links before accessing them.

---

## Repository Setup & Contribution Guidelines

TThis guide explains how to **pull the project, create your own branch, and push your work safely** without affecting the main code.

---

# 1. Create a GitHub Personal Access Token

GitHub no longer allows password authentication for Git.

## Step 1
Open:

```

[https://github.com/settings/tokens](https://github.com/settings/tokens)

```

## Step 2
Click:

```

Generate new token → Fine-grained token

```

## Step 3
Settings:

```

Repository access → Select repository
Smart-Phishing-Detection-URL-Risk-Analyzer

```

Permissions:

```

Contents → Read and Write
Metadata → Read

```

## Step 4
Generate token and **copy it immediately**.

Example token:

```

github_pat_xxxxxxxxxxxxxxxxx

````

---

# 2. Clone the Repository

Open terminal and run:

```bash
git clone https://github.com/samarjeets10/Smart-Phishing-Detection-URL-Risk-Analyzer.git
````

Enter:

```
Username: <your github username>
Password: <paste token here>
```

Go inside the project folder:

```bash
cd Smart-Phishing-Detection-URL-Risk-Analyzer
```

---

# 3. Always Pull Latest Code

Before starting work run:

```bash
git checkout main
git pull origin main
```

This keeps your project updated.

---

# 4. Create Your Own Branch

Never work directly on `main`.

Create your personal branch:

```bash
git checkout -b yourname-feature
```

Example:

```bash
git checkout -b rahul-feature
```

Check branch:

```bash
git branch
```

---

# 5. Work on the Code

Edit files or add new scripts.

Check modified files:

```bash
git status
```

---

# 6. Add Files to Git

```bash
git add .
```

Or specific file:

```bash
git add filename.py
```

---

# 7. Commit Your Changes

```bash
git commit -m "Added phishing detection feature"
```

---

# 8. Push Your Branch

Push your branch to GitHub:

```bash
git push origin yourname-feature
```

Example:

```bash
git push origin rahul-feature
```

---

# 9. Create a Pull Request

Go to the repository on GitHub.

You will see:

```
Compare & Pull Request
```

Create a pull request:

```
base: main
compare: your branch
```

Admin will review and merge your code.

---


# Useful Commands

Check status:

```bash
git status
```

View branches:

```bash
git branch
```

Switch branch:

```bash
git checkout branch-name
```

Update project:

```bash
git pull origin main
```

---

# Basic Workflow

```
git clone repo
cd project
git pull origin main
git checkout -b your-branch
(edit code)
git add .
git commit -m "message"
git push origin your-branch
create pull request
```

Following this workflow ensures **safe collaboration without breaking the main project.**


## Team Collaboration Rules

- Always work on a **separate branch**.
- Do **not modify the main branch directly**.
- Inform the team before merging major changes.
- Try to avoid editing the same files simultaneously.

---
