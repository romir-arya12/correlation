import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    cupsOfCoffee=[]
    hoursOfSleep=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            hoursOfSleep.append(float(row["sleep in hours"]))
            cupsOfCoffee.append(float(row["Coffee in ml"]))
    return {"x":hoursOfSleep,"y":cupsOfCoffee}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between hours of sleep of cups of coffee is: ",correlation[0,1])
def setup():
    data_path="./cups of coffee vs hours of sleep.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()