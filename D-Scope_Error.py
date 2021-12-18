import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd


def saving_data_error():
    path = 'C:/Google One/University/Third year/Lab_B_1/Interference/Measuring_instruments/D-scope_error.xlsx'
    df = pd.read_excel(path)
    time = np.array(df["time"].tolist())
    theta_voltage = np.array(df["Ch0_V"].tolist())
    intensity_voltage = np.array(df["Ch1_V"].tolist())
    return time, theta_voltage, intensity_voltage


def theta_error():
    time, theta_voltage, intensity_voltage = saving_data_error()
    max_theta = max(theta_voltage)
    min_theta = min(theta_voltage)
    theta_error = max_theta-min_theta
    print('The Voltage of theta differences between maximum value measured and the min', theta_error)
    print()
    max_intens = max(intensity_voltage)
    min_intens = min(intensity_voltage)
    v_intens_error = max_intens-min_intens
    print('The voltage intensity differences between maximum and min value measured is ', v_intens_error)

