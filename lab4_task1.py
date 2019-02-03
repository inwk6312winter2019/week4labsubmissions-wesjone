import string
fin = open('word.txt')
t = ''
for line in fin:
  t = line.strip().lower().replace(' ', '')
  for s in t:
    if s in string.punctuation:
      t = t.replace(s, '')
print(t)
