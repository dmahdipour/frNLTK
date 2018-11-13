def my_TF(mainDic, axDic):
    tmpDic = []
    for i in mainDic:    
        if i in axDic:
            tmpDic.append(axDic.get(i))
        else:
            tmpDic.append(0)
            
    return tmpDic


def my_TF_IDF(mainDic, axDic):
    tmpDic = []
    for i in range(len(mainDic)):
        tmpDic.append(mainDic[i]/axDic[i])
    
    return tmpDic
