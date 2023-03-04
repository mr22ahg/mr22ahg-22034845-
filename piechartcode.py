#importing libraries
import matplotlib.pyplot as plt
import pandas as pd 
#defining function
def piechart():
#loading CSV file
    cd=pd.read_csv("2003_2017_waste.csv")
#setting size of figure
    plt.figure(figsize=(30,15))
#fontsize of text
    textprops={"fontsize":15}
#plotting piechart
    plt.pie(cd["waste_disposed_of_tonne"],labels=cd["wastetype"].astype(str),
            autopct="%.2f%%",shadow=True,radius=0.9,textprops=textprops)      
    plt.legend(fontsize=13)
    plt.title("Singapore Waste Management",fontsize=30)
    plt.show()
#calling the function
print(piechart())