def my_TF_IDF(mainDic, axDic):
    tmpDic = {}
    for i in mainDic:    
        if i in axDic:
            tmpDic[i] = axDic.get(i)/mainDic.get(i)
        else:
            tmpDic[i] = 0
    return tmpDic


def my_TF(mainDic, axDic):
    tmpDic = {}
    for i in mainDic:    
        if i in axDic:
            tmpDic[i] = axDic.get(i)
        else:
            tmpDic[i] = 0
    return tmpDic