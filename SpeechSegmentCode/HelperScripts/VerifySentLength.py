#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 01:35:15 2018

@author: sharang
"""
import numpy as np
import os

def TimitPrepareVerificationData(test_dir,target_file):
    with open(target_file, 'w') as f:
        for subdir in sorted(os.listdir(test_dir)):
            subdir_path = test_dir + '/' + subdir
            
            for sub_subdir in sorted(os.listdir(subdir_path)):
                sub_subdir_path = subdir_path + '/' + sub_subdir
                filename_list = [os.path.splitext(f)[0] for f in os.listdir(sub_subdir_path)]
                filename_list = list(set(filename_list))
                
                for file in sorted(filename_list):
                    if file[:3] != 'WAV':
                        text_file = sub_subdir_path + '/' + file + '.txt'
                        text_file_data = np.genfromtxt(text_file, dtype=str)

                        f.write(str(np.int32(text_file_data[1])/200.0) + '\n')
                

timit_test_dir = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/test'
target = '/home/sharang/Documents/Projects/Speech/Data/test_sent_length.txt'

TimitPrepareVerificationData(timit_test_dir, target)
#PhoneSeqTimit(wordfile, phonefile, kaldi_phones_dict, timit_to_kaldi_dict)
    
    