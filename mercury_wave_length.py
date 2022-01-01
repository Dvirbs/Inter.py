import errors_calculate
import mercury
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np


def mercury_data():
    Intensity_voltage = mercury.average_intenicty_list()[500:2150]
    theta_deg = mercury.centered_theta()[500:2150]
    # plt.plot(theta_deg, Intensity_voltage)
    # plt.show()
    return Intensity_voltage, theta_deg


def intensity_local_maximum():
    intesity, theta = mercury_data()
    peaks, dic = find_peaks(intesity, height=0.3, distance=100)
    return peaks


def theta_picks_values(peaks=intensity_local_maximum()):
    theta_values = mercury_data()[1]
    theata_picks_values = theta_values[peaks]
    #print('theata_picks_values: ', theata_picks_values)
    return theata_picks_values


def calculate_wave_length():
    theata_picks_values = theta_picks_values()
    wave_length_everge = theata_picks_values * 3.9062 * 10 ** -6
    wave_length_right = theata_picks_values * 3.9207 * 10 ** -6
    print('wave_length_everge', wave_length_everge)
    print('wave_length_right', wave_length_right)
    return wave_length_right


def local_maximum():
    # Theta_voltage, Intensity_voltage = mercury.saving_data_intence_theta()
    # theta_deg = mercury.theta_voltageTo_dagreTo_radians(Theta_voltage)

    x, theta = mercury_data()
    peaks, dic = find_peaks(x, height=0.3, distance=100)
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.plot(np.zeros_like(x), "--", color="gray")
    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('local_maximum_mercury_intense_graph')
    plt.show()
    # plt.savefig('local_maximum_mercury_intense_graph')


if __name__ == '__main__':
    # mercury_data()
    # intensity_local_maximum()
    # theta_picks_values()
    calculate_wave_length()
    print(errors_calculate.cal_wave_lengh_error())
