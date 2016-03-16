import csv
import numpy as np
import matplotlib.pyplot as plt

# Open NationalNames.csv file; read data; Ask user for input name and gender
with open('NationalNames.csv', 'rb') as f:
    reader = csv.reader(f)
    name= raw_input('Enter name : ')
    gender = raw_input('Enter gender (M/F):' )
    fout = open ('outputbaby.csv','wb')
    mywriter =csv.writer(fout)
    for row in reader:
        if row[1]==name:
            if row[3]==gender:
                year = row[2]
                count = row[4]
                mywriter.writerow(row)
        else:
            continue
    fout.close()
# Draw graph for the outputbaby file (Year vs Count)

with open('outputbaby.csv','rb') as f1:
    reader = csv.reader(f1)
    x_total = []
    y_total = []
    for row in reader:
        x_numbers= [row[2]]
        x_total = x_total+x_numbers
        y_numbers = [row[4]]
        y_total= y_total+y_numbers

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Year vs Count")
ax1.set_xlabel('Year')
ax1.set_ylabel('Count')

ax1.plot(x_total,y_total, c='r', label='Counts')

leg = ax1.legend()

plt.show()
