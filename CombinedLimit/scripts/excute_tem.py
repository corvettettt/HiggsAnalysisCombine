import os

for i in [str(i) for i in range(1600,7000,100)]:
  f1 = 'cards_Folder1_scan/dijet_combine_qg_%s_lumi-37.600_Folder1.txt'%i
  f2 = 'cards_Folder2_scan/dijet_combine_qg_%s_lumi-41.800_Folder2.txt'%i
  f3 = 'cards_Folder3_scan/dijet_combine_qg_%s_lumi-59.750_Folder3.txt'%i
  print 'python combineCards.py PFDijet2016=%s PFDijet2017=%s PFDijet2018=%s > dijet_combine_qg_%s_lumi-137.700_TAG.txt'%(f1,f2,f3,i)
  os.system('python combineCards.py PFDijet2016=%s PFDijet2017=%s PFDijet2018=%s > cards_TAG_scan/dijet_combine_qg_%s_lumi-137.700_TAG.txt'%(f1,f2,f3,i)) 
