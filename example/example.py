import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import *
import math as mt
import csv
from sparsesvd import sparsesvd

#constants defining the dimensions of our User Rating Matrix (URM)
MAX_PID = 37143
MAX_UID = 15375

def readUrm():
	urm = np.zeros(shape=(MAX_UID,MAX_PID), dtype=np.float32)
	with open('/PathToTrainFile.csv', 'rb') as trainFile:
		urmReader = csv.reader(trainFile, delimiter=',')
		for row in urmReader:
			urm[int(row[0]), int(row[1])] = float(row[2])

	return csr_matrix(urm, dtype=np.float32)


def computeSVD(urm, K):
	U, s, Vt = sparsesvd(urm, K)

	dim = (len(s), len(s))
	S = np.zeros(dim, dtype=np.float32)
	for i in range(0, len(s)):
		S[i,i] = mt.sqrt(s[i])

	U = csr_matrix(np.transpose(U), dtype=np.float32)
	S = csr_matrix(S, dtype=np.float32)
	Vt = csr_matrix(Vt, dtype=np.float32)

	return U, S, Vt




def main():
	K = 90
	urm = readUrm()
	U, S, Vt = computeSVD(urm, K)
	uTest = readUsersTest()
	moviesSeen = getMoviesSeen()
	uTest = computeEstimatedRatings(urm, U, S, Vt, uTest, moviesSeen, K, True)
