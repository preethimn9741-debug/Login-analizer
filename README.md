
# Login Analyzer

## 📌 Project Description
**Login Analyzer** is a Python-based tool that analyzes login log files to detect failed login attempts and potential suspicious activity.
It processes log data, summarizes user login behavior, and generates structured CSV reports for easy review.

This project is created as a **learning and practice project** to understand log analysis, data processing, and automation using Python.

---

## 🎯 Purpose of the Project
This project is:
- ✅ A learning exercise
- ✅ A log analysis utility
- ❌ Not a production-grade security system

It helps in understanding how login logs can be analyzed to identify issues and patterns.

---

## ✨ Features
- Reads login log files (CSV format)
- Counts total login attempts per user
- Identifies failed login attempts
- Flags users with suspicious repeated failures
- Generates summary reports in CSV format
- Handles missing or invalid data safely

---

## 🛠 Tech Stack
- **Language:** Python  
- **Library:** pandas  
- **Execution:** Command Line (CLI)  
- **Input Format:** CSV  
- **Output Format:** CSV  

---

## 🏗 Architecture Overview
- Log files are read using pandas
- Data is cleaned and validated
- Login attempts are grouped by user
- Failed attempts are analyzed
- Results are written to a CSV report

---

## 📂 Project Structure
Login-analyzer/
│
├── login_analyzer.py # Main analysis script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── data/
│ └── sample_logs.csv # Sample input log file
│
└── reports/
└── output.csv # Generated report

---

## ⚙️ Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/preethimn9741-debug/Login-analizer.git
cd Login-analizer

