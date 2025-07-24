# 🤖 Claims Automation System

This is a smart insurance claims processing system that automates simple claims and routes complex ones to human reviewers. It uses OCR, simple rule-based classification, and complexity scoring to streamline document workflows.

---

## 🚀 Features

- 📄 Upload and process claim documents (PDF, images, or text)
- 🔍 Extracts important information: Name, Policy ID, Amount, etc.
- 🧠 Scores complexity and flags incomplete/ambiguous claims
- 🔀 Automatically routes claims: auto-process or human review
- 🧪 Test interactively with a Streamlit UI or via Flask API

---

## 🛠 Technologies Used

- Python
- Streamlit (for dashboard)
- Flask (for REST API)
- Tesseract OCR
- PyMuPDF (for PDF reading)
- Regex/NLP for info extraction

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/claims-automation-system.git
cd claims-automation-system
pip install -r requirements.txt
