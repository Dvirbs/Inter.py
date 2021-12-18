import mercury
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np


def preparing_data():
    Theta_voltage, Intensity_voltage = mercury.saving_data_intence_theta()
    theta_centered = mercury.intensity_to_center(Theta_voltage)[:2150]
    print(theta_centered[876])
    return abs(Intensity_voltage[:2150])

def local_maximum():
    x = preparing_data()
    peaks, _ = find_peaks(x, height=0.1, distance=150)
    print('****** \npeaks is ', peaks)
    print('****** \nx[peaks] is ', x[peaks])
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.plot(np.zeros_like(x), "--", color="gray")
    plt.show()

preparing_data()
local_maximum()