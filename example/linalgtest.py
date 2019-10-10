from scipy.sparse.linalg import svds
from scipy.sparse import csr_matrix

A = csr_matrix([[1, 0, 0], [5, 0, 2], [0, -1, 0], [0, 0, 3]], dtype=float)

u, s, vt = svds(A, k=2)

print('A:\n ', A.toarray(),'\n')
print('u:\n ', u, '\n')
print('s:\n ', s, '\n')
print('vt:\n ', vt, '\n')

