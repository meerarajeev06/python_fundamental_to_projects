import matplotlib.pyplot as plt
import seaborn as sns

# Set a professional dark/light grid style automatically
sns.set_theme(style="whitegrid")

components = ["LED", "ESP32", "Arduino", "Resistor"]
power_mw = [40, 528, 250, 2.5]

plt.bar(components, power_mw, color="orange")
plt.title("Power Consumption by Component")
plt.ylabel("Power (mW)")
plt.show()