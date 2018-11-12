from tqdm import tqdm


def my_token_conter(tokens):
    dic = {}
    for wordTkn in tqdm(tokens):
        if wordTkn in dic:
            tknCount = dic.get(wordTkn)
            dic.update({wordTkn:tknCount+1})
        else:
            dic[wordTkn] = 1
    return dic




def myAll_token_conter(dic, tokens):
    for wordTkn in tqdm(tokens):
        tknTokensCount = tokens.get(wordTkn)
        if wordTkn in dic:
            tknDicCount = dic.get(wordTkn)
            dic.update({wordTkn:tknDicCount+tknTokensCount})
        else:
            dic[wordTkn] = tknTokensCount
    return dic