import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set modern Seaborn theme
sns.set_theme(style="darkgrid")

try:
    # 1. Load inventory dataset
    df = pd.read_csv("inventory.csv")

    # 2. Calculate Power in mW
    df["Power_mW"] = df["Voltage_V"] * df["Current_mA"]

    # Create figure with 2 subplots side-by-side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Subplot 1: Power Consumption ---
    sns.barplot(
        data=df,
        x="Component",
        y="Power_mW",
        ax=ax1,
        palette="viridis",
        hue="Component",
        legend=False,
    )
    ax1.set_title("⚡ Component Power Dissipation (mW)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Component")
    ax1.set_ylabel("Power (mW)")
    ax1.tick_params(axis="x", rotation=30)

    # --- Subplot 2: Stock Quantity ---
    # Highlight items with stock < 15 in red, others in blue
    colors = ["#e74c3c" if qty < 15 else "#3498db" for qty in df["Stock_Qty"]]

    ax2.bar(df["Component"], df["Stock_Qty"], color=colors)
    ax2.axhline(
        y=15,
        color="r",
        linestyle="--",
        label="Low Stock Threshold (15)",
    )
    ax2.set_title("📦 Inventory Stock Levels", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Component")
    ax2.set_ylabel("Quantity in Stock")
    ax2.tick_params(axis="x", rotation=30)
    ax2.legend()

    plt.tight_layout()

    # 3. Save plot to image file
    output_image = "inventory_analysis.png"
    plt.savefig(output_image, dpi=300)
    print(f"✅ Visualization saved successfully as '{output_image}'!")

    # Display plot window
    plt.show()

except FileNotFoundError:
    print("❌ Error: 'inventory.csv' not found in current folder!")