import wave
import numpy as np

def index_slice(infile, outfilename, start_ms, end_ms):
    width = infile.getsampwidth()
    rate = infile.getframerate()
    fpms = rate / 1000 # frames per ms
    length = np.int32((end_ms - start_ms) * fpms)
    start_index = np.int32(start_ms * fpms)

    out = wave.open(outfilename, "w")
    out.setparams((infile.getnchannels(), width, rate, length, infile.getcomptype(), infile.getcompname()))
    
    infile.rewind()
    anchor = infile.tell()
    infile.setpos(anchor + start_index)
    out.writeframes(infile.readframes(length))

def Segment(large_wav_file, slice_index_file):
	slice_indices = np.loadtxt(slice_index_file)
	print(slice_indices)
	large_wav = wave.open(large_wav_file)
	out_dir = '/home/timit_test_out'
	for i in range(len(slice_indices)-1):
		filename = out_dir + '/' + 'out' + str(i) + '.wav'
		index_slice(large_wav, filename, slice_indices[i]*10, slice_indices[i+1]*10)


slices_path = '/home/code/out_sent_length.txt'
wav_path = '/home/code/raw_sound.wav'
Segment(wav_path, slices_path)


