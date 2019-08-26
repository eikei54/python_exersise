
#input_str=input()
#dimensions=[]
#for x in input_str.split(','):
#    dimensions.append(int(x))
#print(dimensions)


input_str2=input()
dim=[int(x) for x in input_str2.split(',')]
print(dim)

tempList=[[0 for col in range(dim[1])] for row in range(dim[0])]

print(tempList)
print(dim[0],dim[1])

for row in range(dim[0]):
    print("row:", row)
    for col in range(dim[1]):
        print("col", col)
        tempList[row][col] = row*col
#multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#multilist = [0 for col in range()]


#for row in range(4):
#    print("row:", row)
#    for col in range(5):
#        print("col", col)
#        tempList[row][col] = row*col

print(tempList)
