import glob
from tqdm import tqdm

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

# all_in_1
filesContent = ""
for filesNum in tqdm(range(len(txtFileList))):
    filesContent = filesContent + fileReader.my_file_reader(txtFileList[filesNum], "UTF-8") + "\n"  

corpusVocabC = NTCS.n_t_c_s(corpusContent)
fileWriter.my_file_writer(myTokenizedPath+"0_myIndexList.tok", filesSorted_dic)

# one_By_One
for fileNum in tqdm(range(len(txtFileList))):    
    fileContent = fileReader.my_file_reader(txtFileList[fileNum], "UTF-8")
    
    sorted_dic = NTCS.n_t_c_s(fileContent)
   
    fileName = txtFileList[fileNum].split(myCorpusPath)
    fileName = fileName[1].split(".txt")

    file_tf_idf = tf_idf_dicCreator.my_TF_IDF(filesTokenCount, sorted_dic)
    file_tf = tf_idf_dicCreator.my_TF(filesTokenCount, sorted_dic)

    fileWriter.my_file_writer(myTokenizedPath+fileName[0]+".tok", sorted_dic)
    fileWriter.my_file_writer(myTF_path+fileName[0]+".TF", file_tf)
    fileWriter.my_file_writer(myTF_IDF_path+fileName[0]+".TfIdf", file_tf_idf)

vecSim = vectorSimilarity.cos_sim_vectors(myTF_path+"01"+".TF", myTF_path+"02"+".TF")
print(vecSim)

vecSim = vectorSimilarity.cos_sim_vectors(myTF_IDF_path+"01"+".TfIdf", myTF_IDF_path+"02"+".TfIdf")
print(vecSim)