#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 01:35:15 2018

@author: sharang
"""
import numpy as np
import os
 
#Given timit phone data, generates a sequence of phonemes mapped to integers with word spaces indicated by @ 

def TimitPrepareTextData(test_dir, target_file):
    
    with open(target_file, 'w') as f:
        for subdir in sorted(os.listdir(test_dir)):
            subdir_path = test_dir + '/' + subdir
            
            for sub_subdir in sorted(os.listdir(subdir_path)):
                sub_subdir_path = subdir_path + '/' + sub_subdir
                filename_list = [f for f in sorted(os.listdir(sub_subdir_path))]
                for filename in filename_list:
                    if filename[-3:] == 'txt':
                        with open(sub_subdir_path + '/' + filename, 'r') as f_read:
                            f.write(f_read.readline())
                
                
                
    
    
    
    


timit_test_dir = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/test'
target = '/home/sharang/Documents/Projects/Speech/Data/timit_sentences.txt'

TimitPrepareTextData(timit_test_dir, target)
#PhoneSeqTimit(wordfile, phonefile, kaldi_phones_dict, timit_to_kaldi_dict)
    
    