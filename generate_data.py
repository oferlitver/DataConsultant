"""
File for generation of time-series data
"""

import os
import string
import numpy as np
import pandas as pd

print(os.getcwd())

my_seed = 271828
np.random.seed(my_seed)


def generate_data(n_days, a, b):
    """make a straight line with intercept a and slope b"""
    return a + b * np.arange(n_days)


def noise_data(raw_data, sigma):
    """add random(0, sigma) to each value of raw_data"""
    return raw_data + np.random.normal(0, sigma, raw_data.size)


def build_data_frame(start_date, n_days, a, b, sigma):
    dates = pd.date_range(start=start_date, periods=n_days)
    df = pd.DataFrame(index=dates)
    for i in range(len(a)):
        raw_data = generate_data(n_days=n_days, a=a[i], b=b[i])
        data = noise_data(raw_data, sigma)
        # adds a column named 'a', 'b', 'c', etc.
        df[string.ascii_lowercase[i]] = data
        # also works: df[chr(i+97)] = data
    return df


if __name__ == "__main__":
    df = build_data_frame(start_date="2016-10-01",
                          n_days=60,
                          a=(100, 120),
                          b=(0.5, 0.6),
                          sigma=5)
    try:
        df.to_csv("/data/historic_data.csv")
    except FileNotFoundError:
        df.to_csv("historic_data.csv")