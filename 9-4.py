##함수 선언 부분
def plus(v1, v2): #def 함수 부분은 바로 실행X
    result = 0
    result = v1+v2
    return result

#전연 변수 선언 부분
hap = 0

#메인 코드 부분
hap=plus(100,200)
print("100과 200의 plus() 함수 결과는 %d" %hap)