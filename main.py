import platform
import glob
from tqdm import tqdm
import numpy as np

import FolderDir_ExChk
import fileWriter
import fileReader
import tf_idf_dicCreator
import vectorSimilarity
import NTCS


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
    

txtFileList = glob.glob(f'{myCorpusPath}*.txt')

### corpus vocab creator
corpusContent = ""
for corpusNum in tqdm(range(len(txtFileList))):
    corpusContent = corpusContent + fileReader.my_file_reader(txtFileList[corpusNum], "UTF-8") + "\n"         

corpusVocabC = NTCS.n_t_c_s(corpusContent)
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
  
myDF = tf_idf_dicCreator.my_DF(documrntsMatrix)
file_tf_idf = tf_idf_dicCreator.my_TF_IDF(documrntsMatrix, myDF)


for fileNum in tqdm(range(len(txtFileList))):  
    row_tf_idf =file_tf_idf[fileNum,:]
    
    fileName = txtFileList[fileNum].split(myCorpusPath)
    fileName = fileName[1].split(".txt")
    fileWriter.my_file_line_writer(myTF_IDF_path+fileName[0]+".TfIdf", row_tf_idf)
 
for fileNum in range(len(txtFileList)):
    doc1 = "01"
    #doc2 = "10"  
    
    fileName = txtFileList[fileNum].split(myCorpusPath)
    fileName = fileName[1].split(".txt")
    
    vecSim = vectorSimilarity.cos_sim_vectors(myTF_path+doc1+".TF", myTF_path+fileName[0]+".TF")
    print("similarity Doc01 and Doc"+fileName[0]+" By Just TF is: ",vecSim)
    
    vecSim = vectorSimilarity.cos_sim2_vectors(myTF_IDF_path+doc1+".TfIdf", myTF_IDF_path+fileName[0]+".TfIdf")
    print("similarity Doc01 and Doc"+fileName[0]+" By TF_IDF is: ",vecSim)
    print("=================================")
    