#i = 0
#while i < 11111 :
#  print(i)
#  i = i+1
#print('끝!')










a= ['사과','딸기','배','두리안','귤']
for i in a:
  if i == '배' :
    continue
  print(i)

a= ['사과','딸기','배','두리안','귤']
for index, value in enumerate(a):
  if value =='배':
    a[index] = 0
print(a)


for i in range(2,10,1) :
  print(i,'단')
  for j in range(1,10,1) :
    print(i,'*',j,'=',i*j)




a = [[1,2],[3,4],[5,6]]
for value1 in a:
  print(value1)
  for value2 in value1 :
    print(value2)





