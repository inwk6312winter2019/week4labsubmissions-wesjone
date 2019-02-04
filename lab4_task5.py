import matplotlib

def freq_rank(hist):
  rf = [(r+1,f) for r,f in enumerate(freqs)]
  return rf
def print_ranks(hist):
  for r,f in freq_rank(hist):
    print(r,f)
def plot_line(hist,scale = 'log'):
  t = freq_rank(hist)
  rs,fs=zip(*t)
  pyplot.clf()
  pyplot.xscale(scale)
  pyplot.yscale(scale)
  pyplot.title('Zipf ploy')
  pyplot.xlabel('rank')
  pyplot.ylabel('frequency')
  pyplot.plot(rs,fs,'r-')
  pyplot.show()

def main(name, filename='book.txt', flag='plot',*args):
  hist = process_file(filename,skip_header=True)
  if flag == 'print'
    print_ranks(hist)
  elif flag == 'plot'
    plot_ranks(hist)
  else:
    print('usage:zipf.py filename [print|plot]')
if __name__ == '__main__':
  main(*sys.argv)
