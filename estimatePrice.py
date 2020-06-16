import numpy as np

def estimatePrice(lr, reducer):
    milage = 0
    while milage != 'return':

        milage = input("\nEnter a value in km (or type 'return')\n")
        while not milage:
            milage = input("Can't be empty! Enter a value in km (or type 'return')\n")

        if milage != 'return' and milage.isdigit():
            milage = int(milage)
            value = np.array([milage*reducer]).reshape(-1,1)
            predict = lr.predict_(value)[0,0]/reducer
            print("The estimate price for this milage is : {:.2f}".format(predict))
        elif milage != 'return':
            print("Oops! Format error : has to be a positif number")