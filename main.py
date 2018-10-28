import glob
from tqdm import tqdm
import numpy as np

import fileWriter
import fileReader
import tf_idf_dicCreator
import vectorSimilarity
import NTCS


myCorpusPath = "ahrarnews_corpus/"
myTokenizedPath = "tokenized/"
myTF_IDF_path = "tf_idf/"
myTF_path = "tf/"


txtFileList = glob.glob(f'{myCorpusPath}*.txt')

### corpus vocab creator
corpusContent = ""
for corpusNum in tqdm(range(len(txtFileList))):
    corpusContent = corpusContent + fileReader.my_file_reader(txtFileList[corpusNum], "UTF-8") + "\n" 

documrntsMatrix = list(corpusVocabC.values())
fileWriter.my_file_writer(myTokenizedPath+"0_corpusVocabC.voc", corpusVocabC)

### tf creator
for fileNum in tqdm(range(len(txtFileList))):    
    fileContent = fileReader.my_file_reader(txtFileList[fileNum], "UTF-8")

    sorted_dic = NTCS.n_t_c_s(fileContent)
    
    fileName = txtFileList[fileNum].split(myCorpusPath)
    fileName = fileName[1].split(".txt")
    
    fileWriter.my_file_writer(myTokenizedPath+fileName[0]+".tok", sorted_dic)

    file_tf = tf_idf_dicCreator.my_TF(corpusVocabC, sorted_dic)
    documrntsMatrix = np.vstack((documrntsMatrix, list(file_tf.values())))
    fileWriter.my_file_writer(myTF_path+fileName[0]+".TF", file_tf)

vecSim = vectorSimilarity.cos_sim_vectors(myTF_path+"01"+".TF", myTF_path+"02"+".TF")
print(vecSim)

vecSim = vectorSimilarity.cos_sim_vectors(myTF_IDF_path+"01"+".TfIdf", myTF_IDF_path+"02"+".TfIdf")
print(vecSim)