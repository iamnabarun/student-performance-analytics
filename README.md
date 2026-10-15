# Student Performance Analytics System

A beginner-friendly Python data-analysis project built for the EWB Courses Python with AI assignment. It uses Python, NumPy and Pandas to analyze student marks and attendance.

## Features
- Loads a CSV dataset with 20 sample student records using Pandas.
- Validates required columns and checks that marks/attendance are between 0 and 100.
- Calculates total and average marks using NumPy.
- Assigns grades (A/B/C/D/F) with a clearly defined rule.
- Identifies pass/fail students. A student passes only if every subject mark is at least 35.
- Reports class averages, highest/lowest averages, attendance, subject-wise statistics, top five students, grade counts and department averages.
- Exports detailed results to `student_analysis_results.csv`.

## Requirements
- Python 3.9 or newer
- pip

## Setup and run
```bash
python -m venv .venv
```
Windows:
```bash
.venv\Scripts\activate
```
macOS/Linux:
```bash
source .venv/bin/activate
```
Install packages and run:
```bash
pip install -r requirements.txt
python main.py
```

## Dataset
`students.csv` includes `Student_ID`, `Name`, `Department`, `Python`, `Mathematics`, `English`, and `Attendance`. All records are fictional sample data.

## Grading rule
- A: average >= 90
- B: average >= 80 and < 90
- C: average >= 70 and < 80
- D: average >= 60 and < 70
- F: average < 60

Pass condition: at least 35 marks in every subject. Grade and pass/fail status are separate measures.

## Project files
- `main.py` — data loading, validation, processing and reporting
- `students.csv` — sample input data
- `requirements.txt` — dependencies
- `Project_Documentation.md` — assignment documentation

## GitHub submission
Create a repository named `student-performance-analytics`, then upload these project files. Verify that `main.py`, `students.csv`, `README.md`, and `Project_Documentation.md` are visible. Copy the repository URL into the EWB Google Form provided by your trainer.
