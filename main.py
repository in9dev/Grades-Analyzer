import pandas as pd
import os


def get_grades(grade_type):
    """Ask user for multiple grades (summative/formative) with validation."""
    grades = []
    print(f"\nEnter {grade_type} grades (type 'done' when finished):")
    while True:
        g = input(f"{grade_type.capitalize()} grade: ")
        if g.lower() == 'done':
            break
        try:
            g_val = float(g)
            if 0 <= g_val <= 100:
                grades.append(g_val)
            else:
                print("⚠️ Grade must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")
    if not grades:
        return 0
    return sum(grades) / len(grades)  # average


def load_existing_data():
    """Load old data if grades.csv exists."""
    if os.path.exists("grades.csv"):
        print("\n📂 Found existing grades.csv. Loading data...")
        df = pd.read_csv("grades.csv")
        print(df)
        return df
    else:
        print("\n📄 No existing data found. Starting fresh.")
        return pd.DataFrame(columns=["Subject", "Summative (avg)", "Formative (avg)", "Weighted_Avg"])


def main():
    print("🎓 Welcome to Grade Analyzer 2.2 🎓")

    df = load_existing_data()
    data = df.to_dict("records")

    num_subjects = int(input("\nEnter number of new subjects to add: "))

    for _ in range(num_subjects):
        subject = input("\nSubject name: ")

        avg_summative = get_grades("summative")
        avg_formative = get_grades("formative")

        if avg_summative == 0 and avg_formative == 0:
            print("⚠️ Skipping subject (no grades entered).")
            continue

        if avg_summative == 0:
            weighted_avg = avg_formative
        elif avg_formative == 0:
            weighted_avg = avg_summative
        else:
            weighted_avg = (avg_summative * 0.7) + (avg_formative * 0.3)

        data.append({
            "Subject": subject,
            "Summative (avg)": round(avg_summative, 2),
            "Formative (avg)": round(avg_formative, 2),
            "Weighted_Avg": round(weighted_avg, 2)
        })

    df_updated = pd.DataFrame(data)
    df_updated.to_csv("grades.csv", index=False)

    print("\n✅ All grades (old + new) saved to 'grades.csv'\n")
    print(df_updated)

    overall_avg = df_updated["Weighted_Avg"].mean()
    print(f"\n📘 Overall Average: {overall_avg:.2f}%")

if __name__ == "__main__":
    main()
