import pandas as pd

# 1. Load inventory dataset
try:
    df = pd.read_csv("inventory.csv")
    print("--- 📦 Original Inventory Data ---")
    print(df)
    print("\n" + "=" * 45 + "\n")

    # 2. Calculate Power Dissipation (P = V * I) in mW
    df["Power_mW"] = df["Voltage_V"] * df["Current_mA"]

    print("--- ⚡ Inventory Data with Calculated Power (mW) ---")
    print(df)
    print("\n" + "=" * 45 + "\n")

    # 3. Filter Low-Stock Components (Stock_Qty < 15)
    low_stock_threshold = 15
    low_stock_df = df[df["Stock_Qty"] < low_stock_threshold]

    print(
        f"--- ⚠️ Low-Stock Alert (Less than {low_stock_threshold} units) ---"
    )
    if not low_stock_df.empty:
        print(low_stock_df[["Component", "Category", "Stock_Qty"]])
    else:
        print("All components have sufficient stock!")

    # 4. Export Low-Stock report to a new CSV file
    output_filename = "low_stock_alert.csv"
    low_stock_df.to_csv(output_filename, index=False)
    print(f"\n✅ Low-stock report exported successfully to '{output_filename}'")

except FileNotFoundError:
    print(
        "❌ Error: 'inventory.csv' not found. Make sure the file exists in your current folder!"
    )