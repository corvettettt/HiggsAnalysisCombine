import glob,os

L = ['cards_PFNo70Dijet2016bgDeepJet0b','cards_PFNo70Dijet2017bgDeepJet0b','cards_PFNo70Dijet2018bgDeepJet0b']

for i in L:
 for folder in glob.glob(i+'*5p*'):
   folder = folder.replace('cards_','').replace('_scan','')

   print folder
 #  continue
   tag = folder.replace('0b','')
   folder1 = folder
   folder2 = folder.replace('0b','1b')
   folder3 = folder.replace('0b','2b')
   os.system('mkdir '+tag) 
   if '2016' in tag:
     temp = 'excute_tem2016.py'
   elif '2017' in tag:
     temp = 'excute_tem2017.py'
   elif '2018' in tag:
     temp = 'excute_tem2018.py'
   with open(temp) as fin: 
     content = fin.read().replace('Folder1',folder1).replace('Folder2',folder2).replace('Folder3',folder3).replace('TAG',tag)
     with open('excute_'+tag+'.py','w+') as fout:
       fout.write(content)
     os.system('python excute_'+tag+'.py')
   with open('process_tem.py') as fin:
     content = fin.read().replace('TAG',tag)
     with open('process_'+tag+'.py','w+') as fout:
       fout.write(content)
     os.system('python process_'+tag+'.py')
   os.system('mv *'+tag+'* '+tag+'/')


