import csv

# csvfile = open("myfile.csv", "x")

filename = 'myfile.csv'
csvfile = open(filename,"r+")

print("File opened")

csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Name', 'Age', 'City'])
print("Columns Created")


csvwriter.writerow(['Peter', 25, 'New York'])
print("Data Created")

csvfile.close()
print("closed")
