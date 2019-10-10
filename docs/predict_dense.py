from scipy.sparse.linalg import * #used for matrix multiplication

def computeEstimatedRatings(urm, U, S, Vt, uTest, moviesSeen, K, test):
	rightTerm = S*Vt 

	estimatedRatings = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float16)
	for userTest in uTest:
		prod = U[userTest, :]*rightTerm

		#we convert the vector to dense format in order to get the indices of the movies with the best estimated ratings 
		estimatedRatings[userTest, :] = prod.todense()
		recom = (-estimatedRatings[userTest, :]).argsort()[:250]
		for r in recom:
			if r not in moviesSeen[userTest]:
				uTest[userTest].append(r)

				if len(uTest[userTest]) == 5:
					break

	return uTest
