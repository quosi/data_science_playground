print("intercept: ", m.intercept_)
ypred = m.predict(X)
pop = pd.read_excel('gapminder_population.xlsx', index_col=0)
xfuture = [[2020], [2030]]
yfuture = np.exp(yfuture) / 1000_000_000
print("R-squared: ", m.score(X, y))
plt.plot(X, y)
yfuture = m.predict(xfuture)
print(f"population forecast for {year}: {forecast:5.1f} bln")
from sklearn.linear_model import LinearRegression
import pandas as pd
pop.index = pop.index.astype(int)
y = logpop.values
for year, forecast in zip(xfuture, yfuture):
m.fit(X, y)
print("slope    : ", m.coef_[0])
m = LinearRegression()
from matplotlib import pyplot as plt
logpop = np.log(pop)
pop = pop.sum()
logpop.dropna(inplace=True)
import numpy as np
plt.show()
plt.plot(X, ypred)
X = logpop.index.values.reshape(-1, 1)
