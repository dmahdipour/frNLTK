import normalizer
import tokenizer
import tokenCounter
import dicSorter
#import stopwordRemover


def n_t_c_s(fileContent):
    fileContent = normalizer.my_normalizing(fileContent)
    #fileContent = stopwordRemover.remove_proNone(fileContent)
    #fileContent = stopwordRemover.remove_regularWords(fileContent)
    fileContent = tokenizer.my_word_tokenize(fileContent)
    fileContent = tokenCounter.my_token_conter(fileContent)
    fileContent = dicSorter.dic_key_sort(fileContent, 0)
    return fileContent