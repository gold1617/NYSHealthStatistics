import csv


def add(data,county,stat):
    for d in data:
        if d[0].lower() == county.lower():
            d.append(stat)

header = ('County','Heart Attack Hospitalization per 10000','Percentage of Obese Adults','Percentage of Adults who smoke','Percentage of Adults Binge Drinking','Hospitalization for Short-Term complications of Diabetes per 10000','Percentage of Obese Students','Unemployment Percentage')
data = []

inp = open('PA__Age-adjusted_Heart_Attack_Hospitalization_Rate_per_10_000_Map.csv')
out = open('Health_Metrics.csv','w')

try:

    reader = csv.reader(inp)
    writer = csv.writer(out,quoting=csv.QUOTE_NONNUMERIC)
    for i,line in enumerate(reader):
        if i != 0:
            data.append([line[6],line[9]])
    
    inp.close()

    inp = open('PA__Percentage_of_Adults_who_are_Obese_Map.csv');
    reader = csv.reader(inp)

    for i,line in enumerate(reader):
        if i != 0:
            add(data,line[6],line[9])
    
    inp.close()

    inp = open('PA__Percentage_of_Cigarette_Smoking_Among_Adults_Map.csv');
    reader = csv.reader(inp)

    for i,line in enumerate(reader):
        if i != 0:
            add(data,line[6],line[9])
    
    inp.close()

    inp = open('PA__Promote_Mental_Health_and_Prevention_Substance_Abuse_Indicators_by_County.csv');
    reader = csv.reader(inp)

    for i,line in enumerate(reader):
        if i != 0:
            add(data,line[0],line[10])
   
    inp.close()

    inp = open('PA__Rate_of_Hospitalizations_for_Short-term_Complications_of_Diabetes_per_10_000_-_Ages_18__Map.csv');
    reader = csv.reader(inp)

    for i,line in enumerate(reader):
        if i != 0:
            if(line[9]==''):
                line[9] = '-1'
            add(data,line[6],line[9])

    inp.close()

    inp = open('PA_Student_Weight_Status_Category_Reporting_Results__Beginning_2010.csv');
    reader = csv.reader(inp)

    for i,line in enumerate(reader):
        if i != 0:
            if(line[4]=='2010-2012' and line[11]=='DISTRICT TOTAL' and line[12]=='COUNTY'):
                add(data,line[1],line[8][:-1])

    for d in data:
        if(len(d) < 7):
            d.append('-1')

    inp.close()

    inp = open('Local_Area_Unemployment_Statistics__Beginning_1976.csv')
    reader = csv.reader(inp) 

    totals = {}
    for i,line in enumerate(reader):
        if i != 0:
           year = int(line[1])
           if year >= 2010 and  year <= 2012:
               if totals.has_key(line[0]):
                   totals[line[0]] = totals[line[0]] + float(line[6][:-1])
               else:
                   totals[line[0]] = float(line[6][:-1])

    for key in totals.keys():
        add(data,key.rsplit(' ',1)[0],totals[key]/36)

    writer.writerow(header)

    for d in data:
        writer.writerow((d[0],float(d[1]),float(d[2]),float(d[3]),float(d[4]),float(d[5]),float(d[6]),d[7]))
        
finally:
    inp.close()
    out.close()
