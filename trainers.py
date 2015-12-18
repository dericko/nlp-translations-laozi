masters = [
  "Arthur Waley",
  "Ch'u Ta-Kao",
  "Lin Yutang",
  "J.J.L. Duyvendak",
  "John C.H. Wu",
  "Wing-Tsit Chan",
  "D.C. Lau",
  "D.C. Lau2",
  "Gia-fu Feng and Jane English",
  "Richard Wilhelm",
  "Ellen M. Chen",
  "Michael LaFargue",
  "Stephen Addiss and Stanley Lombardo",
  "Robert Henricks",
  "Victor H. Mair"
  ]

amateurs = [
  "Witter Brynner",
  "Stephen Mitchell"
  ]

class Trainers():

  def __init__(self):
    self.i = 0
    self.found = []

  def is_master(self, name):
    return name in masters

  def is_amateur(self, name):
    return name.rstrip() in amateurs

  def print_i(self):
    print 'found', self.i, 'masters'
    for master in masters:
      if master not in self.found:
        print master

  def get_score(self, name):
    if name in masters:
      self.i = self.i + 1
      self.found.append(name)
      return 100
    elif name in amateurs:
      return 0
    else:
      return 50

  def get_masters(self):
    return masters
