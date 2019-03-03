fname = input("mbox-short.txt")
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0

fh = open(fname)
for line in fh:
  if line.startswith('From') :
    if line.startswith('From:') : continue
    count = count + 1
    for word in line:
      word = line.split()[1]
    print(word)
print('There were', count, 'lines in the file with From as the first word')



