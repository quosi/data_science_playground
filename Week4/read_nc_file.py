from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

m = Dataset("Complete_TAVG_EqualArea.nc", "r", format="NETCDF4")

print(m.dimensions.keys())
t = m.variables['temperature']

# pick the 1000th data point
N = 1000

print(m['time'][N])
title = f"lat: {m['latitude'][N]:8.2f}    long: {m['longitude'][N]:8.2f}"
print(title)
# time series for one location
ma = t[:, 1000]
a = np.array(ma)

plt.plot(range(3232), a)
plt.title(title)
plt.show()
