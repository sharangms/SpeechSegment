#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:35:27 2018

@author: sharang
"""

import wave
test = wave.open('/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/test/dr1/faks0/WAVsi2203.wav', 'rb')
frame = test.readframes(test.getnframes())
print('frame',frame)