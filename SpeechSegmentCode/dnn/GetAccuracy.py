import numpy as np
act = np.load('actual_indices.npy')
est = np.load('loc.npy')
act = act[:130]

print(act, est)
