import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from ft_linear_regression import ft_linear_regression
from drawGraph import drawGraph
from estimatePrice import estimatePrice

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
print("\nthetas = {}\nmse = {}\n".format(lr.thetas.T, MSE))

selection = 0
while selection != 3:
    choices = [1, 2, 3]

    selection = input("\nPlease select an option by typing the corresponding number:\n\
1: Draw graphic\n\
2: Estimate price\n\
3: Quit\n")

    if selection.isdigit():
        selection = int(selection)

    while not selection in choices:
        selection = input("This option does not exist, please type the corresponding number.\n\
To exit, enter 3.\n")
        if selection.isdigit():
            selection = int(selection)

    if selection == 1:
        drawGraph(X, Y, lr, reducer)        
    elif selection == 2:
        estimatePrice(lr, reducer)




