import numpy as np
import wave
from kaldi.util.table import MatrixWriter
from kaldi.feat.wave import WaveData
from kaldi.util.io import xopen
from kaldi.feat.mfcc import Mfcc,MfccOptions
from kaldi.matrix import Vector, DoubleMatrix, Matrix
from kaldi.feat.functions import DeltaFeatures, DeltaFeaturesOptions
#Setting Source and Target File Locations
source_file = '/home/code/raw_sound.wav'
target_file = '/home/code/timit_mfcc.npy'
#Reading Wave data into file
source_file = '/home/code/raw_sound.wav'
wav_reader = WaveData()
wav_obj = xopen(source_file)
wav_reader.read(wav_obj.stream())
wav_data = wav_reader.data()
#Preparing MFCC
mfcc_opts = MfccOptions()
mfcc_opts.frame_opts.samp_freq = 16000
mfcc = Mfcc(mfcc_opts)
sf = mfcc_opts.frame_opts.samp_freq
#Computing 13 dim  MFCC
wav_data = wav_data.numpy()
wav_data = wav_data.flatten()
features = mfcc.compute_features(Vector(wav_data), 16000, 1.0)
feat = features.numpy()

#Appending Deltas and Delta-Deltas
delta_opts = DeltaFeaturesOptions()
delta_opts.order = 2
delta_feat_obj = DeltaFeatures(delta_opts)
empty_delta_frame = Vector(39)
mfcc_39_dim = []
for row_count in range(0,feat.shape[0]):
        delta_feat_obj.process(features, row_count, empty_delta_frame)
        mfcc_39_dim.append(list(empty_delta_frame.numpy()))

mfcc_39_dim = np.asarray(mfcc_39_dim)
np.save(target_file, mfcc_39_dim)
