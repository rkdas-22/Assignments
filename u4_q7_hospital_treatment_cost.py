# Unit 4 - Q7: Hospital Treatment Cost Analysis System (NumPy and Pandas)

import numpy as np
import pandas as pd


def main():
    patient_ids = ["P101", "P102", "P103", "P104", "P105", "P106"]
    names = ["Asha Patil", "Vikram Rao", "Meera Joshi", "Arjun Kulkarni", "Sneha Deshmukh", "Rahul Mehta"]
    costs = np.array([15000, 32000, 8500, 27000, 12000, 21500])

    print("Treatment costs (NumPy array):", costs)
    print(f"Mean treatment cost   : ₹{np.mean(costs):.2f}")
    print(f"Maximum treatment cost: ₹{np.max(costs)}")
    print(f"Minimum treatment cost: ₹{np.min(costs)}")

    df = pd.DataFrame({"Patient ID": patient_ids, "Name": names, "Treatment Cost": costs})
    print("\nAll patients:")
    print(df.to_string(index=False))

    print("\nPatients whose treatment cost exceeds ₹20,000:")
    print(df[df["Treatment Cost"] > 20000].to_string(index=False))


if __name__ == "__main__":
    main()
