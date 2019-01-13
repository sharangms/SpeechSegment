from kaldi.feat.mfcc import Mfcc, MfccOptions
from kaldi.matrix import SubVector, SubMatrix
from kaldi.util.options import ParseOptions
from kaldi.util.table import SequentialWaveReader
from kaldi.util.table import MatrixWriter
from numpy import mean
from sklearn.preprocessing import scale
usage = """Extract MFCC features.
Usage: example.py [opts...] <rspec> <wspec>
"""
po = ParseOptions(usage)
po.register_float("min-duration", 0.0,
"minimum segment duration")
mfcc_opts = MfccOptions()
mfcc_opts.frame_opts.samp_freq = 8000
mfcc_opts.register(po)
# parse command-line options
opts = po.parse_args()
rspec, wspec = po.get_arg(1), po.get_arg(2)
mfcc = Mfcc(mfcc_opts)
sf = mfcc_opts.frame_opts.samp_freq
with SequentialWaveReader(rspec) as reader, \
MatrixWriter(wspec) as writer:
	for key, wav in reader:
		if wav.duration < opts.min_duration:
			continue
		assert(wav.samp_freq >= sf)
		assert(wav.samp_freq % sf == 0)
		# >>> print(wav.samp_freq)
		# 16000.0
		s = wav.data()
		s = s[:,::int(wav.samp_freq / sf)]
		# mix-down stereo to mono
		m = SubVector(mean(s, axis=0))
		# compute MFCC features
		f = mfcc.compute_features(m, sf, 1.0)
		standardize_features = SubMatrix(scale(f))
		print('The Features', standardize_features)
		print('The Shape', standardize_features.Shape)

		# write features to archive
		writer[key] = f