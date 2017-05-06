import csv
from matplotlib import pyplot
import numpy

f = open("Health_Metrics.csv")
x = []
y = []
counties = []
labels = []
try:
    reader = csv.reader(f)

    for i,line in enumerate(reader):
        if(i > 0 and line[6] != '-1.0' and line[2] != '-1.0'):
            counties.append(line[0])
            x.append(float(line[2]))
            y.append(float(line[6]))
        elif i == 0:
            labels.append(line[2])
            labels.append(line[6])
    
    fig,ax = pyplot.subplots()
    ax.scatter(x,y)

    for i,txt in enumerate(counties):
        ax.annotate(txt, (x[i],y[i]))
    
    pyplot.xlabel(labels[0])
    pyplot.ylabel(labels[1])

    print numpy.corrcoef(x,y)
    
    pyplot.show()
    

finally:
    f.close()


