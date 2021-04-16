import pandas as pd
import numpy as np
import os
from definitions import ASSETS_PATH


def read_penetration():
    return pd.read_csv(os.path.join(ASSETS_PATH, "penetration.csv"))


def get_new_total_cars(total_cars_previous, growth = 0.018):
    """
    242,727,242 car in 2019, 1.8% growth rate in 2019
    Assumption: constant growth rate  TODO Jarne: check for more historical growth rate?
    Source: https://www.acea.be/uploads/publications/report-vehicles-in-use-europe-january-2021.pdf
    :return: amount of cars for given year, in million cars
    """
    return total_cars_previous * (1 + growth)


def init_penetration():
    """
    Only to be run once in beginning to create penetration status file
    242,727,242 car in 2019, 1.8% growth rate in 2019
    Source: https://www.acea.be/uploads/publications/report-vehicles-in-use-europe-january-2021.pdf
    """

    df = pd.DataFrame({"total_cars": [get_new_total_cars(242.73)],
                       "new_cars": [0.0],
                       "new_cars_share": [0.0],
                       "itsg5_shares": [0.0],
                       "cv2x_shares": [0.0],
                       "new_itsg5": [0.0],
                       "new_cv2x": [0.0],
                       "removed_cars": [0.0],
                       "scrapped_itsg5": [0.0],
                       "scrapped_cv2x": [0.0],
                       "total_amount_itsg5": [0.0],
                       "total_amount_cv2x": [0.0],
                       "cits_penetration": [0.0],
                       "itsg5_penetration": [0.0],
                       "cv2x_penetration": [0.0]})

    df.to_csv(os.path.join(ASSETS_PATH, "penetration.csv"), index=False)


def get_penetration():
    """ gets the latest penetration of ITS-G5 and C-V2X

    :return: itsg5_penetration: float, cv2x_penetration: float
    """
    df = read_penetration()
    last_row = df.tail(1)
    itsg5_penetration = last_row["itsg5_penetration"].values[0]
    cv2x_penetration = last_row["cv2x_penetration"].values[0]

    return {"itsg5": itsg5_penetration, "cv2x": cv2x_penetration}


def get_removed_cars(total_cars):
    """ Get amount of cars removed from European fleet
    Avg age: 11.6 y
    Source: https://www.acea.be/statistics/article/average-age-of-the-eu-motor-vehicle-fleet-by-vehicle-type
    :return: removed_cars
    """
    removal_rate = 1 / 11.6  # on avg, each year 1/11.5 th share of the fleet leaves the fleet
    removed_cars = total_cars * removal_rate
    return removed_cars


def get_new_cars(total_cars_previous_period, total_cars, removed_cars):
    """ returns amount of new cars to cope with removed cars and obtain growth

    :param total_cars_previous_period: total cars previous time period
    :param total_cars: output of get_new_total_cars
    :param removed_cars: output of get_removed_cars
    :return: amount of newly introduced cars per year
    """
    incremental_growth = total_cars - total_cars_previous_period
    return removed_cars + incremental_growth


def scrappage_cits_func(x):
    """exp function to arrive +/- at 11.5 avg age """
    removal_rate_age = 0.03 * np.exp(1 / 11.5 * x)
    return removal_rate_age


def get_scrappage_cumprods(years):
    """ Get the factors to get scrap sizes

    :param years: amount of years into simulation
    :return: factors to multiply the amount of cars per generation
    """
    array = np.array([scrappage_cits_func(x) for x in range(years)])
    array_remain = 1 - array
    remain_rates = np.cumprod(array_remain)
    remove_rates = 1 - remain_rates

    # import matplotlib.pyplot as plt
    # plt.plot(remain_rates, label="remain")
    # plt.plot(remove_rates, label="remove")
    # plt.axvline(x=11.5, color='grey', ls='--', lw=1)
    # plt.axhline(y=0.5, color='grey', ls='--', lw=1)
    # plt.legend(loc="best")
    #
    # plt.show()

    return remove_rates


def get_scrapped_cars(new_cars_list):
    """ Return amount of cars that are scrapped in current year

    :param new_cars_array: list of yearly amounts
    :return: amount of scrapped cars (int)
    """
    years = len(new_cars_list)
    remove_rates = np.flip(get_scrappage_cumprods(years))  # oldest cars highest removal factor
    scrapped_per_age = new_cars_list * remove_rates  # element-wise multiplication
    # print(scrapped_per_age)

    total_scrapped_cars = np.sum(scrapped_per_age)
    return total_scrapped_cars


