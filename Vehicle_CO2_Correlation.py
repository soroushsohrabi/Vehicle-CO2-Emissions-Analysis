import csv


Enginsize, Cylinders, FUELCONSUMPTION_COMB_MPG, CO2EMISSIONS=[], [], [] , []

with open("FuelConsumption.csv","rt") as f1:
    reader = csv.reader(f1)
    next(reader)
    for row in reader:
        Enginsize.append(float(row[4]))
        Cylinders.append(float(row[5]))
        FUELCONSUMPTION_COMB_MPG.append(float(row[11]))
        CO2EMISSIONS.append(float(row[12]))

def avg(ms):
    return sum(ms)/len(ms)
def variance(ms):
    return sum((m-avg(ms))**2 for m in ms)/len(ms)
def std(ms):
    return variance(ms)**0.5
def cov(ms,ns):
    l=0
    for i in range(len(ms)):
        l+= (ms[i]-avg(ms))*(ns[i]-avg(ns))
    return l/len(ms)
def corr(ms,ns):
    sm,sn=std(ms),std(ns)
    return cov(ms,ns)/(sm*sn)

print(f"Correlation between Engine Size and CO2 Emissions::{corr(Enginsize,CO2EMISSIONS):.3f}\nCorrelation between Cylinders and CO2 Emissions::{corr(Cylinders,CO2EMISSIONS):.3f}\nCorrelation between FUELCONSUMPTION_COMB_MPG and CO2EMISSIONS:{corr(FUELCONSUMPTION_COMB_MPG,CO2EMISSIONS):.3f}")

def linear_regression(x,y):
    a=cov(x,y)/variance(x)
    b=avg(y)-(a*avg(x))
    return f"y={a:.2f}x+{b:.2f}"

print(f"Linear Regression Enginsize and CO2EMISSIONS{linear_regression(Enginsize,CO2EMISSIONS)}\nLinear Regression Cylinders and CO2EMISSIONS{linear_regression(Cylinders,CO2EMISSIONS)}\nLinear Regression FUELCONSUMPTION_COMB_MPG and CO2EMISSIONS{linear_regression(FUELCONSUMPTION_COMB_MPG,CO2EMISSIONS)}")