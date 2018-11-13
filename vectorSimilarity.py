import fileReader
from numpy import dot
from numpy.linalg import norm

def cos_sim_vectors(vec1, vec2):    
    return dot(vec1, vec2)/(norm(vec1)*norm(vec2))


def cos_sim2_vectors(doc1, doc2):
    ls_d1 = fileReader.my_floatFile_reader(doc1)
    ls_d2 = fileReader.my_floatFile_reader(doc2)
    
    return dot(ls_d1, ls_d2)/(norm(ls_d1)*norm(ls_d2))