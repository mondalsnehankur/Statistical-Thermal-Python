import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Input data
T = np.array([451, 452, 455, 458, 460])  # Temperature in Kelvin
chi = np.array([110, 51, 12, 10, 1.5])   # Magnetic susceptibility
Tc = 450  # Critical temperature in Kelvin

# Step 2: Compute reduced temperature t = (T - Tc) / Tc
t = (T - Tc) / Tc

# Step 3: Take natural logarithms to linearize the equation
ln_t = np.log(t)
ln_chi = np.log(chi)

# Step 4: Perform linear regression: ln(chi) = ln(chi0) - gamma * ln(t)
slope, intercept, r_value, p_value, std_err = linregress(ln_t, ln_chi)

gamma = -slope            # gamma is -slope of the linear fit
chi0 = np.exp(intercept)  # chi0 = exp(intercept)

# Step 5: Print results
print(f"Estimated gamma (γ): {gamma:.4f}")
print(f"Estimated chi0 (χ₀): {chi0:.4f}")

# Step 6: Plotting ln(chi) vs ln(t)
plt.figure(figsize=(8, 5))
plt.plot(ln_t, ln_chi, 'o', label='Data points')
plt.plot(ln_t, intercept + slope * ln_t, 'r-', label='Linear fit')
plt.xlabel('$ln(t)$ ------>')
plt.ylabel('$ln(χ)$ ------>')
plt.title('Linear fit to estimate χ₀ and γ')
plt.grid(True)
plt.legend()
plt.show()

'''
Output:
Estimated gamma (γ): 1.6056
Estimated chi0 (χ₀): 0.0075
'''