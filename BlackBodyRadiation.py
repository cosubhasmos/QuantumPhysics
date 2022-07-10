# Planck’s law for Black Body radiation, Checked Corrected And Modified By - Subhash
# This project is open and free to use.

import numpy as np
from scipy.constants import h, c, k, pi
import matplotlib.pyplot as plt

newparams = {'axes.labelsize': 10, 'axes.linewidth': 1.5, 'savefig.dpi':
    1000,
             'lines.linewidth': 2, 'figure.figsize': (18, 12),
             'legend.frameon': True,
             'legend.handlelength': 0.7}

plt.rcParams.update(newparams)

L0 = np.arange(0.1, 30, 0.005)  # Wavelength in micro m
L = L0 * 1e-6  # wavelength in m


def planck_lamda(L, T):
    a = (8 * pi * h * c) / L ** 5
    b = (h * c) / (L * k * T)
    c1 = np.exp(b) - 1
    d = a / c1
    return d


plt.suptitle("""Planck’s law for Black Body radiation & Raleigh-Jeans Law at high & low temperature""",
             size=14, color='g', fontstyle="italic")

R_Ht = (8 * pi * k * 1100) / L ** 4  # Rayleigh's law at High temperature
R_Lt = (8 * pi * k * 200) / L ** 4  # Rayleigh's law at Low temperature

T500 = planck_lamda(L, 500)
T700 = planck_lamda(L, 700)
T900 = planck_lamda(L, 900)
T1100 = planck_lamda(L, 1100)


plt.subplot(2, 2, (1, 2))
plt.plot(L, T500, label='T=500 K')
plt.plot(L, T700, label='T=700 K')
plt.plot(L, T900, label='T=900 K')
plt.plot(L, T1100, label='T=1100 K')
plt.legend(loc="best", prop={'size': 12})
plt.xlabel(r"$\lambda$ ")
plt.ylabel(r"U($\lambda $,T )")
plt.title("Planck Law of Radiation")
plt.ylim(0, 300)
plt.xlim(0, 0.00002)

plt.subplot(2, 2, 3)
plt.plot(L, (planck_lamda(L, 200)), label='Planck Law')
plt.plot(L, R_Lt, "--", label="Rayleigh-Jeans Law")
plt.legend(title="Comparison at low Temperature", loc="best", prop={'size': 12})
plt.xlabel(r"$\lambda$ ")
plt.ylabel(r"U($\lambda $,T )")
plt.title("T=200 K (For Low Temperature)")
plt.ylim(0, 0.5)
plt.xlim(0, 0.00003)

plt.subplot(2, 2, 4)
plt.plot(L, T1100, label='Planck Law')
plt.plot(L, R_Ht, "--", label="Rayleigh-Jeans Law")
plt.legend(title="Comparison at high Temperature", loc="best", prop={'size': 12})
plt.xlabel(r"$\lambda$ ")
plt.ylabel(r"U($\lambda $,T )")
plt.title("T=1100 K (For High Temperature)")
plt.ylim(0, 350)


plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

plt.show()

