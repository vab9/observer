import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from brownian import brownian
from volatility_gen import generate_volatility


data = pd.read_csv('../Exporte/Tagesverkauf.csv', sep=";")


print(data[:3])

# init daily demand = 2000 pcs
initial_demand = 1100
# stdeviation
stdev = 50
# run for certain amount of years
period = 365
max_time_point = 5 * period

delta = 2

# for i in range(1):
#     brownian_sample = brownian(initial_demand, max_time_point, 1, delta)
#     volitility_sample = generate_volatility(initial_demand, max_time_point, 0.01)
#     x = np.arange(max_time_point)
#     plt.plot(x, brownian_sample, label="brownian motion")
#     plt.plot(x, volitility_sample, label="volatility algorithm")

# plt.legend()
# plt.show()

# write values to csv
# distr = np.random.normal(initial_demand, stdev, max_time_point)
# with open("out.csv", "w") as f:
#     f.write("timestep, value\n")
#     for (i, val) in enumerate(distr):
#         # val = "---"
#         f.write("{}, {}".format(i, val))
#         f.write("\n")

print('...done!')
