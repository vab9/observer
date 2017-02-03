"""
generate_volatility() generates volatile time series data
"""

# File: volatility_gen.py

import numpy as np

def generate_volatility(initial, n, volatility):
    # return np.fromiter(vol_iter(initial, n, volatility), np.float)
    res = []
    current = initial
    for i in range(n):
        res.append(current)
        current = vol_iter(current, volatility)
    return np.array(res)

def vol_iter(value, volatility):
    current = value
    r = np.random.random()
    change_percent = 2 * volatility * r
    if change_percent > volatility:
        change_percent -= 2 * volatility
    return current * (1 + change_percent)
