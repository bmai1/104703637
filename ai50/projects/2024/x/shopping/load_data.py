import csv

month = {
    'Jan': 0,
    'Feb': 1,
    'Mar': 2,
    'Apr': 3,
    'May': 4,
    'Jun': 5,
    'Jul': 6,
    'Aug': 7,
    'Sep': 8,
    'Oct': 9,
    'Nov': 10,
    'Dec': 11,
}

evidence = []
labels = []
with open('small.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        row = []
        row.append(int(line[0])) # Administrative
        row.append(float(line[1])) # Administrative_Duration
        row.append(int(line[2])) # Informational
        row.append(float(line[3])) # Informational_Duration
        row.append(int(line[4])) # ProductRelated

        for i in range(5, 10):
            row.append(float(line[i])) # ProductRelated_Duration, BounceRates, ExitRates, PageValues, SpecialDay
        row.append(month[line[10]]) # Month
        for i in range(11, 15):
            row.append(int(line[i])) # OperatingSystems, Browser, Region, TrafficType
        
        row.append(1 if line[15] == "Returning_Visitor" else 0) # VisitorType
        row.append(1 if line[16] == "TRUE" else 0) # Weekend
        labels.append(1 if line[17] == "TRUE" else 0)

        evidence.append(row)

print(evidence)
print(labels)