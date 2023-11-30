import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))

filename = "pythonfilein.txt"
print(filename)
# open(filename, "x")
fh = open(filename,"r+")
fh.write('This is a test1\n')
fh.write('This is a test2\n')
fh.write('This is a test3\n')

fh.close()
print("here")
fh = open(filename,"r+")
for x in fh:
  print(x, "data")
  
print("here2")
fh.read(1)
print(fh.read(1),"Data?")
print(fh.readline(1),"data2")
print("here3")
print(fh.readline(2))
fh.read(2)


#fh.write("\nnew content!")
#fh.close()
#/Users/PeterBarry/Desktop