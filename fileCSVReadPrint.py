
"""
import csv

with open('myfile.csv', 'r') as filename:
    csv_reader = csv.reader(filename)
    for row in csv_reader:
        print(row)
filename.close()
print("closed")




"""
import csv
filename = 'myfile.csv'
csvfile = open(filename,"r+")

print("File opened")
with open('myfile.csv', 'r') as filename:
    csv_reader = csv.reader(filename)
    for row in csv_reader:
        print(row[0],row[2])


csvfile.close()
print("closed")
