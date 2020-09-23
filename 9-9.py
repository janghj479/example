#함수 선언 부분
def multi(v1,v2):
    retList = []
    res1=v1+v2
    res2=v1-v2
    retList.append(res1) #(6~8) >> return res1, res2
    retList.append(res2)
    return retList

#전역 변수 선언 부분
myList=[]
hap,sub=0,0

#메인 코드 부분
myList=multi(100,200)  #>hap,sub=multi(100,200) (15~17) >> myList 필요X
hap=myList[0]
sub=myList[1]
print("multi()에서 돌려준 값==>%d, %d"%(hap,sub))