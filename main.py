import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from ft_linear_regression import ft_linear_regression

data = pd.read_csv("./resources/data.csv")

X = np.array(data.km).reshape(-1,1)
Y = np.array(data.price).reshape(-1,1)

thetas = [8000., 0.]
alpha = 1e-10
n_cycle = 100000
print("alpha = {}\nn_cycle = {}".format(alpha, n_cycle))

lr = ft_linear_regression(thetas, alpha=alpha, n_cycle=n_cycle)

MSE = int(lr.mse_(X, Y))
print("\nthetas = {}\nmse = {}".format(lr.thetas.T, MSE))

print("\ntraining ...", end=" ")
lr.fit_(X, Y)
print("done.")

MSE = int(lr.mse_(X, Y))
print("\nthetas = {}\nmse = {}".format(lr.thetas.T, MSE))

predict = lr.predict_(X)

plt.plot(X, Y, 'bo', X, predict, 'r-')
plt.grid(True)
plt.show()