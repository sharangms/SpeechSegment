import numpy as np 
def MakeTargets(actual, estimated):
	actual = np.round(actual)
	print(len(actual), len(estimated))
	targets = []
	for i in range(len(estimated)):
		if abs(actual[i] - estimated[i]) > 50:
			targets.append(np.ones(100)*np.nan)
		else:
			lower = estimated[i] - 50
			print('lower',lower)
			cur_target = np.int32([ind == (actual[i] - lower) for ind in range(100)])
			print(cur_target)
			targets.append(cur_target)
			print('targets', targets)
	return np.array(targets)

act = np.load('actual_indices.npy')
est = np.load('loc.npy')
np.save('targets.npy', MakeTargets(act,est))

