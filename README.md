# CyberVerify
---
# CyberVerify - Suspicious Message Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

## About the Project

**CyberVerify** is a Python-based message analysis tool designed to identify **potential indicators of phishing, scams, and social engineering**.

The system receives a message provided by the user, analyzes its content based on a list of suspicious words and indicators, and classifies the potential risk level of the message.

The project was developed with a focus on **programming practice, modularization, and the application of basic cybersecurity concepts**.

> ⚠️ CyberVerify does not determine whether a message is definitely malicious. The result represents an analysis based only on the indicators identified.

## Technologies Used

* **Python** - Programming language used to develop the application.
* **Git** - Version control.
* **GitHub** - Code hosting and project documentation.
* **ANSI Escape Codes** - Used for terminal styling and visual identification of analysis results.

## Project Structure

The application was organized into separate modules, with each file responsible for a specific part of the system:

```text
CyberVerify/
│
├── main.py
├── menu.py
├── analysis.py
└── rules.py
```

### `main.py`

Responsible for starting the application and controlling the main system flow.

### `menu.py`

Responsible for the menu and initial user interaction.

### `analysis.py`

Responsible for receiving and analyzing the message, identifying suspicious indicators, and determining the risk level.

### `rules.py`

Stores the list of suspicious words and indicators used during the analysis.

## How It Works

The analysis process follows these steps:

```text
User message
     ↓
Content analysis
     ↓
Suspicious indicator detection
     ↓
Indicator count
     ↓
Risk classification
     ↓
Analysis result
```

### Risk Classification

| Indicators Found | Risk Level     |
| ---------------- | -------------- |
| 0                | 🟢 Low Risk    |
| 1–2              | 🟡 Medium Risk |
| 3+               | 🔴 High Risk   |

## Analyzed Indicators

The system uses a list of words related to situations commonly found in suspicious messages, including terms related to:

* Accounts and access
* Passwords and credentials
* Payments and transfers
* PIX
* Identity verification
* Prizes and rewards
* Account blocking
* Links and downloads
* Deliveries and orders
* Security and authentication

The indicators include both **English and Portuguese** terms.

## Project Goals

The project was created to apply Python knowledge in a **cybersecurity-related context**, working with concepts such as:

* Functions
* Lists
* Conditional statements
* Loops
* String manipulation
* Modularization
* Module imports
* Rule-based analysis
* Risk classification

## Limitations

CyberVerify currently uses an approach based on predefined words and indicators. Therefore, the tool may produce false positives or fail to identify more sophisticated phishing messages.

The result should be treated as a **risk indicator**, not as definitive confirmation that a message is safe or malicious.

## Future Improvements

Future versions may include:

* More advanced message analysis
* Additional detection rules
* URL analysis
* A more detailed scoring system
* Phishing pattern detection
* Object-Oriented Programming
* Improved system architecture
