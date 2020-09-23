#전역 변수 선언 부분
coffee=0

#함수 선언 부분
def coffee_machine(button): #coffee_machine(입력값) > button에 입력값을 넘김
    print()
    print("#1.(자동으로) 뜨거운 물을 준비한다.");
    print("#2.(자동으로) 종이컵을 준비한다.");
    
    if button==1 :
        print("#3.(자동으로) 보통커피를 탄다.");
    elif button==2 :
        print("#3.(자동으로) 설탕커피를 탄다.");
    elif button==3 :
        print("#3.(자동으로) 블랙커피를 탄다.");
    else :
        print("#3.(자동으로) 아무거나 탄다.\n");
        
    print("#4.(자동으로) 물을 붓는다.");
    print("#5.(자동으로) 스푼으로 젓는다.");
    print()

#메인 코드 부분
coffee=int(input("A손님, 어떤 커피 드릴까요?(1.아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소)"))
coffee_machine(coffee) #coffee_machine(입력값)
print("A손님~ 커피 여기 있습니다.");

coffee=int(input("B손님, 어떤 커피 드릴까요?(1.아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소)"))
coffee_machine(coffee) #coffee_machine(입력값)
print("B손님~ 커피 여기 있습니다.");

coffee=int(input("C손님, 어떤 커피 드릴까요?(1.아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소)"))
coffee_machine(coffee) #coffee_machine(입력값)
print("C손님~ 커피 여기 있습니다.");

coffee=int(input("D님, 어떤 커피 드릴까요?(1.아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소)"))
coffee_machine(coffee) #coffee_machine(입력값)
print("C손님~ 커피 여기 있습니다.");

#button만 누르면(함수만 호출하면) 커피 세잔이 자동으로 나옴