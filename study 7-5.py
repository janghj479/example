
##변수 선언 부분
animals = {"닭":"병아리", #딕셔너리에 키와 값넣기
         "개":"강아지",
         "곰":"능소니",
         "고등어":"고도리",
         "명태":"노가리",
         "말":"망아지",
         "호랑이":"개호주"};

#메인 코드 부분
while(True):
    myanimal=input(str(list(animals.keys()))+" 중 새끼 이름을 알고 싶은 동물은?")#입력받기
    if myanimal in animals :
        print("<%s>의 새끼는 <%s>입니다." %(myanimal, animals.get(myanimal)))
    elif myanimal == "끝" : # 끝내기
        break
    else:
        print("리스트에 없습니다. 확인해 보세요.") #리스트에 없는메뉴 확인