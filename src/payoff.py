import numpy as np
from src.penetration import *


def get_technology_cost_cv2x(cv2x_used):
    """
    OBU cost of C-V2X is more expensive than ITS-G5, on average 13.5euros
    Source: https://unex.com.tw/public/uploads/shortcuts/ABI-DSRC-price-comparison.pdf
    :param cv2x_used: boolean stating if cars are equipped with C-V2X OBU
    :return: additional cost for equipping cars with C-V2X rather than ITS-G5, in million euros
    """
    # return x*13.5/1000000
    if cv2x_used:
        return -100
    else:
        return 0


def get_network_effects(x, previous_share, k=10):
    if x < 0 or x > 1:
        raise ValueError("x is not a valid number")

    else:
        return np.around(1 / (1 + np.exp(-k * (x + previous_share - 0.5))), 3) * 1000


def get_switching_cost(switching, switching_share):
    """
    The initial software development costs would be approximately €1mn per model,
    based on a team of ten engineers working for a year to develop the software (BMW 2014)
    Software expenses could be shared to some extent, still approx 50% of
    total development costs needed
    Assumption: switching from tech A to tech B means additional cost of 500.000 euro (1mil for new tech,
    but still 50% of that being paid when sticking to same tech)
    :param switching: boolean stating if technology is switched
    Source: https://ec.europa.eu/transport/sites/transport/files/2016-c-its-deployment-study-final-report.pdf
    :return: switching cost for implementing other tech, in million euros
    """
    if switching:
        return -200 * switching_share
    else:
        return 0
    # return 0.5*x


def get_total_payoff(itsg5_share, cv2x_share, switching, switching_share, cv2x_used, previous_share_itsg5, previous_share_cv2x):
    """

    :param switching_share:
    :param itsg5_share:
    :param cv2x_share:
    :param switching:
    :param cv2x_used:
    :return:
    """
    # To think: relative to share of tech or not ?
    # is itsg5_share*1/7 correct ?
    total_payoff = get_switching_cost(switching, switching_share) + \
                   np.around(get_technology_cost_cv2x(cv2x_used) * cv2x_share, 0) \
                   + np.around(get_network_effects(itsg5_share*1/7, previous_share_itsg5), 0) + \
                   np.around(get_network_effects(cv2x_share*1/7, previous_share_cv2x), 0)
    return total_payoff

def get_consortia_shares():
    shares = [25.7, 22.7, 10.2, 7.2, 7.1, 6.9, 6.2, 5.1]    # add source
    total_share = np.sum(shares)
    share_c2c_cc = (25.7/2+10.2/2+7.1/2+6.9)/total_share
    share_5gaa = (25.7/2+22.7+10.2/2+7.2+7.1/2+6.2+5.1)/total_share
    return share_c2c_cc, share_5gaa

def build_payoff_matrix(strategies):
    previous_share_itsg5 = get_penetration()['itsg5']
    previous_share_cv2x = get_penetration()['cv2x']
    print(previous_share_itsg5, previous_share_cv2x)
    shares = [25.7, 22.7, 10.2, 7.2, 7.1, 6.9, 6.2, 5.1]    # add source
    total_share = np.sum(shares)
    share_c2c_cc, share_5gaa = get_consortia_shares()

    payoff_matrix_c2c_cc = np.zeros((len(strategies), len(strategies)))
    payoff_matrix_5gaa = np.zeros((len(strategies), len(strategies)))

    # Initialize payoff matrixes
    for count_c2c_cc, strategy_c2c_cc in enumerate(strategies):  # The base strategy here is ITS_G5
        for count_5gaa, strategy_5gaa in enumerate(strategies): # change: not nested
            itsg5_share = strategy_c2c_cc * share_c2c_cc + strategy_5gaa * share_5gaa
            cv2x_share = 1 - itsg5_share
            switching = False

            if cv2x_share > 0:
                cv2x_used = True
            else:
                cv2x_used = False

            if strategy_c2c_cc <= 1:
                switching = True
            payoff_matrix_c2c_cc[count_c2c_cc, count_5gaa] = \
                np.around(get_total_payoff(itsg5_share, cv2x_share, switching, cv2x_share, cv2x_used, previous_share_itsg5, previous_share_cv2x), 1)
            switching = False

            if strategy_5gaa > 0:
                switching = True
            payoff_matrix_5gaa[count_c2c_cc, count_5gaa] = \
                np.around(get_total_payoff(itsg5_share, cv2x_share, switching, itsg5_share, cv2x_used, previous_share_itsg5, previous_share_cv2x), 1)

            array_c2c_cc = np.array(payoff_matrix_c2c_cc)
            array_5gaa = np.array(payoff_matrix_5gaa)
    return array_c2c_cc, array_5gaa
