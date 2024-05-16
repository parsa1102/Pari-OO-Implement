from pariMatrix import Matrix
import numpy as np

def __main__() :
    mt = [
        [1, 0, 1, 2, 10],
        [2, 0, 2 ,10 ,2],
        [1, 0, 1, 2, 1]
    ]                
    
    mat = Matrix(mt, 3, 5)
    
    print(np.array(mat.fromTopLeftToDownRight()).reshape(3, 5))
    
    
__main__()