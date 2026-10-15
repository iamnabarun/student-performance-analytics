"""
Student Performance Analytics System
Technologies: Python, NumPy, Pandas
Run: python main.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "students.csv"

SUBJECTS = ["Python", "Mathematics", "English"]


def load_data(file_path=DATA_FILE):
    """Load the CSV dataset and validate the required columns."""
    df = pd.read_csv(file_path)
    required = {"Student_ID", "Name", "Department", "Python", "Mathematics",
                "English", "Attendance"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    if df.empty:
        raise ValueError("The student dataset is empty.")
    for subject in SUBJECTS:
        df[subject] = pd.to_numeric(df[subject], errors="raise")
        if not df[subject].between(0, 100).all():
            raise ValueError(f"{subject} marks must be between 0 and 100.")
    df["Attendance"] = pd.to_numeric(df["Attendance"], errors="raise")
    if not df["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")
    return df


def assign_grade(average):
    """Grade rule: A >= 90, B >= 80, C >= 70, D >= 60, else F."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def process_students(df):
    """Use NumPy for calculations and a loop for grade/pass processing."""
    result = df.copy()
    marks = result[SUBJECTS].to_numpy(dtype=float)
    result["Total_Marks"] = np.sum(marks, axis=1)
    result["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)

    grades, statuses = [], []
    for average in result["Average_Marks"]:
        grades.append(assign_grade(average))
        # A student passes only when each subject mark is at least 35.
        statuses.append("Pass" if all(result.loc[result.index[len(grades)-1], s] >= 35
                                      for s in SUBJECTS) else "Fail")
    result["Grade"] = grades
    result["Result"] = statuses
    return result


def print_section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def show_summary(df):
    print_section("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print(f"Total students: {len(df)}")
    print(f"Overall class average: {df['Average_Marks'].mean():.2f}/100")
    print(f"Highest student average: {df['Average_Marks'].max():.2f}/100")
    print(f"Lowest student average: {df['Average_Marks'].min():.2f}/100")
    print(f"Passed: {(df['Result'] == 'Pass').sum()}")
    print(f"Failed: {(df['Result'] == 'Fail').sum()}")
    print(f"Average attendance: {df['Attendance'].mean():.2f}%")

    print_section("INDIVIDUAL STUDENT RESULTS")
    columns = ["Student_ID", "Name", "Department", "Total_Marks",
               "Average_Marks", "Grade", "Result", "Attendance"]
    print(df[columns].to_string(index=False))

    print_section("SUBJECT-WISE PERFORMANCE")
    for subject in SUBJECTS:
        print(f"{subject:15} Average: {df[subject].mean():6.2f} | "
              f"Highest: {df[subject].max():6.2f} | Lowest: {df[subject].min():6.2f}")

    print_section("TOP PERFORMERS (TOP 5)")
    top = df.nlargest(5, "Average_Marks")[["Student_ID", "Name", "Average_Marks", "Grade"]]
    print(top.to_string(index=False))

    print_section("GRADE DISTRIBUTION")
    print(df["Grade"].value_counts().sort_index().to_string())

    print_section("DEPARTMENT-WISE AVERAGE")
    print(df.groupby("Department")["Average_Marks"].mean().round(2).to_string())


def main():
    try:
        raw_data = load_data()
        processed = process_students(raw_data)
        show_summary(processed)
        output_file = BASE_DIR / "student_analysis_results.csv"
        processed.to_csv(output_file, index=False)
        print(f"\nDetailed results saved to: {output_file.name}")
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        print(f"Could not process the dataset: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
