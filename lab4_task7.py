def sed(pattern,replacement,f1,f2):
  fread = open('f1','r')
  fwrite = open('f2','w')
  a = 'a'
  text = ''
  while a != '':
    a = fread.readline()
    text = text +a
  while pattern in text:
    p = text.find(pattern)
    text = text[:p]+replacement+text[p+len(pattern):]
  fwrite.write(text)
  fread.close()
  fwrite.close()
  return 'does not fempute'

