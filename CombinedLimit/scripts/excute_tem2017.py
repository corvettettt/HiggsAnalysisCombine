import os

for i in [str(i) for i in range(1600,7000,100)]:
  f1 = 'cards_Folder1_scan/dijet_combine_qg_%s_lumi-41.800_Folder1.txt'%i
  f2 = 'cards_Folder2_scan/dijet_combine_qg_%s_lumi-41.800_Folder2.txt'%i
  f3 = 'cards_Folder3_scan/dijet_combine_qg_%s_lumi-41.800_Folder3.txt'%i
  print 'python combineCards.py PFDijet20170b=%s PFDijet20171b=%s PFDijet20172b=%s > dijet_combine_qg_%s_lumi-41.800_TAG.txt'%(f1,f2,f3,i)
  os.system('python combineCards.py PFDijet20170b=%s PFDijet20171b=%s PFDijet20172b=%s > dijet_combine_qg_%s_lumi-41.800_TAG.txt'%(f1,f2,f3,i)) 
