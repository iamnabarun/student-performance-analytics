# Project Documentation: Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**  
Student name: [Enter your name]  
Course: Python with AI — EWB Courses

## 2. Objective
The objective is to build a Python program that reads student records and analyzes marks and attendance. It summarizes individual and class performance, assigns grades, identifies pass/fail results, compares subjects and highlights top performers.

## 3. Technologies Used
- Python
- NumPy for numerical calculations
- Pandas for CSV loading, DataFrame processing, grouping and output

## 4. Dataset Description
The included `students.csv` contains 20 fictional student records. Columns are Student_ID, Name, Department, Python, Mathematics, English and Attendance. Marks and attendance are percentages out of 100.

## 5. Implementation
1. Pandas reads the CSV file into a DataFrame.
2. The program checks that required columns exist and validates marks and attendance ranges.
3. NumPy calculates total marks and average marks for each student.
4. A reusable function assigns a grade based on the student's average.
5. A loop evaluates each student's grade and pass/fail status. Passing requires at least 35 marks in every subject.
6. Pandas and Python functions calculate class statistics, subject-wise statistics, grade distribution, department averages and the top five students.
7. The processed DataFrame is printed in a readable format and saved to `student_analysis_results.csv`.

## 6. Key Features
- Dataset loading and validation
- Total and average marks per student
- Grade and pass/fail assignment
- Highest, lowest and overall average performance
- Subject-wise average, highest and lowest marks
- Top five performers
- Grade distribution and department-wise averages
- Export of processed results

## 7. Output / Screenshots
Run `python main.py` and capture a screenshot of the terminal showing the class summary, individual results, subject-wise analysis and top performers. The program also creates `student_analysis_results.csv`.

## 8. Final Outcome
The program turns the raw student CSV into a readable performance report. It identifies individual results and summarizes patterns across subjects and departments. The output can be reproduced by running the script with the included dataset.

## 9. Challenges & Learning
The project practices reading structured data, validating values, using DataFrames, performing numerical calculations with NumPy, writing reusable functions, applying loops and conditions, and presenting analysis in a clear format. Input validation helps catch missing columns and out-of-range marks before analysis.

## 10. GitHub Repository
Repository URL: [Paste your GitHub repository URL here after uploading the project.]

## Rules used
**Grades:** A >= 90; B >= 80; C >= 70; D >= 60; F < 60.  
**Pass condition:** a student passes only if each subject mark is at least 35.
