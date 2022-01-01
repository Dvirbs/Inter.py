import mercury
import mercury_wave_length
import numpy as np


def cal_angle_error():
    theata_radian_picks_values = mercury_wave_length.theta_picks_values()
    theata_dagree_picks = theata_radian_picks_values * 180 / np.pi
    theta_voltage_picks = theata_dagree_picks * 0.17
    dv = 0.00258 / 2
    d0_To_dv = 1 / 0.17  # =a
    da = 0.213 / 2
    d0_TO_da = theta_voltage_picks  # = v
    delta_theta_dag = np.sqrt((dv * d0_To_dv) ** 2 + (da * d0_TO_da) ** 2)
    delta_theta_radian = delta_theta_dag * np.pi / 180
    print('delta_theta_of_picks: ', delta_theta_radian)
    return delta_theta_radian


def cal_wave_lengh_error():
    d = 3.9207 * 10 ** -6
    d0_vector = cal_angle_error()  # delta_theta_radian
    delta_d = 0.0346 * 10 ** -6
    theta = mercury_wave_length.theta_picks_values()  # theata_radian_picks_values
    print(theta)
    d_lemda = list()
    for index in range(len(d0_vector)):
        d_error = delta_d * theta[index]
        O_error = d * d0_vector[index]
        res = np.sqrt(d_error ** 2 + O_error ** 2)
        d_lemda.append(res)
    print(d_lemda)  # just for consistency od smaller ro the right
    return d_lemda


if __name__ == '__main__':
    cal_angle_error()
    cal_wave_lengh_error()
