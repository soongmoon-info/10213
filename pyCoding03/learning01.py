#리스트
#tempList = ['안녕',10,20,30,40]
#print(tempList[1:4])
#tempList2 = [[1,2,3],[4,5,6],7]
#print(          )

tempList = [10,20,30,40]
tempList[1] = 2
print(tempList)
#추가
tempList.append(50)
print(tempList)
tempList.insert(2,25)
print(tempList)
#삭제
tempList.remove(50)
print(tempList)
del(tempList[2])
print(tempList)

