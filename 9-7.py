#함수 선언 부분
def func1():
    global a # 이안에서 a는 전역 변수
    a=10 #전역변수 값을 10으로 변경
    print("func1()에서 a값 %d" %a)

def func2():
    print("func2()에서 a값 %d" %a)
    
#함수 변수 선언 부분
a=20 #전역변수

#메인 코드
func1()
func2()