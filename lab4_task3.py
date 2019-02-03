fin = open('book.txt','r',encoding='UTF-8')
def number_of_words():
  d = dict()
  for line in fin:
    for c in line.split():
      if c not in d:
        d[c]=1
      else:
        d[c]+=1
    return d

def most_fre_words_within20():
  t = []
  p = number_of_words()
  for key, value in p.items():
    t.append((value,key))
  t.sort(reverse = True)
  return t

t = most_fre_words_within20()
for i,j in t[0:20]:
  print(j,'\t',i)

