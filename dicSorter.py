from operator import itemgetter

def dic_key_sort(dic, idx):
    return dict(sorted(dic.items(), key=itemgetter(idx), reverse=True))