#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:36:42 2018

@author: sharang
"""
import os
import wave

def TimitPrepareWaveData(test_dir, target_file): 
    wav_concat = []
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
                    wav_concat.append( [new_wave.getparams(), new_wave.readframes(new_wave.getnframes())] )
                    new_wave.close()
    print(len(wav_concat))   
    output = wave.open(target_file, 'wb')
    output.setparams(wav_concat[0][0])
    for count in range(0, len(wav_concat)):
        output.writeframes(wav_concat[count][1])
    output.close()
                    
                    
timit_test_dir = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/test'
target = '/home/sharang/Documents/Projects/Speech/Data/wave_concat.wav'
TimitPrepareWaveData(timit_test_dir, target)