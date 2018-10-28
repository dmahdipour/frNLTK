import numpy as np


def my_TF(mainDic, axDic):
    tmpDic = {}
    for i in mainDic:    
        if i in axDic:
            tmpDic[i] = axDic.get(i)
        else:
            tmpDic[i] = 0
    return tmpDic

def my_DF(mainDic):
    [row, col] = (mainDic.shape)
    df = np.zeros(col).astype(int)    
    for i in range(col):
        for j in range(1, row):
            if int(mainDic[j, i]) > 0:
                df[i] = df[i]+1
    return df 


def my_TF_IDF(mainDic, axDic):
    mainDic = np.array(mainDic).astype(float)
    [row, col] = (mainDic.shape)
    for i in range(row):
        mainDic[i,:] = mainDic[i,:]/axDic
    
    return mainDic[1:row,:]
