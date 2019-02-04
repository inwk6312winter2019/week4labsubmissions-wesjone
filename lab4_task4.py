##this is the first way
fin = open('words.txt')
fin2 = open('book.txt','r',encoding='UTF-8')
def different_words():
  t = []
  for line in fin2:
    for c in line.split():
      if c not in fin:
        t.append(c)
  return t
print(different_words())

##second way to achieve
def hist_line(filename):
  fp=open(filename,'r',encoding='UTF-8')
  hist = dict()
  for line in fp:
    hist_word(line,hist)
  return hist

def hist_word(line,hist):
  t = line.strip().lower().replace('',' ')
  t = t.split()
  for c in t:
    hist[c]=hist.get(c,0)+1
  return hist

def subtract(d1,d2)
  res={}
  for i in d1:
    if i not in d2:
      res[i] = None
  return res

words = hist_line('words.txt')
hist = hist_line('book.txt')
print(subtract(hist,words))
