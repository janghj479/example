#클래스 선언 부분
class SuperClass:
    def method(self):
        pass
    
class SubClass1 (SuperClass):
    def method(self): #메서드 오버라이딩
        print('SubClass1에서 method()를 오버다이딩함')
        
class SubClass2 (SuperClass):
    def method(self): #반드시 오버라이딩 해야함 > 논리적인 오류 발생 가능
        raise NotImplementedError()
        
#메인 코드 부분
sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()