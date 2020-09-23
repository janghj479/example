# ** -> 튜플이 아닌 딕셔너리 형식으로 전

def dic_func(**para):
    for k in para.keys():
        print("%s --> %d명입니다." %(k,para[k]))
dic_func(샤이니=5, 레드벨벳=5, EXO=7)