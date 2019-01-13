#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 01:35:15 2018

@author: sharang
"""
import numpy as np
import os

def BuildDict(phone_mapping_file):
    phone_map = np.genfromtxt(phone_mapping_file, dtype = str)
    mapping_dict = dict(zip(phone_map[:,0], phone_map[:,1]))
    return mapping_dict
 
#Given timit phone data, generates a sequence of phonemes mapped to integers with word spaces indicated by @ 
def PhoneSeqTimit(word_file, phone_file, kaldi_phones_dict, timit_to_kaldi_dict):
    words = np.genfromtxt(word_file, dtype = str)
    phones = np.genfromtxt(phone_file, dtype = str)
    
    output_string = ''
    count_word = 0
    for j in range(0, len(phones)):
        cur_word_index = min(count_word, len(words) - 1)
        current_word_end = np.int32(words[cur_word_index,1])
        current_phone_end = np.int32(phones[j,1])
        if current_phone_end > current_word_end:
            output_string += '@' + ','
            count_word = count_word + 1
        if phones[j,2] != 'q':
            phone_to_write = kaldi_phones_dict[timit_to_kaldi_dict[phones[j,2]]]
            output_string += phone_to_write + ','
            
    return output_string[:-1]

def TimitPrepareTextData(test_dir, kaldi_mapping_file, timit_to_kaldi_mapfile, target_file):
    kaldi_phones_dict = BuildDict(kaldi_mapping_file)
    timit_to_kaldi_dict = BuildDict(timit_to_kaldi_mapfile)
    
    with open(target_file, 'w') as f:
        for subdir in sorted(os.listdir(test_dir)):
            subdir_path = test_dir + '/' + subdir
            
            for sub_subdir in sorted(os.listdir(subdir_path)):
                sub_subdir_path = subdir_path + '/' + sub_subdir
                filename_list = [os.path.splitext(f)[0] for f in os.listdir(sub_subdir_path)]
                filename_list = list(set(filename_list))
                
                for file in sorted(filename_list):
                    if file[:3] != 'WAV':
                        word_file = sub_subdir_path + '/' + file + '.wrd'
                        phone_file = sub_subdir_path + '/' + file + '.phn'
                        line = PhoneSeqTimit(word_file, phone_file, kaldi_phones_dict, timit_to_kaldi_dict)
                        f.write(line + '\n')
                
                
                
    
    
    
    

wordfile = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/train/dr1/fdaw0/sa2.wrd'
phonefile = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/train/dr1/fdaw0/sa2.phn'
phone_map_file = '/home/sharang/kaldi/egs/timit/s5/data/lang/phones.txt'
timit_to_kaldi_file = '/home/sharang/Documents/Projects/Speech/Data/phones_timit_kaldi.map'
timit_test_dir = '/home/sharang/Documents/Projects/Speech/Data/TIMIT/timit/test'
target = '/home/sharang/Documents/Projects/Speech/Data/phoneseq.txt'

kaldi_phones_dict = BuildDict(phone_map_file)
timit_to_kaldi_dict = BuildDict(timit_to_kaldi_file)
TimitPrepareTextData(timit_test_dir, phone_map_file, timit_to_kaldi_file, target)
#PhoneSeqTimit(wordfile, phonefile, kaldi_phones_dict, timit_to_kaldi_dict)
    
    