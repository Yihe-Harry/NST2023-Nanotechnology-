import numpy as np
import matplotlib.pyplot as plt

# Define the energy equation
def interaction_energy(r):
    return -(4.03 * 10**(-28)) / r + (6.97 * 10**(-96)) / (r**8)

# Define range of r (distance in meters)
r_values = np.linspace(0.2e-9, 1e-9, 500)  # From 0.2 nm to 0.6 nm
E_values = interaction_energy(r_values)

# Plot the interaction energy curve
plt.figure(figsize=(8, 5))
plt.plot(r_values * 1e9, E_values, label="Interaction Energy", color="blue")
plt.axvline(x=0.28, color='red', linestyle='--', label="Equilibrium distance (0.28 nm)")
plt.axhline(y=0, color='black', linestyle='-')

# Labels and title
plt.xlabel("Distance r (nm)")
plt.ylabel("Energy E (J)")
plt.title("Interaction Energy vs. Distance for NaCl Ion Pair")
plt.legend()
plt.grid()

# Show plot
plt.show()
