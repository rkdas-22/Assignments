# Unit 3 - Q5: Hospital Patient Record System (CSV)
# Reads patients.csv using a with statement.

import csv


def load_patients(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def display_patients(patients):
    if not patients:
        print("No matching patient found.")
        return
    for p in patients:
        print(f"Patient ID: {p['patient_id']} | Name: {p['name']} | "
              f"Treatment Cost: ₹{p['treatment_cost']}")


def main():
    patients = load_patients("patients.csv")

    print("\n--- All Patient Details ---")
    display_patients(patients)

    pid = input("\nEnter Patient ID to search: ").strip()
    print("\n--- Search Result ---")
    display_patients([p for p in patients if p["patient_id"].upper() == pid.upper()])


if __name__ == "__main__":
    main()
