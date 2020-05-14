import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from ft_linear_regression import ft_linear_regression

data = pd.read_csv("./resources/data.csv")

X = np.array(data.km).reshape(-1,1)
Y = np.array(data.price).reshape(-1,1)

# reduce data size
reducer = 1e-4
X = X * reducer
Y = Y * reducer

# without reducing data
# thetas = [8000., 0.]
# alpha = 1e-10
# n_cycle = 100000

thetas = [0., 0.]
alpha = 1e-3
n_cycle = 150000

print("alpha = {}\nn_cycle = {}".format(alpha, n_cycle))

lr = ft_linear_regression(thetas, alpha=alpha, n_cycle=n_cycle)

MSE = lr.mse_(X, Y)
print("\nthetas = {}\nmse = {}".format(lr.thetas.T, MSE))

print("\ntraining ...", end=" ")
lr.fit_(X, Y)
print("done.")

MSE = lr.mse_(X, Y)
print("\nthetas = {}\nmse = {}".format(lr.thetas.T, MSE))

predict = lr.predict_(X)

plt.plot(X, Y, 'bo', X, predict, 'r-')

# options
axes = plt.gca()
axes.set_xlabel("milage / {} (in km)".format(int(1/reducer)))
axes.set_ylabel("price / {}".format(int(1/reducer)))

plt.title("Car prices by mileage")
plt.legend(["data set", "linear regression predictions"])
plt.grid(True)

plt.show()