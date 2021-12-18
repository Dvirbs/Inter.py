import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd


def saving_data_intence_theta():
    path = 'C:/Google One/University/Third year/Lab_B_1/Interference/intence(theta)_measurments/intence(theta)_last_mesur.xlsx'
    df = pd.read_excel(path)
    theta_voltage = np.array(df["Ch0_V"].tolist())
    intensity_voltage = np.array(df["Ch1_V"].tolist())
    return theta_voltage, intensity_voltage


def intence_VS_theta_graph():
    theta, intensity_voltage = saving_data_intence_theta()
    print(linregress(theta, intensity_voltage))
    plt.plot(theta, intensity_voltage, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=8)
    # plt.xlim(-3, 3)
    # plt.ylim(-3, 3)

    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('intence_VS_theta')
    plt.show()


def saving_data_intence_theta_try2():
    path = 'C:/Google One/University/Third year/Lab_B_1/Interference/intence(theta)_measurments/intence(theta)_last_mesur_try2.xlsx'
    df = pd.read_excel(path)
    theta_voltage = np.array(df["Ch0_V"].tolist())
    intensity_voltage = np.array(df["Ch1_V"].tolist())
    return theta_voltage, intensity_voltage


def intence_VS_theta_graph_try2():
    theta, intensity_voltage = saving_data_intence_theta_try2()
    print(linregress(theta, intensity_voltage))
    plt.plot(theta, intensity_voltage, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=8)
    # plt.xlim(-3, 3)
    # plt.ylim(-3, 3)

    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('intence_VS_theta')
    plt.show()


def saving_data_intence_theta_try1():
    path = 'C:/Google One/University/Third year/Lab_B_1/Interference/intence(theta)_measurments/intence(theta)_last_mesur_try1.xlsx'
    df = pd.read_excel(path)
    theta_voltage = np.array(df["Ch0_V"].tolist())
    intensity_voltage = np.array(df["Ch1_V"].tolist())
    return theta_voltage, intensity_voltage


def intence_VS_theta_graph_try1():
    theta_voltage, intensity_voltage = saving_data_intence_theta_try1()
    intensity_voltage = abs(intensity_voltage)
    theta = theta_voltage / 0.17
    print(linregress(theta, intensity_voltage))
    plt.plot(theta, intensity_voltage, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=1)
    plt.xlim(-15, 15)
    plt.ylim(-1, 13)

    plt.xlabel('Theta_voltage - axis')
    plt.ylabel('intensity_voltage - axis')
    plt.title('intence_VS_theta')
    plt.savefig('intence_VS_theta_best_try')


intence_VS_theta_graph_try1()