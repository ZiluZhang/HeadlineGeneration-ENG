import math
import numpy as np
import gzip, cPickle
import os
# from gensim.models import *
from gensim.models import KeyedVectors

rng = np.random

WRITE_DICT = True
input_dir = 'Fmt_data_divsens'
# stop_words_file = 'Stop-words-none.txt'

# wv = KeyedVectors.load('SohuNews_w2v_CHN_300.bin')
wv = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300-SLIM.bin', binary=True)

d = {}                          # Used words: word -> vector
d_w2id = {}                     # word -> id
id2w = []                       # id -> word
id2v = []                       # id -> vector

# fo = open(stop_words_file, 'r')
# stop_words = fo.readlines()
# fo.close()
# for i in range(len(stop_words)):
#     stop_words[i] = stop_words[i].strip()

def regWord(w):
    if w in wv:
        d[w] = wv[w]
    # elif len(wd) > 0 and not d.has_key(wd):
    #     _v = rng.uniform(-1, 1, 300)
    #     _v = _v / np.linalg.norm(_v)
    #     d[wd] = _v

fid = 0
for dirpath, dirnames, filenames in os.walk('./' + input_dir):
    for fnm in filenames:
        fo = open('%s/%s' % (dirpath, fnm), 'r')
        lines = fo.readlines()
        fo.close()

        if len(lines) < 4:     # Malformed
            continue
        title = lines[1].strip().split(' ')     # Need to strip(), because the end mark is 'ED'...
        ctnt = ' '.join([lines[i].strip() for i in range(3, len(lines))]).split(' ')

        for wd in title:
            regWord(wd)
        for wd in ctnt:
            regWord(wd)

        if fid % 1000 == 0:
            print('Progress: %d' % fid)
        fid += 1

print('--- Registering words completed.')
    
if WRITE_DICT:
    d_w2id[''] = 0
    id2w.append('')
    id2v.append(np.zeros(300))              # word No.0 is 'padding'
    index = 1
    for w, v in d.iteritems():
        d_w2id[w] = index                   # New index = current len of the list
        id2w.append(w)
        id2v.append(v)
        index += 1

    fo = open('w2id.pkl', 'wb')
    cPickle.dump(d_w2id, fo)
    fo.close()
    fo = open('id2w.pkl', 'wb')
    cPickle.dump(id2w, fo)
    fo.close()
    fo = open('id2v.pkl', 'wb')
    cPickle.dump(id2v, fo)
    fo.close()
    print('--- Output completed.')
    print('size of d = ' + str(len(d_w2id)))
