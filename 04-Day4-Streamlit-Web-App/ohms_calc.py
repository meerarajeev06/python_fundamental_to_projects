import streamlit as st

# Page Configuration
st.set_page_config(page_title="Ohm's Law & Power Calculator", page_icon="⚡")

# Header Section
st.title("⚡ ECE Workbench: Ohm's Law & Power Calculator")
st.write(
    "Adjust Voltage and Resistance using the controls below to calculate Current ($I$) and Power ($P$) in real time."
)

st.divider()

# Input Controls
st.subheader("🎛️ Input Parameters")

col1, col2 = st.columns(2)

with col1:
    voltage = st.number_input(
        "Voltage (V) [Volts]",
        min_value=0.0,
        max_value=1000.0,
        value=12.0,
        step=0.5,
        help="Supply voltage in Volts",
    )

with col2:
    resistance = st.number_input(
        "Resistance (R) [Ohms Ω]",
        min_value=0.0,
        max_value=10000.0,
        value=100.0,
        step=1.0,
        help="Circuit resistance in Ohms",
    )

st.divider()

# Calculation & Logic Section
st.subheader("📊 Output Metrics")

# Guard against Division by Zero
if resistance == 0:
    st.error(
        "⚠️ **Short Circuit Warning:** Resistance cannot be 0 Ω! Division by zero is undefined."
    )
else:
    # Calculations
    current_amps = voltage / resistance
    power_watts = voltage * current_amps

    # Unit formatting helper (e.g., mA vs A, mW vs W)
    if current_amps < 1 and current_amps > 0:
        current_display = f"{current_amps * 1000:.2f} mA"
    else:
        current_display = f"{current_amps:.4f} A"

    if power_watts < 1 and power_watts > 0:
        power_display = f"{power_watts * 1000:.2f} mW"
    else:
        power_display = f"{power_watts:.4f} W"

    # Metric Cards Display
    m1, m2 = st.columns(2)

    with m1:
        st.metric(
            label="Current (I)",
            value=current_display,
            help="Formula: I = V / R",
        )

    with m2:
        st.metric(
            label="Power Dissipation (P)",
            value=power_display,
            help="Formula: P = V × I",
        )

    # Formula Cheat Sheet
    with st.expander("ℹ️ View Formulas Used"):
        st.latex(r"I = \frac{V}{R}")
        st.latex(r"P = V \times I = \frac{V^2}{R} = I^2 \times R")