from scipy.sparse.linalg import svds
from scipy.sparse import csr_matrix

def decomp(A):
    """
    :param A: URM to be factored
    
    :return u: lhs
    :return s: singular values
    :return vt: rhs
    """
    
    return svds(A, k=2)