import numpy as np 

forw = np.load('forward.npy')
energy = np.load('energy.npy')
targets = np.load('targets.npy')
print(len(forw), len(energy), len(targets))

dataset = []
final_targets = []
for i in range(len(forw)):
	cur_energy = energy[i]
	cur_forw = forw[i].flatten()
	cur_target = targets[i].flatten()
	if np.isnan(cur_target[0]) or np.isnan(cur_forw[0]) or np.isnan(cur_energy[0][0]):
		continue
	else:
		dataset.append(np.column_stack([cur_energy, cur_forw]))
		final_targets.append(cur_target)

A = np.array(dataset)
np.save('final_train', A)
B = np.array(final_targets)
np.save('final_targets', B)



