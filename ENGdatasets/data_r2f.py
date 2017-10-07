# -*- coding: utf-8 -*-

import os
import re, string
import tqdm
# from gensim.models import *
from gensim.models import KeyedVectors

######
# TODO:
#   Loop eliminating punc_ptrn

# wv = KeyedVectors.load('SohuNews_w2v_CHN_300.bin')
wv = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300-SLIM.bin', binary=True)

input_dir = 'Raw_data'
output_dir = 'Fmt_data_divsens'
news_id = 0
DIR_SZ = 5000
punc = [',','.',"'",'"',':',';','(',')','!']

# ff01 = '！', ff1f = '？', ff0c = '，', 3002 = '。'

Q2B_dict = dict((c, c - 65248) for c in range(65281, 65375))

def _is_num(s):
    try:
        float(s)
        return True
    except:
        return False


def get_sen_list(doc, div_sens = True):
    begin_mark = u'BG'
    end_mark = u'ED'
    num_mark = u'NUM'
    res = []

    if div_sens:
        # chars = re.findall(ur'[\u4e00-\u9fa5\uff01\uff1f\u3002]', doc)
        # print chars
        # res = []
        # w_list = [begin_mark]
        # for w in chars:
        #     if w in u'。！？':           # ending punc
        #         if len(w_list) > 1:     # is a sentence
        #             w_list.append(end_mark)
        #             res.append(' '.join(w_list))
        #             w_list = [begin_mark]
        #     elif w in wv:               # known char
        #         w_list.append(w)

        # if len(w_list) > 1:     # remaining words
        #     w_list.append(end_mark)
        #     res.append(' '.join(w_list))
        
        chars = doc.split(' ')
        w_list = [begin_mark]
        for w in chars:
            wtrue = w
            for idx in xrange(len(punc)):
                wtrue = wtrue.replace(punc[idx],'')
            if len(wtrue) < 1: continue
            if w[-1] == '.' or w[-1] == '?' or w[-1] == "!": # ending of a sentence
                if _is_num(wtrue):
                    w_list.append(num_mark)
                elif wtrue in wv:
                    w_list.append(wtrue.lower())
                if len(w_list) > 1:
                    w_list.append(end_mark)
                    res.append(' '.join(w_list))
                    w_list = [begin_mark]
            elif _is_num(wtrue):
                w_list.append(num_mark)
            elif wtrue in wv:
                w_list.append(wtrue.lower())
        if len(w_list) > 1:
            w_list.append(end_mark)
            res.append(' '.join(w_list))

    else:
        chars = doc.split(' ')
        # chars = re.findall(ur'[\u4e00-\u9fa5]', doc)
        chars = [begin_mark] + [c for c in chars if c in wv] + [end_mark]   # remove UNK
        res = [' '.join(chars)]
    return res
    



if not os.path.exists('./%s' % output_dir):
    os.mkdir('./%s' % output_dir)

input_file_list = []
for dirpath, dirnames, filenames in os.walk('./' + input_dir):
    for fnm in filenames:
        input_file_list.append((dirpath, fnm))

for dirpath, fnm in tqdm.tqdm(input_file_list):
    fin = open('%s/%s' % (dirpath, fnm), 'r')
    lines = fin.readlines()
    fin.close()
        
    # Deal with title
    s = ''
    lid = 0
    for lid in range(1, len(lines)):
        if lines[lid].find('Content:') >= 0:
            break
        # s += lines[lid].decode('gb18030', 'ignore').strip()
        s += lines[lid].strip()

    hd = get_sen_list(s)
    lid += 1

    # Deal with content
    s = ''
    for lid in range(lid, len(lines)):
        # s += lines[lid].decode('gb18030', 'ignore').strip()
        s += lines[lid].strip()

    ctnt = get_sen_list(s)
    # ctnt = list of all sentences

    if len(ctnt) <= 0 or len(hd) <= 0:  # Malformed - maybe not a news file
        continue

    # Output
    if news_id % DIR_SZ == 0 and not os.path.exists('./%s/%d' % (output_dir, news_id / DIR_SZ)):
        os.mkdir('./%s/%d' % (output_dir, news_id / DIR_SZ))

    fout = open('./%s/%d/%d.txt' % (output_dir, news_id / DIR_SZ, news_id), 'w')
    # fout.write('Title:\n%s\nContent:\n' % hd[0].encode('utf-8'))
    fout.write('Title:\n%s\nContent:\n' % hd[0])
    for s in ctnt:
        # fout.write('%s\n' % s.encode('utf-8'))
        fout.write('%s\n' % s)
    fout.close()

    # if news_id % DIR_SZ == 0:
        # print('Progress: %d' % news_id)

    news_id += 1

