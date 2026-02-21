# Self Savings for Retirement 💰

A FastAPI-based project to simulate and track retirement savings performance.  
This API helps users calculate returns, manage transactions, and evaluate long-term savings strategies.

---

## 🚀 Features
- **Performance tracking**: Monitor savings growth over time.
- **Returns calculation**: Evaluate investment returns across different periods.
- **Transaction management**: Add, update, and validate savings transactions.
- **Temporal analysis**: Explore savings projections across time horizons.
- **Secure utilities**: Basic security helpers for safe API usage.
- **Test suite**: Pytest coverage for models, routes, and services.

---

## 🛠️ Tech Stack
- **Python 3.14**
- **FastAPI** (for API framework)
- **Pydantic v2** (for data validation)
- **Pytest** (for testing)
- **Docker** (optional deployment)
- **GitHub Actions** (CI/CD ready)

---

## 📦 Installation

Clone the repository:
```Bash
git clone https://github.com/sarabhanuprasadgoud-collab/self_saving_for_retirement.git
cd self_saving_for_retirement
```
---

Create a virtual environment:
```Bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

Install dependencies:
```Bash
pip install -r requirements.txt
```

---

▶️ Running the API
Start the FastAPI server:
```Bash
uvicorn app.main:app --reload
```

---

Visit the interactive docs:

- Swagger UI: http://127.0.0.1:8000/docs (127.0.0.1 in Bing)
- ReDoc: http://127.0.0.1:8000/redoc (127.0.0.1 in Bing)

----

🧪 Testing
Run the test suite:
```Bash
pytest
```

---

📂 Project Structure

app/
 ├── main.py              # Entry point
 ├── models/              # Data models
 ├── routes/              # API endpoints
 ├── services/            # Business logic
 ├── utils/               # Utilities (e.g., security)
 └── tests/               # Pytest test cases
requirements.txt
.gitignore

---

🌟 Future Enhancements
• Add authentication & user accounts
• Integrate database (PostgreSQL / MongoDB)
• Deploy with Docker & CI/CD pipeline
• Performance metrics dashboard

---

👩‍💻 Author
Sara Bhanu Prasad Goud
Software Engineer | FastAPI & Pydantic Enthusiast | Hackathon-ready API builder
