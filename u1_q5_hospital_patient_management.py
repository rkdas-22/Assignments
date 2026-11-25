# Unit 1 - Q5: Hospital Patient Management System (OOP)
# Assumption: "Special" if treatment cost >= 20000, otherwise "General"

class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def get_category(self):
        return "Special" if self.treatment_cost >= 20000 else "General"

    def __str__(self):
        return (f"Patient ID: {self.patient_id} | Name: {self.name} | "
                f"Treatment Cost: ₹{self.treatment_cost:.2f} | Category: {self.get_category()}")


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_records(self):
        if not self.patients:
            print("No patient records.")
            return
        print("\n--- Patient Records ---")
        for p in self.patients:
            print(p)


def main():
    hospital = Hospital()
    n = int(input("Enter number of patients: "))
    for i in range(n):
        print(f"\nPatient {i + 1}:")
        pid = input("Patient ID: ")
        name = input("Name: ")
        cost = float(input("Treatment Cost: "))
        hospital.add_patient(Patient(pid, name, cost))
    hospital.display_records()


if __name__ == "__main__":
    main()
