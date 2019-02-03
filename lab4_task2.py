import string
fin = open('book.txt','r',encoding='UTF-8')
def del_punctuation(word):
  for c in word:
    if c in string.puctuation:
      word = word.replace(c,'')
  return word

def count_words_inbook():
  total_number = 0
  for line in fin:
    for item in line.split():
      total_number+=1
  print(total_number)

def break_into_words():
  res = []
  for every_line in fin:
    for every_word in every_line.split():
      every_word = del_puctuation(every_word)
      every_word = every_word.lower()
      res.append(every_word)
  return res

def count_times_ofwords():
  p = break_into_words()
  d = dict()
  for c in p:
    if c not in d:
      d[c] =1
    else:
      d[c]+=1
  return d

def fre_words():
  t = []
  p = count_times_ofwords()
  for i, j in p.items():
    t.append((j,i))
  t.sort(reverse =True)
  return t

print(fre_words())
