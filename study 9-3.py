#함수 선언 부분
def para_func(*para): #매개변수가 없으면 0을 기본값으로 사용
    #튜플 사용해서 해결
    result=0
    for num in para:
        result = result + num
    return result

#전역 변수 선언 부분
hap=0

#메인 코드 부분
hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==>%d" %hap)
hap=para_func(10,20,30,40,50,60,70,80,90,100)
print("매개변수가 10개인 함수를 호출한 결과==>%d" %hap)