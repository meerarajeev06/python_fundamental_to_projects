import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="ECE Component & Power Workbench", page_icon="⚡", layout="wide"
)

sns.set_theme(style="darkgrid")

st.title("⚡ ECE Component & Power Analytics Workbench")
st.write(
    "Integrated Capstone Application: Manage inventory, analyze circuit power dissipation, and monitor stock threshold alerts."
)

st.divider()

# --- Sidebar: Data & Settings ---
st.sidebar.header("⚙️ Configuration")

# Option to load sample or custom CSV
uploaded_file = st.sidebar.file_uploader("Upload Inventory CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv("inventory.csv")
    except FileNotFoundError:
        # Fallback dummy data if no CSV exists
        df = pd.DataFrame(
            {
                "Component": [
                    "Resistor 10k",
                    "LED Red",
                    "Arduino Uno",
                    "ESP32",
                    "LM7805",
                ],
                "Category": [
                    "Passive",
                    "Opto",
                    "Microcontroller",
                    "Microcontroller",
                    "Power",
                ],
                "Voltage_V": [5.0, 2.0, 5.0, 3.3, 12.0],
                "Current_mA": [0.5, 20.0, 50.0, 160.0, 5.0],
                "Stock_Qty": [150, 12, 5, 3, 8],
            }
        )

# Threshold slider in sidebar
low_stock_limit = st.sidebar.slider(
    "Low Stock Threshold", min_value=1, max_value=50, value=15
)

# Calculations
df["Power_mW"] = df["Voltage_V"] * df["Current_mA"]

# --- Main Dashboard Tabs ---
tab1, tab2, tab3 = st.tabs(
    ["📊 Data Overview", "📈 Visual Analytics", "⚠️ Low-Stock Alerts"]
)

# TAB 1: Data Table & Summary Metrics
with tab1:
    st.subheader("Inventory Master Table")

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Components", len(df))
    m2.metric("Total Power (mW)", f"{df['Power_mW'].sum():.2f} mW")
    m3.metric(
        "Low Stock Items", len(df[df["Stock_Qty"] < low_stock_limit])
    )

    st.dataframe(df, use_container_width=True)

# TAB 2: Visualizations
with tab2:
    st.subheader("Component Power & Stock Distribution")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=df,
            x="Component",
            y="Power_mW",
            ax=ax1,
            palette="viridis",
            hue="Component",
            legend=False,
        )
        ax1.set_title("Power Dissipation (mW)", fontweight="bold")
        ax1.tick_params(axis="x", rotation=45)
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        colors = [
            "#e74c3c" if qty < low_stock_limit else "#3498db"
            for qty in df["Stock_Qty"]
        ]
        ax2.bar(df["Component"], df["Stock_Qty"], color=colors)
        ax2.axhline(
            y=low_stock_limit,
            color="r",
            linestyle="--",
            label=f"Threshold ({low_stock_limit})",
        )
        ax2.set_title("Current Stock Levels", fontweight="bold")
        ax2.tick_params(axis="x", rotation=45)
        ax2.legend()
        st.pyplot(fig2)

# TAB 3: Filtered Alerts & Export
with tab3:
    st.subheader(f"Items Below Threshold ({low_stock_limit} units)")

    alert_df = df[df["Stock_Qty"] < low_stock_limit]

    if not alert_df.empty:
        st.warning(
            f"Found {len(alert_df)} item(s) that require immediate reordering!"
        )
        st.dataframe(
            alert_df[["Component", "Category", "Stock_Qty"]],
            use_container_width=True,
        )

        # Download button for filtered CSV
        csv_data = alert_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Low-Stock Report (CSV)",
            data=csv_data,
            file_name="reorder_report.csv",
            mime="text/csv",
        )
    else:
        st.success("All inventory stock levels are healthy!")