import matplotlib.pyplot as plt

# # Data
# temperature = [0, 20, 40, 60, 80, 100]
# NaCl = [35.7, 36.0, 36.6, 37.3, 38.0, 39.0]
# NaNO3 = [73, 88, 105, 124, 148, 180]
# KI = [128, 144, 160, 176, 192, 208]
#
# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(temperature, NaCl, label="NaCl", marker='o')
# plt.plot(temperature, NaNO3, label="NaNO₃", marker='o')
# plt.plot(temperature, KI, label="KI", marker='o')
#
# # Customize
# plt.title("Solubility Curves for Various Compounds")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Solubility (g/100 mL)")
# plt.legend()
# plt.grid()
# plt.show()

#
# # Given solubility data for NaNO3
# temperatures = [10, 30, 45, 65]  # Saturation temperatures in °C
# solubility = [40, 80, 120, 160]  # Solubility in g/100mL
#
# # Create the solubility curve plot
# plt.figure(figsize=(8, 5))
# plt.plot(temperatures, solubility, marker='o', linestyle='-', color='b', label='NaNO3')
#
# # Labels and title
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Solubility (g/100mL)")
# plt.title("Solubility Curve of NaNO3")
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()


# Given solubility data for KI
# temperatures = [0, 15, 30, 50]  # Saturation temperatures in °C
# solubility = [40, 80, 120, 160]  # Solubility in g/100mL
#
# # Create the solubility curve plot
# plt.figure(figsize=(8, 5))
# plt.plot(temperatures, solubility, marker='o', linestyle='-', color='r', label='KI')
#
# # Labels and title
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Solubility (g/100mL)")
# plt.title("Solubility Curve of KI")
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()


# Given solubility data for NaCl
# temperatures = [25, 40, 60, 80, 100]  # Saturation temperatures in °C
# solubility = [40, 50, 60, 70, 80]  # Solubility in g/100mL
#
# # Create the solubility curve plot
# plt.figure(figsize=(8, 5))
# plt.plot(temperatures, solubility, marker='o', linestyle='-', color='g', label='NaCl')
#
# # Labels and title
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Solubility (g/100mL)")
# plt.title("Solubility Curve of NaCl")
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()

#
# # Solubility data
# temperatures_nano3 = [10, 30, 45, 65]
# solubility_nano3 = [40, 80, 120, 160]
#
# temperatures_ki = [0, 15, 30, 50]
# solubility_ki = [40, 80, 120, 160]
#
# temperatures_nacl = [25, 40, 60, 80, 100]
# solubility_nacl = [40, 50, 60, 70, 80]
#
# # Create the solubility curve plot
# plt.figure(figsize=(8, 5))
# plt.plot(temperatures_nano3, solubility_nano3, marker='o', linestyle='-', color='b', label='NaNO3')
# plt.plot(temperatures_ki, solubility_ki, marker='s', linestyle='-', color='r', label='KI')
# plt.plot(temperatures_nacl, solubility_nacl, marker='^', linestyle='-', color='g', label='NaCl')
#
# # Labels and title
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Solubility (g/100mL)")
# plt.title("Solubility Curves of NaNO3, KI, and NaCl")
# plt.legend()
# plt.grid(True)

# Show the plot
# plt.show()


# Solubility data
# temperatures_nano3 = [17, 32, 47, 87]
# solubility_nano3 = [80, 100, 120, 160]
#
# temperatures_ki = [0, 14, 24, 34]
# solubility_ki = [120, 135, 145, 160]
#
# temperatures_nacl = [70, 40, 60, 80, 100]
# solubility_nacl = [40, 50, 60, 70, 80]
#
# # Create the solubility curve plot
# plt.figure(figsize=(8, 5))
# plt.plot(temperatures_nano3, solubility_nano3, marker='o', linestyle='-', color='b', label='NaNO3')
# plt.plot(temperatures_ki, solubility_ki, marker='s', linestyle='-', color='r', label='KI')
# plt.plot(temperatures_nacl, solubility_nacl, marker='^', linestyle='-', color='g', label='NaCl')
#
# # Labels and title
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Solubility (g/100mL)")
# plt.title("Solubility Curves of NaNO3, KI, and NaCl")
# plt.title("Solubility Curves of NaNO3, KI, and NaCl")
#
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()
#
# import numpy as np
#
# # Data from the experiment
# Ce = np.array([0.019, 0.059, 0.128, 0.15, 0.23])  # Final Concentration (N)
# Ce_over_x_m = np.array([0.2085, 0.372, 0.661, 0.533, 0.757])  # Ce/(x/m)
#
# # Perform linear regression to find slope and intercept
# slope, intercept = np.polyfit(Ce, Ce_over_x_m, 1)
# print(intercept)
# # Langmuir constants
# a = 1 / intercept  # Langmuir constant a (g/g)
# b = slope * a      # Langmuir constant b (L/g)
#
# # Generate the best-fit line for the plot
# best_fit_line = slope * Ce + intercept
#
# # Plot the Langmuir Isotherm
# plt.figure(figsize=(8, 6))
# plt.scatter(Ce, Ce_over_x_m, color='blue', label='Experimental Data')
# plt.plot(Ce, best_fit_line, color='red', label=f'Best Fit Line: y = {slope:.3f}x + {intercept:.3f}')
# plt.xlabel('Ce (Final Concentration, N)')
# plt.ylabel('Ce/(x/m)')
# plt.title('Langmuir Isotherm')
# plt.grid(True)
# plt.legend()
#
# # Annotate the Langmuir constants on the plot
# # plt.text(0.1, 0.6, f'Langmuir Constants:\na = {a:.2f} g/g\nb = {b:.2f} L/g', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
#
# # Show the plot
# plt.show()
import numpy as np

# Data from the experiment
Ce = np.array([0.019, 0.059, 0.128, 0.15, 0.23])  # Final Concentration (N)
x_m = np.array([0.091125, 0.158625, 0.1935, 0.28125, 0.30375])  # x/m (g/g)

# Take logarithms for Freundlich Isotherm
log_Ce = np.log10(Ce)  # log(Ce)
log_x_m = np.log10(x_m)  # log(x/m)

# Perform linear regression to find slope and intercept
slope, intercept = np.polyfit(log_Ce, log_x_m, 1)

# Freundlich constants
n = 1 / slope  # Freundlich constant n
k_f = 10**intercept  # Freundlich constant k_f

# Generate the best-fit line for the plot
best_fit_line = slope * log_Ce + intercept

# Plot the Freundlich Isotherm
plt.figure(figsize=(8, 6))
plt.scatter(log_Ce, log_x_m, color='blue', label='Experimental Data')
plt.plot(log_Ce, best_fit_line, color='red', label=f'Best Fit Line: y = {slope:.3f}x + {intercept:.3f}')
plt.xlabel('log(Ce)')
plt.ylabel('log(x/m)')
plt.title('Freundlich Isotherm')
plt.grid(True)
plt.legend()

# Annotate the Freundlich constants on the plot
# plt.text(-1.8, -0.8, f'Freundlich Constants:\nk_f = {k_f:.3f}\nn = {n:.3f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Show the plot
plt.show()