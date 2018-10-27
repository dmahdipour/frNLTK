import glob
from tqdm import tqdm

import normalizer
import tokenizer
import tokenCounter
import dicSorter
import fileWriter
import fileReader
import tf_idf_dicCreator


myCorpusPath = "ahrarnews_corpus/"
myTokenizedPath = "tokenized/"
myTF_IDF_path = "tf_idf/"
myTF_path = "tf/"


txtFileList = glob.glob(f'{myCorpusPath}*.txt')

# all_in_1
filesContent = ""
for filesNum in tqdm(range(len(txtFileList))):
    filesContent = filesContent + fileReader.my_file_reader(txtFileList[filesNum], "UTF-8") + "\n"  

filesWordNormalize = normalizer.my_normalizing(filesContent)
filesWordTokenize = tokenizer.my_word_tokenize(filesWordNormalize)
filesTokenCount = tokenCounter.my_token_conter(filesWordTokenize)
filesSorted_dic = dicSorter.dic_key_sort(filesTokenCount, 0)
fileWriter.my_file_writer(myTokenizedPath+"0_myIndexList.tok", filesSorted_dic)

# one_By_One
for fileNum in tqdm(range(len(txtFileList))):    
    fileContent = fileReader.my_file_reader(txtFileList[fileNum], "UTF-8")
    
    wordNormalize = normalizer.my_normalizing(fileContent)
    wordTokenize = tokenizer.my_word_tokenize(wordNormalize)
    tokenCount = tokenCounter.my_token_conter(wordTokenize)    
    sorted_dic = dicSorter.dic_key_sort(tokenCount, 0)
   
    fileName = txtFileList[fileNum].split(myCorpusPath)
    fileName = fileName[1].split(".txt")

    file_tf_idf = tf_idf_dicCreator.my_TF_IDF(filesTokenCount, sorted_dic)
    file_tf = tf_idf_dicCreator.my_TF(filesTokenCount, sorted_dic)
    
    fileWriter.my_file_writer(myTokenizedPath+fileName[0]+".tok", sorted_dic)
