#importing libraries
import matplotlib.pyplot as plt
import pandas as pd
#defining function
def linechart():
#loading CSV file
    cd=pd.read_csv("statsfinal.csv")
#plotting line graph
    plt.plot(cd["Year"],cd["Q-P1"],label="Q-P1")
    plt.plot(cd["Year"],cd["Q-P2"],label="Q-P2")
    plt.plot(cd["Year"],cd["Q-P3"],label="Q-P3")
    plt.plot(cd["Year"],cd["Q-P4"],label="Q-P4")
#plotting labels
    plt.xlabel("Year")
    plt.ylabel("Sales of Products")
    plt.title("Sales of Prodcuts by Year")
    plt.legend(fontsize=8)
    plt.show()
#calling function
print(linechart())

