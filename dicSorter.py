import operator
from operator import itemgetter
from collections import OrderedDict

def dic_key_sort(dic, idx):
    return dict(OrderedDict(sorted(dic.items(), key=itemgetter(idx))))