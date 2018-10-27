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