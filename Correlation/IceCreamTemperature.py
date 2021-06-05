import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    iceCreamSales=[]
    temperature=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            iceCreamSales.append(float(row["Ice-cream Sales"]))
    return {"x":temperature,"y":iceCreamSales}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between temperature of ice-cream sales is: ",correlation[0,1])
def setup():
    data_path="./Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()