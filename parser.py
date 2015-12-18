import re
import json
from trainers import Trainers 
from nltk.stem.porter import PorterStemmer 

class Parser():
  def __init__(self, input):
    self.output = {} # map TRANSLATOR->BLOB 
    self.t = Trainers()
    self.input_file = input

  def translation_line(self, s):
    return "Translated by" in s or "translator" in s or "Translated into" in s

  def parse(self):
    with open(self.input_file, 'r') as f:
      lines = f.readlines() 
    
    # Parse entire file
    i = 0
    temp = ""
    for line in lines:

      if (not self.translation_line(line)):

        line = line.rstrip()
        line = re.sub(r'"|;|:|\)|\(|\[|\]|-|!|\?|(\\|0)x\w\w', '', line)
        line = re.sub(r'0xce', '', line)
        line = re.sub(r'-|/|\'', ' ', line)
        temp = temp + " " + line

      else:
        i = i + 1
        items = {}

        # parse translator
        name = re.sub(r"Translat(ed|ion at.*) (into.*by|by)? ", "", line)
        name = re.sub(r"\(.*\)", "", name)
        name = name.rstrip(',')

        # parse date
        date = re.findall(r"\(.*\)", line)
        date = re.sub(r"\(|\)", "", date[0])

        name = name.rstrip()
        items.update({'name': name})
        items.update({'date': date.rstrip()})
        #items.update({'text': temp.rstrip()})
        items.update({'score': self.t.get_score(name)})
        items.update({'toks': self.tokenize(temp.rstrip())})

        if name in self.output:
          name = name + '2'
          self.output.update({name : items})
        else:
          self.output.update({name : items})
        temp = ""

  def clean(self, w):
    return w.lower()

  def should_skip(self, w):
    # remove wtf that is...
    return w == "\xce\xb5\xce\xb9\xce\xb4\xcf\x89\xce\xbb\xce\xbf\xce\xbd" or w == ''

  def tokenize(self, text):
    stemmer = PorterStemmer() 
    toks = re.split(r'\s+?|_|\n|,|\.|\"', text)
    filtered = []
    for tok in toks:
      if self.should_skip(tok): continue
      filtered.append(self.clean(tok))

    stemmed = [stemmer.stem(tok) for tok in filtered]

    return stemmed

  def write_corpus(self):
    for entry in self.output:
      doc = self.output[entry]
      with open('corpus/'+doc.get('name')+'.txt', 'w') as f:
        json.dump(doc.get('text'), f)

  def write_json(self):
    with open('laozi-translations.json', 'w') as f:
      json.dump(self.output, f)

  def get_output(self):
    return self.output
