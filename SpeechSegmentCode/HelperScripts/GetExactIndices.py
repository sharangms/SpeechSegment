#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:36:42 2018

@author: sharang
"""
import numpy as np
import os
import wave

def TimitPrepareWaveData(test_dir, target_file): 
    indices = []
    sum_duration = 0
    for subdir in sorted(os.listdir(test_dir)):
        subdir_path = test_dir + '/' + subdir
        
        for sub_subdir in sorted(os.listdir(subdir_path)):
            sub_subdir_path = subdir_path + '/' + sub_subdir
            filename_list = [os.path.splitext(f)[0] for f in os.listdir(sub_subdir_path)]
            filename_list = list(set(filename_list))
            for file in sorted(filename_list):
                if file[:3] == 'WAV':
                    file_path = sub_subdir_path + '/' + file + '.wav'
                    print(file_path)
                    new_wave = wave.open(file_path, 'rb')
                    frames = new_wave.getnframes()
                    rate = new_wave.getframerate()
                    fpms = np.int32(rate/1000)
                    duration = frames / float(rate)
                    sum_duration = sum_duration + duration
                    indices.append(sum_duration * 200)
                    new_wave.close()
    indices = np.array(indices)
    np.save(target_file, indices)
                    
                    
timit_test_dir = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/test'
target = '/home/sharang/Documents/Projects/Speech/Data/actual_indices.npy'
TimitPrepareWaveData(timit_test_dir, target)