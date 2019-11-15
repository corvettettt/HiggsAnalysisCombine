import glob,os

for i in glob.glob('cards_TAG_scan/dije*TAG*.txt'):
  with open(i) as f:
    lines = []
    for line in f.readlines():
      if 'shapes' in line:
	print line
        folder = line.split()[3].split('/')[1]
        thisline = line.replace(folder+'/dijet','/dijet')
	lines.append(thisline)
      else:
	lines.append(line)
  os.system('rm '+i)
  with open(i,'w+') as f:
    content = ''
    for line in lines:
      content+=line
    f.write(content)


