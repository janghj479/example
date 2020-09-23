import operator

trainDic, trainList = {},[]

traninDic = {'Thomas' : '토마스', 'Edward' : '에드워드', 'Henry': '헨리' }
traintList = sorted(trainDic.items(), key=operator.itemgetter(0))

print(trainList)

#출력결과 > [('Edward','에드워드'),()~]