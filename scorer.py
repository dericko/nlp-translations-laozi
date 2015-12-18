from numpy import zeros, dot
from numpy.linalg import norm
import json, csv
import re
import operator
from trainers import Trainers
from parser import Parser
from math import log

def corp_freq(output, tot_words):
  corp_freq = {}

  for entry in output:
    toks = output.get(entry).get('toks')

    for tok in toks:
      tot_words = tot_words + 1
      cnt = 1
      if tok in corp_freq:
        cnt = corp_freq.get(tok) + 1
      corp_freq.update({tok: cnt}) 

  return corp_freq, tot_words

def doc_vectors(output, master_list, tot_words):

  #TODO can improve with n-grams instead of 1-grams

  vectors = {}
  for entry in output:
    
    vector = zeros(tot_words)
    i = 0
    for word in master_list:
      if word in output.get(entry).get('toks'):
        vector[i] = 1
      i = i + 1

    vectors.update({entry: vector})
  return vectors

def sum(v1, v2):
  v_out = zeros(len(v1))
  for i in range(0, len(v1)):
    if v1[i] == 1 or v2[i] == 1:
      v_out[i] = 1
  return v_out
    
def master_vector(vectors, tot_words):
  t = Trainers()
  master_vector = zeros(tot_words)

  for master in t.get_masters():
    master_vector = sum(master_vector, vectors.get(master))

  return master_vector

def scores(vectors, master):
  scores = {}

  for author in vectors:
    v = vectors.get(author)
    score = float(dot(v, master) / (norm(v) * norm(master))) #cosine measure
    scores.update({author: score})

  return scores

def tf_idf(author):
  tf_idf = {}
  for tok in output.get(author).get('toks'):
    cnt = 1.0
    if tok in mair_freq:
      cnt = mair_freq.get(tok) + 1
    tf_idf.update({tok: cnt}) 

  for entry in tf_idf:
    tf = 1.0 + log(mair_freq.get(entry))
    idf = log( tot_words / master_freq.get(entry) )
    freq = tf * idf
    tf_idf.update({entry: freq})

def should_filter(entry): # Entry(string, int)
  too_many = entry[1] > 333
  too_short = len(entry[0]) < 3
  return too_many or too_short 

# Parse
parser = Parser('laozi-raw_text')
parser.parse()
output = parser.get_output()

# Build freqs
master_freq, tot_words = corp_freq(output, 0)

# Get total order
master_list = []
for tok in sorted(master_freq.items(), key=operator.itemgetter(1)):
  if should_filter(tok): continue
  master_list.append(tok[0])

# Get doc vectors
vectors = doc_vectors(output, master_list, tot_words)

# Sum master doc vectors
master_v = master_vector(vectors, tot_words)

# Output comparison for unknown doc vectors
scores = scores(vectors, master_v)
with open('cosine_scores.csv', 'w') as f:
  for score in sorted(scores.items(), key=operator.itemgetter(1)):
    f.write(score[0] + '\t' + output.get(score[0]).get('date') + '\t' + str(score[1]) +'\n')
  
