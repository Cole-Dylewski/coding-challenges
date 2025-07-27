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

> **More challenges coming soon!**

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

## 🎯 What This Repository Demonstrates

* **Code clarity & maintainability** → following PEP8 & clean code standards
* **Problem-solving methodology** → reasoning