def get_new_cits_cars(cv2x_share, df, itsg5_share, new_car_share, new_cars):
    """ Get amount of new C-ITS cars based on last complete renewal cycle"""
    amount_years_to_full_revision = int(1/new_car_share)
    slice_year = amount_years_to_full_revision - 1  # previous n-1 periods + current period = full revision
    if len(df) < amount_years_to_full_revision:
        sumprod_itsg5 = np.dot(df["new_cars_share"].values, df["itsg5_shares"].values) + new_car_share * itsg5_share
        sumprod_cv2x = np.dot(df["new_cars_share"].values, df["cv2x_shares"].values) + new_car_share * cv2x_share
    else:
        sumprod_itsg5 = np.dot(df["new_cars_share"].values[-slice_year:],
                               df["itsg5_shares"].values[-slice_year:]) \
                        + new_car_share * itsg5_share
        sumprod_cv2x = np.dot(df["new_cars_share"].values[-slice_year:],
                              df["cv2x_shares"].values[-slice_year:]) \
                       + new_car_share * cv2x_share
    new_itsg5 = new_cars * sumprod_itsg5
    new_cv2x = new_cars * sumprod_cv2x
    return new_cv2x, new_itsg5


def update_penetration(itsg5_share, cv2x_share, new_car_share=1 / 7):
    """ Updates penetration file with outcome of game
    Assumption: one game per year
    1/7th of fleet makes decision per year

    :param itsg5_share: amount of new c-its cars equipped with itsg5
    :param cv2_share: amount of new c-its cars equipped with cv2x
    :param new_car_share: amount of new cars equipped with cits
    """
    assert itsg5_share + cv2x_share <= 1, "Please provide valid shares for its-g5 and c-v2x"
    assert new_car_share <= 1, "Please provide new car share smaller than one"

    df = read_penetration()
    total_cars_previous_period = df.tail(1)["total_cars"].values[0]

    total_cars = get_new_total_cars(total_cars_previous_period)  # apply growth rate
    removed_cars = get_removed_cars(total_cars)
    new_cars = get_new_cars(total_cars_previous_period, total_cars, removed_cars)

    # new cits cars
    new_cv2x, new_itsg5 = get_new_cits_cars(cv2x_share, df, itsg5_share, new_car_share, new_cars)

    # scrapped cits cars
    scrapped_itsg5 = get_scrapped_cars(np.append(df["scrapped_itsg5"].values, new_itsg5))
    scrapped_cv2x = get_scrapped_cars(np.append(df["scrapped_cv2x"].values, new_cv2x))

    # total amount cits
    total_amount_itsg5 = df.tail(1)["total_amount_itsg5"].values[0] + new_itsg5 - scrapped_itsg5
    total_amount_cv2x = df.tail(1)["total_amount_cv2x"].values[0] + new_cv2x - scrapped_cv2x

    # penetration
    itsg5_penetration = total_amount_itsg5 / total_cars
    cv2x_penetration = total_amount_cv2x / total_cars
    cits_penetration = itsg5_penetration + cv2x_penetration

    new_df = df.append({"total_cars": total_cars,
                        "new_cars": new_cars,
                        "new_cars_share": new_car_share,
                        "itsg5_shares": itsg5_share,
                        "cv2x_shares": cv2x_share,
                        "new_itsg5": new_itsg5,
                        "new_cv2x": new_cv2x,
                        "removed_cars": removed_cars,
                        "scrapped_itsg5": scrapped_itsg5,
                        "scrapped_cv2x": scrapped_cv2x,
                        "total_amount_itsg5": total_amount_itsg5,
                        "total_amount_cv2x": total_amount_cv2x,
                        "cits_penetration": cits_penetration,
                        "itsg5_penetration": itsg5_penetration,
                        "cv2x_penetration": cv2x_penetration}, ignore_index=True)

    # print(new_df)
    new_df.to_csv(os.path.join(ASSETS_PATH, "penetration.csv"), index=False)


if __name__ == "__main__":
    # init file
    init_penetration()

    # test
    import random

    for i in range(10):  # 7 years for 1 revision cycle
        rand_float = np.random.random()
        update_penetration(rand_float, 1 - rand_float, new_car_share=1 / 7)  # 1/7: default

    print(get_penetration())

    result_df = read_penetration()
    print(result_df)
