import matplotlib.pyplot as plt

def drawGraph(X, Y, lr, reducer):
    predict = lr.predict_(X)

    plt.plot(X, Y, 'bo', X, predict, 'r-')

    # options
    axes = plt.gca()
    axes.set_xlabel("milage / {} (in km)".format(int(1/reducer)))
    axes.set_ylabel("price / {}".format(int(1/reducer)))

    plt.title("Car prices by mileage")
    plt.legend(["data set", "linear regression predictions"])
    plt.grid(True)

    print("Close graphic to return\n")
    plt.show()
