import normalizer
import tokenizer
import tokenCounter
import dicSorter


def n_t_c_s(fileContent):
    wordNormalize = normalizer.my_normalizing(fileContent)
    wordTokenize = tokenizer.my_word_tokenize(wordNormalize)
    tokenCount = tokenCounter.my_token_conter(wordTokenize)
    sorted_dic = dicSorter.dic_key_sort(tokenCount, 0)
    return sorted_dic