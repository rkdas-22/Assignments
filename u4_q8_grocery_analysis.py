# Unit 4 - Q8: Grocery Store Analysis System (NumPy and Pandas)

import numpy as np
import pandas as pd


def main():
    items = ["Rice", "Wheat Flour", "Sugar", "Milk", "Eggs", "Salt", "Tea", "Oil"]
    prices = np.array([60, 45, 42, 56, 7, 20, 150, 180])
    quantities = np.array([25, 8, 30, 6, 40, 12, 9, 20])

    print("Product prices (NumPy array):", prices)
    print(f"Mean price   : ₹{np.mean(prices):.2f}")
    print(f"Median price : ₹{np.median(prices):.2f}")
    print(f"Maximum price: ₹{np.max(prices)}")
    print(f"Minimum price: ₹{np.min(prices)}")

    df = pd.DataFrame({"Item": items, "Price": prices, "Quantity": quantities})
    print("\nAll grocery items:")
    print(df.to_string(index=False))

    print("\nItems having quantity less than 10:")
    print(df[df["Quantity"] < 10].to_string(index=False))


if __name__ == "__main__":
    main()
