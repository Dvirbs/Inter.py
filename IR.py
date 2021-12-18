import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def saving_data_intence_theta():
    path = r'C:\Google One\University\Third year\Lab_B_1\Interference\python_project\infra_red_data\IR.xlsx'
    df = pd.read_excel(path)
    theta_voltage = np.array(df["Ch0_V"].tolist())
    intensity_voltage = np.array(df["Ch1_V"].tolist())
    return theta_voltage, intensity_voltage


def data_norm(intensity_voltage=saving_data_intence_theta()[1]):
    max_intensity = max(abs(intensity_voltage))
    max_intensity_index = 2699
    norm_intensity = []
    for value in abs(intensity_voltage):
        norm_intensity.append(value / max_intensity)
    return np.array(norm_intensity)


def intensity_to_center(theta_voltage):
    theta_of_max_intence = -0.175849
    theta_centered = []
    for value in theta_voltage:
        theta_centered.append(value - theta_of_max_intence)
    return np.array(theta_centered)


def Average(lst):
    return sum(lst) / len(lst)


def data_average(intensity_voltage=saving_data_intence_theta()[1]):
    average_intensity = Average(abs(intensity_voltage))
    norm_intensity = []
    for value in abs(intensity_voltage):
        norm_intensity.append(value / average_intensity)
    return np.array(norm_intensity)


def IR_intense_graph():
    theta, intensity_voltage = saving_data_intence_theta()
    # average_intensity = data_average(intensity_voltage)
    theta_centered = intensity_to_center(theta)

    # plt.plot(theta_centered, average_intensity, color='green', linestyle='dashed', linewidth=3,
    #          marker='o', markerfacecolor='blue', markersize=2)
    plt.plot(theta_centered, abs(intensity_voltage))

    # plt.xlim(0.8, 1.5)
    # plt.ylim(0, 2)

    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('IR_intense_graph')
    plt.show()


IR_intense_graph()
