# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx--xxxx, and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the second year can be anterior to the first year.
# - The month is a two digit number.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly.csv'
if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(filename))
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
range_for_the_years = input('Enter a range for the years in the form XXXX--XXXX: ')
month = input('Enter a month in the form of a 2-digit number: ')
average = 0
years_above_average = []


l = []
m = []
n = []
years=[]
years1= []

for line in range_for_the_years.split('--'):
    years.append(int(line))
for d in years:
    years1.append(d)
if years1[0]<= years1[1]:        
    year1 = years1[0]
    year2 = years1[1]
else:
    year1 = years1[1]
    year2 = years1[0]
month = int(month)
correct_year = []
avg = []
with open(filename) as csvfile:
    
    reader = csv.reader(csvfile)
    for line in reader:
        l.append(line)
    for i in range(1,len(l)):
        int_line = []
        for line in l[i][1].split('-'):
            int_line.append(int(line))
        m.append(int_line)
    for i1 in range(1,len(l)):
        n.append(float(l[i1][2]))
    for i2 in range(len(l)):
        if (l[i2][0] == source) and ((m[i2-1][0]>=year1)and(m[i2-1][0]<=year2))and(m[i2-1][1]==month):
            correct_year.append([m[i2-1][0],n[i2-1]])
            avg.append(n[i2-1])
            #print('t')
    average = sum(avg)/len(avg)
    for i3 in range(len(correct_year)):
        if correct_year[i3][1] >= average:
            years_above_average.append(correct_year[i3][0])
            #print('y')
            
    years_above_average.reverse()

            



print('The average anomaly for this month of those years is: {:.2f}.'.format(average))
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
