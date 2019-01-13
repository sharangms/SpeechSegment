import wave
import numpy as np
from scipy.io.wavfile import read

def ComputeEnergy(sub_wave_array, fpms):
    energies = []
    for i in range(0,len(sub_wave_array) - (5*fpms),(5*fpms)):
        energies.append(np.linalg.norm(sub_wave_array[i:(i+10)*fpms]))
    return energies



    

def SaveEnergy(large_wav_file, slice_index_file):
    slice_indices = np.loadtxt(slice_index_file)
    large_wav = wave.open(large_wav_file)
    width = large_wav.getsampwidth()
    rate = large_wav.getframerate()
    fpms = np.int32(rate / 1000) # frames per ms
    print('fpms', fpms)
    (samp,wave_array) = read(large_wav_file)
    print(wave_array)
    out_file = 'energy.npy'
    all_energies = []
    for i in range(800):
        start = np.int32((slice_indices[i] * 10 - 250) * fpms)
        all_energies.append(ComputeEnergy(wave_array[start:(start + 505 * fpms)], fpms))
    all_energies = np.array(all_energies)
    np.save(out_file,all_energies)


slices_path = 'indices.txt'
wav_path = 'wave_concat.wav'
SaveEnergy(wav_path, slices_path)

