import numpy as np
import csv

children = []

childrencsv = open("Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv")

reader = csv.reader(childrencsv)

for line in reader:
    if(line[1]!= 'N/A' and line[4] == '2010-2012' and line[11] == 'DISTRICT TOTAL' and line[12] == 'COUNTY'):
        children.append([line[1],line[8]])

print(children)
print(len(children))
