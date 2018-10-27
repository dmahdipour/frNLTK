import glob
from tqdm import tqdm

import normalizer


myCorpusPath = "ahrarnews_corpus/"


txtFileList = glob.glob(f'{myCorpusPath}*.txt')

# all_in_1
filesContent = ""
for filesNum in tqdm(range(len(txtFileList))):
    filesContent = filesContent + fileReader.my_file_reader(txtFileList[filesNum], "UTF-8") + "\n"  

filesWordNormalize = normalizer.my_normalizing(filesContent)