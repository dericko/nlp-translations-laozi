from bs4 import BeautifulSoup 

with open('laozi-source.html', 'r') as html_doc:
  soup = BeautifulSoup(html_doc, 'html.parser')

print soup.title

# text += each blockquote.p
# author = blockquote.p.where('alight=right')
# author = "Translated by FNAME-LNAME (DATE)" or SOURCE

def is_author(tag):
  return tag.has_attr('align') and tag.attrs['align'] == 'right'

def is_text(tag):
  return not is_author(tag) 

def translation_line(s):
  return "Translated by" in s or "translator" in s

for block in soup.find_all('blockquote'):
  for text in block.find_all(is_text):
    cleaned = text.get_text(' ', strip=True)
    if translation_line(cleaned): 
      print "RM FROM TEXT", cleaned
      continue
    print "TEXT:"
    print cleaned
  for author in block.find_all(is_author):
    cleaned = author.get_text(' ', strip=True)
    if not translation_line(cleaned): 
      print "RM FROM AUTHOR", cleaned
      continue
    print "AUTHOR:"
    print cleaned


# blockquote > p > *
# p where align=right
