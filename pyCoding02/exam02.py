

kor=float(input('국어 점수 입력:'))
math=float(input('수학 점수 입력:'))
info=float(input('정보 점수 입력:'))
sum=float(kor+math+info)
avg=int(sum)/3

print('총합:',sum)
print('평균:',avg)

if avg >= 90:
  print('등급:A')
elif avg >=80:
  print('등급:B')
else :
  print('등급:C')