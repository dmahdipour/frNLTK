import os
import platform
import glob
from tqdm import tqdm
import datetime
import pickle

import normalizer
import tokenizer
import tokenCounter
import stopwordRemover
import FolderDir_ExChk
import fileReader
import tf_idf_dicCreator
import vectorSimilarity



startTime = datetime.datetime.now()

if platform.system() == 'windows':    
    # Set dir path for windows OS       
    FolderDir_ExChk.windowsDirExistCreate('tf')
    FolderDir_ExChk.windowsDirExistCreate('tf_idf')
    FolderDir_ExChk.windowsDirExistCreate('tokenized')
    myTokenizedPath = "tokenized\\"
    myTF_IDF_path = "tf_idf\\"
    myTF_path = "tf\\"
    myCorpusPath = "irna_corpus\\"
else:    
    # Set dir path for mac OS
    FolderDir_ExChk.macDirExistCreate('tf')
    FolderDir_ExChk.macDirExistCreate('tf_idf')
    FolderDir_ExChk.macDirExistCreate('tokenized')
    myTokenizedPath = "tokenized/"
    myTF_IDF_path = "tf_idf/"
    myTF_path = "tf/"
    myCorpusPath = "irna_corpus/"
    

txtFileList = sorted(glob.glob(f'{myCorpusPath}*.txt'), key=os.path.basename)
corpusLen = len(txtFileList)
corpusLen = 5000

corpusContentJson = []
corpusTokens = {}
for corpusNum in tqdm(range(corpusLen)):
    fileContent = fileReader.my_Json_reader(txtFileList[corpusNum], "UTF-8", 'text')
    fileContent = normalizer.my_tiny_normalizing(fileContent)
    fileContent = stopwordRemover.remove_proNone(fileContent)
    fileContent = stopwordRemover.remove_regularWords(fileContent)
    fileContent = tokenizer.my_word_tokenize(fileContent)
    fileContent = tokenCounter.my_token_conter(fileContent)
    corpusContentJson.append(fileContent)
    
    corpusTokens = tokenCounter.my_DF_conter(corpusTokens, fileContent)



corpusTfJson = []
for rowKeys in tqdm(range(corpusLen)):
    corpusTfJson.append(tf_idf_dicCreator.my_TF(corpusTokens, dict(corpusContentJson[rowKeys])))

corpusTfIdfJson = []
for rowKeys in tqdm(range(corpusLen)):    
    corpusTfIdfJson.append(tf_idf_dicCreator.my_TF_IDF(corpusTfJson[rowKeys], list(corpusTokens.values())))
    


corpusSimilarity = [[] for i in range(corpusLen)]
for rowKeys in tqdm(range(corpusLen)):  
    similarityTf    = vectorSimilarity.cos_sim_vectors(corpusTfJson[0], corpusTfJson[rowKeys])
    similarityTfIdf = vectorSimilarity.cos_sim_vectors(corpusTfIdfJson[0], corpusTfIdfJson[rowKeys])
    corpusSimilarity[rowKeys].append(similarityTf)
    corpusSimilarity[rowKeys].append(similarityTfIdf)


endTime = datetime.datetime.now()
totalTime = endTime - startTime

print(" --- FINISHED in ",totalTime.total_seconds()," seconds --- ")


with open('corpusContentJson.pkl', 'wb') as f:
    pickle.dump([corpusContentJson],f)
with open('corpusTokens.pkl', 'wb') as f:
    pickle.dump([corpusTokens],f)    
with open('corpusTfJson.pkl', 'wb') as f:
    pickle.dump([corpusTfJson],f)
with open('corpusTfIdfJson.pkl', 'wb') as f:
    pickle.dump([corpusTfIdfJson],f)
with open('corpusSimilarity.pkl', 'wb') as f:
    pickle.dump([corpusSimilarity],f)