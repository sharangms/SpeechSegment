#Requires PyKaldi

import numpy as np

class LongTermAligner:
        def __init__(self, text_file, mfcc_array, trans_model, em_model):
                self.mfcc = mfcc_array
                read = open(text_file,'r')
                sentences = read.readlines()
                sentences = [(s.replace('\n','')) for s in sentences]
                self.sentences = sentences
                self.transition_model = trans_model
                self.emission_model = em_model

        def test(self):
                print(self.sentences)
                print(self.transition_model)
                print(self.emission_model)
                print((self.mfcc).shape)

        def PhonePdfStateList(self, phone_list):
                (x, pdf_list) = get_pdfs_for_phones(self.transition_model, phone_list)
                return pdf_list

        def InSamePhone(self, trans_state_1, trans_state_2):
                ph1 = self.transition_model.transition_state_to_phone(trans_state_1)
                ph2 = self.transition_model.transition_state_to_phone(trans_state_2)
                return ph1 == ph2

        def TransitProb(self, pdf_state_from, pdf_state_to):
                if pdf_state_from == pdf_state_to:
#Self Loop
                        trans_type = 0
                else:
#Forward
                        trans_type = 1
                trans_id = self.transition_model.pair_to_transition_id(pdf_state_from + 1, trans_type)
                return self.transition_model.get_transition_log_prob(trans_id)


        def align(self, sent_index, mfcc_index):
#Making an initial overestimate of the no. of observation sequences aligned
                overestimate = len(self.sentences[sent_index]) * 2
#Obtaining a sequence of all states in the sentence
                for_states = self.sentences[sent_index]
                for_states = for_states.replace('@','1')
                for_states = list(np.int32(for_states.split(',')))
                states_seq = PhonePdfStateList(for_states)
                num_models = len(states_seq)

#Keeping a copy of the original string to locate optional silences
                for_opt_sil = self.sentences[sent_index].split(',')
                opt_index = -1
#Initialising the forward variable matrix for viterbi -alpha and backtracker
                alpha = np.zeros((overestimate, num_models), dtype = np.float32)
                backtrack = np.zeros((overestimate, num_models), dtype = np.int32)
#Starting in the left most state
                init_data_vec = Vector(self.mfcc[mfcc_index])
                alpha[0,0] = emission_model.log_likelihood(states_seq[0],init_data_vec)
#Iterating over the observation sequence and updating the alpha matrix
                for count_feat in range(1, overestimate):
                        obs = Vector(sel.mfcc[mfcc_index + count_feat])
                        for count_state in range(0, num_models):
                                state = states_seq[count_state]
                                state_prev = states_seq[count_state - 1]
                                if count_state == 0:
                                        stay = alpha[count_feat-1, count_state] + TransitProb(state, state) + emission_model.log_likelihood(state, obs)
                                        alpha[count_feat,count_state] = stay
                                else:
                                        after_opt_sil = (state_prev == 1) and (state != 1)
                                        if after_opt_sil:
                                                state_jump = states_seq[count_state - 2]
                                                stay = alpha[count_feat-1, count_state] + TransitProb(state, state) + emission_model.log_likelihood(state, obs)
                                                move = alpha[count_feat-1, count_state - 1] + np.log(0.5) + TransitProb(state_prev, state) + emission_model.log_likelihood(state, obs)
                                                jump = alpha[count_feat-1, count_state - 2] + np.log(0.5) + TransitProb(state_jump, state) + emission_model.log_likelihood(state, obs)
                                                alpha[count_feat,count_state] = np.max(stay, move, jump)
                                        else:
                                                stay = alpha[count_feat-1, count_state] + TransitProb(state, state) + emission_model.log_likelihood(state, obs)
                                                move = alpha[count_feat-1, count_state - 1] + TransitProb(state_prev, state) + emission_model.log_likelihood(state, obs)
                                                alpha[count_feat,count_state] = np.max(stay, move)
                print(alpha)
