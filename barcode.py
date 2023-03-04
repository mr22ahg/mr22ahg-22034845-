#importing libraries
import matplotlib.pyplot as plt
import pandas as pd
#defining function
def barchart():
#loading CSV file
    cd=pd.read_csv("oil_production.csv")
#plotting bar graph
    plt.barh(cd["Country"],cd["Oil production2019 (bbl/day)"],
         label="Oil production2019 (bbl/day)",color="blue")
#plotting labels
    plt.xlabel("Barrels per day",fontsize=12)
    plt.ylabel("Country",fontsize=12)
    plt.legend()
    plt.title("Oil Production",fontsize=12)
    plt.show()
#calling the function   
print(barchart())
