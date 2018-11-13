import os
import glob
from tqdm import tqdm

txtFileList = sorted(glob.glob('*.txt'), key=os.path.basename)
corpusLen = len(txtFileList)
for corpusNum in tqdm(range(corpusLen)):
    fileNM = txtFileList[corpusNum].split(".txt")
    if int(fileNM[0])<10:
        os.rename(txtFileList[corpusNum], "0000"+txtFileList[corpusNum]) 
    if int(fileNM[0])>9 and int(fileNM[0])<100:
        os.rename(txtFileList[corpusNum], "000"+txtFileList[corpusNum]) 
    if int(fileNM[0])>99 and int(fileNM[0])<1000:
        os.rename(txtFileList[corpusNum], "00"+txtFileList[corpusNum]) 
    if int(fileNM[0])>999 and int(fileNM[0])<10000:
        os.rename(txtFileList[corpusNum], "0"+txtFileList[corpusNum]) 