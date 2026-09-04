# 🌱 Contributing to AkashaCorruptGuard

Greetings, fellow researcher or scholar of the Akademiya! Whether you are a brilliant student, an ambitious researcher, or a Grand Sage, your contributions to safeguarding the Akasha Terminal are deeply welcomed. 

To maintain data integrity and prevent *Forbidden Knowledge* corruption across our digital archives, please follow these guidelines when contributing to the repository.

---

## 🔍 1. Reporting Anomalies (Issues)
If you discover corrupted metadata, broken bibliographic logic, or a security vulnerability in our Darshan RBAC matrices:
* Open a **GitHub Issue** detailing the anomaly.
* Provide steps to replicate the issue, expected system behavior, and terminal logs.

---

## 🌿 2. The Darshan Development Workflow
To submit code or enhance the QA framework:
1. **Fork** the repository and create your feature branch: `git checkout -b feature/your-feature-name`
2. Set up your local virtual environment and install dependencies.
3. Add your new test cases or utility modules under `tests/` or `utils/`.
4. Ensure all assertions pass locally before submitting.

---

## 🧪 3. Testing Standards (Purification Protocol)
* **Naming Convention:** All test scripts must follow Pytest naming conventions (`test_*.py`).
* **Local Execution Check:** Run the test suite to ensure green results:
  <pre><code>python -m pytest -v</code></pre>
* **Dashboard Generation:** Verify that `report.html` compiles cleanly without unexpected tracebacks.

---

## 📜 4. Matra Commit Message Conventions
We follow standard Conventional Commit patterns to keep our project history clean and organized:
* **`feat:`** Add a new test scenario, fuzzing rule, or utility validator.
* **`fix:`** Fix failing test cases or pipeline scripts.
* **`docs:`** Update documentation, test plans, or execution evidence.
* **`refactor:`** Code improvements without changing testing logic.