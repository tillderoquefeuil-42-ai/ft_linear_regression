import matplotlib.pyplot as plt

def drawGraph(X, Y, lr, reducer):
    predict = lr.predict_(X)

    plt.plot(X/reducer, Y/reducer, 'bo', X/reducer, predict/reducer, 'r-')

    # options
    axes = plt.gca()
    axes.set_xlabel("milage (in km)")
    axes.set_ylabel("price")

    plt.title("Car prices by mileage")
    plt.legend(["data set", "linear regression predictions"])
    plt.grid(True)

    print("Close graphic to return\n")
    plt.ion()
    plt.show()
