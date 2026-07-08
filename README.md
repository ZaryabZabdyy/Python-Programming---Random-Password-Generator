# 🔐 Advanced Random Password Generator

A lightweight, high-performance command-line utility built to generate secure, unpredictable passwords. This project focuses on input validation, secure boundaries, and scalable data structure design.

---

## 🚀 Key Features

* **Strict Input Validation Engine:** Prevents application crashes by filtering non-integer entries and handling exceptions gracefully.
* **Security Boundary Enforcement:** Implements built-in checks to ensure password lengths stay within secure limits (Minimum 8, Maximum 64 characters).
* **Optimized Character Pool:** Dynamically constructs random sequences using a combination of uppercase letters, lowercase letters, and numerical digits.
* **Clean Console Interface:** Provides structured, real-time feedback with intuitive status indicators.

---

## 🏗️ System Architecture & Workflow

The application operates on a clean, decoupled two-phase architecture to separate data validation from the core generation logic:

[User Input] ──> [Phase 1: Validation Engine] ──> [Phase 2: Transformation Engine] ──> [Secure Output]


1. **Phase 1 (Input & Validation):** Captures user input, validates it against system boundaries, and handles exceptions.
2. **Phase 2 (Core Engine):** Utilizes random selection mechanisms to stitch characters together from the secure pool.

---

## 🛠️ Tech Stack & Prerequisites

Before running the project, ensure you have the following installed on your local machine:

* **Environment:** Python 3.8 or higher
* **Database (Optional/Logs):** Local text-based storage / Relational Database (configured for future audit logging)

---

## 💻 How to Setup and Run Locally

Follow these step-by-step instructions to clone and run the project locally:

### 1. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/your-username/Random-Pass-Generator.git](https://github.com/your-username/Random-Pass-Generator.git)
cd Random-Pass-Generator
2. Execute the Script
Run the main Python file directly from your terminal:

Bash
python Random-Pass-Generator.py
3. Local Verification
Enter a number when prompted (e.g., 16).

Copy the generated password safely from the console output.

If you test invalid inputs (like text or small numbers), notice how the system safely rejects them without crashing.

🔮 Upcoming Updates & Roadmap
We are continuously working to elevate this project to production-grade security standards. The following features are scheduled for the next release:

Cryptographically Secure Randomization: Moving from the standard random module to Python’s secrets module to ensure true cryptographic unpredictability.

Special Characters & Symbols: Integrating string.punctuation to support complex passwords containing symbols (e.g., @, #, $).

Diversity Guarantees: Implementing logic to guarantee that every password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.

Database Logging & History: Integrating a secure backend database to safely log generation timestamps and audit data (without saving the actual passwords for security compliance).
