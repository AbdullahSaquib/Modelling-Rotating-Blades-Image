import math

"""
Pressure Conversions
"""


def Pa_to_atm(P):
    return 9.86923 * 1e-6 * P


def Pa_to_bar(P):
    return 1e-5 * P


def atm_to_Pa(P):
    return (1.01e5) * P


def bar_to_Pa(P):
    return 1e5 * P


"""
Temperature conversions
"""


def K_to_degC(T):
    return T - 273.15


def degC_to_K(T):
    return T + 273.15


"""
Volume Conversions
"""


def m3_to_L(V):
    return 1000 * V


def L_to_m3(V):
    return 0.001 * V


def cm3_to_m3(V):
    return 1e-6 * V


def m3_to_cm3(V):
    return 1e6 * V


"""
Angle Conversions
"""


def rad_to_deg(x):
    return 180 * x / math.pi


def deg_to_rad(x):
    return math.pi * x / 180


"""
Time conversions
"""


def years_to_seconds(years):
    return years * 365 * 24 * 60 * 60


"""
Energy Convesions
"""


def cal_to_J(E):
    return 4.184 * E


def J_to_cal(E):
    return E / 4.184
