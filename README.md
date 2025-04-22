# README.md

## Titanic Q&A Streamlit App

A simple Streamlit app that lets you ask natural‑language questions of the Titanic dataset.  
Under the hood it uses OpenAI to generate a small pandas query, runs it, and displays the answer.

---

### 1. Clone or download this repo

Make sure you have these files in your project:

- `app.py` - The main Streamlit application  
- `requirements.txt` - Required Python packages  
- `data/titanic.csv` - The Titanic dataset  
- `.env` - Your environment variables (see below)  

---

### 2. Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1


# macOS / Linux
python3 -m venv venv
source venv/bin/activate


pip install --upgrade pip
pip install -r requirements.txt

streamlit run app.py
```

