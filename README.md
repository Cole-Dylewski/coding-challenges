# Coding Challenges

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A curated collection of coding challenges completed as part of technical interviews, hiring assessments, and personal practice.
These challenges span **algorithms, data structures, API development, DevOps automation, and cloud engineering**, showcasing clean, well-documented, and production-ready solutions.

---

## 🚀 About This Repository

This repository serves as:

* A **portfolio of coding solutions** for prospective employers and collaborators
* A demonstration of **problem-solving approaches, best practices, and trade-offs**
* A structured place to explore **Python 3.13**, cloud-related tasks, and backend/API engineering

Each challenge includes:
✅ **Problem statement or prompt** (where allowed)
✅ **Step-by-step reasoning & approach**
✅ **Implementation with clean code & comments**
✅ **Tests & validation** (where applicable)
✅ **Technical notes on complexity & edge cases**

---

## 🛠 Tech Stack

* **Language:** Python 3.13
* **Environment:** Virtual environment (`venv`)
* **Dependencies:** Listed in `requirements.txt`
* **Optional Tools:** `pytest`, `black`, `mypy`, `jupyter`

---

## ✅ Quick Start

Clone this repository and set up the environment:

```bash
# Clone the repository  
git clone https://github.com/Cole-Dylewski/coding-challenges.git  
cd coding-challenges  

# Create and activate a virtual environment  
py -3.13 -m venv .venv  
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux  

# Verify the Python interpreter  
python -c "import sys; print(sys.executable)"  

# Install dependencies  
pip install -r requirements.txt  
```

Run a challenge notebook by navigating to the `Coding Challenges` folder:

```bash
cd "Coding Challenges"
jupyter notebook
```

---

## 📓 Challenges Overview

All notebooks are located in **`Coding Challenges/`**.
The list below is **auto-updated** when new notebooks are added (via the included `list_notebooks.py` script).

| Notebook                             | Description                                                                                                                                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`close_api.ipynb`](#close_apiipynb) | Implements **Post Body Hash generation** for secure API request signing. Covers hashing techniques (SHA256, HMAC), payload integrity validation, and automated signing for authenticated requests. |

> **More challenges coming soon!** Examples will include algorithmic puzzles, backend API tasks, and cloud automation scripts.

---

### 🔗 Table of Contents for Challenges

* [**close\_api.ipynb**](#close_apiipynb)

  * Challenge Prompt
  * Technical Approach
  * Key Takeaways

---

### 📘 Challenge Details

#### `close_api.ipynb`

**Challenge Prompt:**

> *"Generate Post Body Hashes to sign API requests securely. Implement a reusable function to compute hashes for arbitrary request payloads, ensuring compatibility with REST API authentication requirements."*

**Technical Approach:**

* Used `hashlib` for **SHA256 digest computation**
* Created a reusable function to handle `application/json` payloads
* Implemented **HMAC-based signing** with a secret key for API authentication
* Verified payload integrity with test cases simulating request/response flows

**Key Takeaways:**

* Understanding how APIs validate payload integrity
* Handling edge cases (empty payloads, binary data)
* Ensuring compatibility with AWS SigV4–like signing methods

---

## 📂 Repository Structure

```
coding-challenges/
 ├── Coding Challenges/
 │   ├── close_api.ipynb        # Post Body Hashes challenge
 │   └── ... more notebooks ...
 ├── list_notebooks.py          # Script to auto-update challenge list
 ├── requirements.txt
 └── README.md
```

---

## 🔄 Auto-Generating the Challenge List

This repository includes a helper script (`list_notebooks.py`) that scans the `Coding Challenges/` folder and auto-updates this README with new challenges.

Run it after adding a new notebook:

```bash
python list_notebooks.py
```

---

### 🔄 Automated README Updates

This repository also includes a **GitHub Action workflow** that:

* Detects any new `.ipynb` files pushed to the `main` branch
* Runs `list_notebooks.py` to regenerate the Challenges Overview table
* Commits and pushes the updated README back to the repository automatically

Workflow file location: `.github/workflows/update-readme.yml`

---

## ✅ GitHub Actions Workflow YAML

Here’s the workflow that enables automatic README updates. Create this file at **`.github/workflows/update-readme.yml`**:

```yaml
name: Update README Challenge List

on:
  push:
    branches:
      - main

permissions:
  contents: write   # Allow the workflow to push changes back

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          persist-credentials: true  # required for git push

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.13'

      - name: Update README Challenge List
        run: |
          pip install notebook
          python list_notebooks.py

      - name: Commit changes
        run: |
          git config user.name github-actions[bot]
          git config user.email github-actions[bot]@users.noreply.github.com
          git add README.md
          git commit -m "Auto-update README with new notebooks" || echo "No changes"
          git push
```

After adding this file:

* Any push to `main` will trigger the workflow.
* If new notebooks are found, it updates the README automatically.
* The workflow uses the default `GITHUB_TOKEN` with `contents: write` permission.

---

## 🎯 What This Repository Demonstrates

* **Code clarity & maintainability** → following PEP8 & clean code standards
* **Problem-solving methodology** → reasoning before coding
* **Security-conscious API design** → safe hashing & signing techniques
* **Cloud readiness** → examples that align with AWS & backend best practices

---

## 👨‍💻 About Me

I’m a **Senior Data & Cloud Engineer** with expertise in:

* **Python, FastAPI, and backend microservices**
* **AWS infrastructure (ECS, Lambda, Glue, SageMaker)**
* **DevOps automation & CI/CD pipelines**
* **Scaling cloud-native applications**

This repo highlights some of the hands-on challenges I’ve tackled to stay sharp for technical interviews & real-world problem solving.

---

## 🤝 Feedback

If you’re a hiring manager or fellow engineer reviewing this repository, I’d love your feedback!
Feel free to open an issue or connect with me on [LinkedIn](https://www.linkedin.com/in/cole-dylewski).

---

## 📜 License

This repository is intended for educational and demonstration purposes.

---

> *“To improve is to change, to be perfect is to change often” - Winston Churchill*
