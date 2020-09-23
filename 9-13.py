import random

##함수 선언 부분
def getNumber():
    return random.randrange(1,46)

#전역 변수 선언 부분
lotto=[]
num=0

#메인 코드 부분
print("**로또 추첨을 시작합니다.**\n");

while True : #(14~21) 무한 반복 > 뽑혔던 숫자가 다시 뽑힐수도 있어서
    num=getNumber()
    
    if lotto.count(num)==0: #리스트에 없어야 함수로 추가
        lotto.append(num)
        
    if len(lotto) >=6:
        break
    
print("추첨된 로또 번호 ==> ",end='')
lotto.sort()
for i in range(0,6):
    print("%d  " %lotto[i], end='')