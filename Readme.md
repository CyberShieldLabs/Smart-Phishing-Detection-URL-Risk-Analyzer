# Smart Phishing Detection & URL Risk Analyzer

A web-based system that analyzes URLs and evaluates potential phishing risks to help users identify suspicious or malicious links before accessing them.

---

## Repository Setup & Contribution Guidelines

To maintain proper collaboration and avoid conflicts, all team members must follow the guidelines below.

---

## 1. Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

## 2. Main Branch Policy

- The **main branch** is the stable and primary branch of the project.
- **Do NOT push any changes directly to the `main` branch.**

---

## 3. Create Your Own Branch

Before starting any work, create a new branch.

```bash
git checkout -b your-branch-name
```

Example:

```bash
git checkout -b feature-url-analyzer
```

---

## 4. Push Changes to Your Branch

After completing your work, commit and push the changes to your branch.

```bash
git add .
git commit -m "Describe your changes"
git push origin your-branch-name
```

---

## 5. Inform Before Merging

Before merging your branch:

- Inform the team members.
- Ensure the code is tested.
- Confirm that it does not break existing features.

---

## 6. Do Not Push Directly to Main

Avoid running the following command:

```bash
git push origin main
```

All updates must go through **separate branches**.

---

## 7. Avoid Merge Conflicts

To reduce conflicts:

- Always pull the latest changes before starting work.

```bash
git pull origin main
```

- Work on different modules when possible.
- Commit changes frequently with clear messages.

---

## 8. Commit Message Guidelines

Use meaningful commit messages.

Good examples:

```
Add URL pattern detection logic
Implement risk scoring module
Fix frontend input validation
```

Avoid messages like:

```
update
changes
fix
```

---

## Team Collaboration Rules

- Always work on a **separate branch**.
- Do **not modify the main branch directly**.
- Inform the team before merging major changes.
- Try to avoid editing the same files simultaneously.

---
