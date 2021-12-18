import mercury
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np


def preparing_data():
    Theta_voltage, Intensity_voltage = mercury.saving_data_intence_theta()
    theta_centered = mercury.intensity_to_center(Theta_voltage)[:2150]
    return abs(Intensity_voltage[:2150])


def picks_value():
    Theta_voltage, Intensity_voltage = mercury.saving_data_intence_theta()
    theta_centered = mercury.intensity_to_center(Theta_voltage)[:2150]
    # peaks in  [ 876 1211 1453]
    # intencity on the picks [0.11265408 0.13715785 0.14747523]
    print('theta_value on pick #876 is', theta_centered[876])
    print('theta_value on pick #1211 is', theta_centered[1211])
    print('theta_value on pick #1453 is', theta_centered[1453])


def local_maximum():
    x = preparing_data()
    peaks, _ = find_peaks(x, height=0.1, distance=150)
    print('****** \npeaks is ', peaks)
    print('****** \nx[peaks] is ', x[peaks])
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.plot(np.zeros_like(x), "--", color="gray")
    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('local_maximum_mercury_intense_graph')
    plt.savefig('local_maximum_mercury_intense_graph')


picks_value()
preparing_data()
local_maximum()