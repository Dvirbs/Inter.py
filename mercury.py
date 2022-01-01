import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def raw_data():
    path = r'C:\Google One\University\Third year\Lab_B_1\Interference\python_project\mercory_data\mercoty1_sh15000_try3.xlsx'
    df = pd.read_excel(path)
    theta_voltage = np.array(df["Ch0_V"].tolist())
    intensity_voltage = np.array(df["Ch1_V"].tolist())
    return theta_voltage, intensity_voltage


def theta_in_radian(theta_voltage=raw_data()[0]):
    """
    converting theta voltage value to dagree
    :param theta_voltage: values of theta as voltage
    :return: np array of theta dagree
    """
    theta_deg = theta_voltage * (1 / 0.17)
    theta_red = theta_deg*np.pi/180
    return theta_red


def theta_of_max_intence(theta_values=theta_in_radian(), intensity_voltage=raw_data()[1]):
    max_intence = max(abs(intensity_voltage))
    maxi_index = (abs(intensity_voltage) == max_intence)
    theta_of_max_intence = theta_values[maxi_index]
    return theta_of_max_intence


def centered_theta(theta_values=theta_in_radian()):
    theta_max = theta_of_max_intence()
    theta_centered = theta_values - theta_max
    return theta_centered


def data_norm(intensity_voltage=raw_data()[1]):
    max_intensity = max(abs(intensity_voltage))
    norm_intensity = []
    for value in abs(intensity_voltage):
        norm_intensity.append(value / max_intensity)
    return np.array(norm_intensity)


def intensity_average_value(lst):
    return sum(lst) / len(lst)


def average_intenicty_list(intensity_voltage=raw_data()[1]):
    average_intensity = intensity_average_value(abs(intensity_voltage))
    everages_lst = list()
    for value in abs(intensity_voltage):
        everages_lst.append(value/average_intensity)
    return np.array(everages_lst)


def plot_all_graph(intensity, theta):
    plt.plot(theta, intensity)
    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('mercury_intense')
    plt.show()
    # plt.savefig('mercury_intense_graph')


def locals_maximum_graph(intensity, theta):
    plt.plot(theta, intensity)
    plt.xlim(0.07, 0.17)
    plt.ylim(0, 1.5)
    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('mercury_intense')
    plt.show()


if __name__ == '__main__':
    plot_all_graph(average_intenicty_list(), centered_theta())
    locals_maximum_graph(average_intenicty_list(), centered_theta())
