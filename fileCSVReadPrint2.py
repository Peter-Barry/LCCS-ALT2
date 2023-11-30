#fh = open("3rdYr.csv","w")
#fh.write("PJBarry!")
#fh.write("Lucan!")
#fh.close()
"""
fh = open("myfile2.csv","r")
line = fh.readline()
dataIN = fh.read()
fh.close()
print(line, "line")
print(dataIN, "dataIN")

fh = open("myfile.csv","a")
fh.write("Tina, 27, Boston")
fh.close()
print("closed")
"""
fh = open("myfile2.csv","r")
line = fh.readline()
fields = line.strip().split(',')  # Split line into fields
field0 = fields[0]  # Access the first field (index 0)
field1 = fields[1]  # Access the second field (index 1)
field2 = fields[2]  # Access the first field (index 0)

print(line, "readline","field0 ",field0,"field1 ",field1, "field2",field2)
line = fh.readline()
line = fh.readline()
print(line, "readline")
print(line, "readline","field0 ",field0,"field1 ",field1, "field2",field2)
line = fh.readline()
print(line, "readline")
print(line, "readline","field0 ",field0,"field1 ",field1, "field2",field2)

line = fh.readline()
print(line, "readline")
line = fh.readline()
print(line, "readline")
ine = fh.readline()
print(line, "readline")


dataIN = fh.read()
print("dataIN",dataIN)

fh.close()


# print(dataIN, "read")

"""
fh = open("names.csv","r")
dataIN = fh.read()

fh.close()
print(dataIN)

fh = open("names.txt","r")
dataIN = fh.read()
fh.close()
print("txt",dataIN)
#a = Add
#w = write
#r = Read only
"""