import fileReader
from numpy import dot
from numpy.linalg import norm

def cos_sim_vectors(doc1, doc2):
    d1 = eval(fileReader.my_file_reader(doc1, "UTF-8"))
    ls_d1 = list(d1.values())    
    d2 = eval(fileReader.my_file_reader(doc2, "UTF-8"))
    ls_d2 = list(d2.values())
    
    return dot(ls_d1, ls_d2)/(norm(ls_d1)*norm(ls_d2))


def cos_sim2_vectors(doc1, doc2):
    ls_d1 = fileReader.my_floatFile_reader(doc1)
    ls_d2 = fileReader.my_floatFile_reader(doc2)
    
    return dot(ls_d1, ls_d2)/(norm(ls_d1)*norm(ls_d2))