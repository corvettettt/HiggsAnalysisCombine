import os

for i in [str(i) for i in range(1600,7000,100)]:
  f1 = 'cards_PFNo70Dijet2016bgDeepJet1b3095p_scan/dijet_combine_qg_%s_lumi-37.600_PFNo70Dijet2016bgDeepJet1b3095p.txt'%i
  f2 = 'cards_PFNo70Dijet2017bgDeepJet1b3035p_scan/dijet_combine_qg_%s_lumi-41.800_PFNo70Dijet2017bgDeepJet1b3035p.txt'%i
  f3 = 'cards_PFNo70Dijet2018bgDeepJet1b277_scan/dijet_combine_qg_%s_lumi-59.750_PFNo70Dijet2018bgDeepJet1b277.txt'%i
  print 'python combineCards.py PFDijet2016=%s PFDijet2017=%s PFDijet2018=%s > dijet_combine_qg_%s_lumi-137.700_PFNo65Dijet1617187bgDeepJet.txt'%(f1,f2,f3,i)
  os.system('python combineCards.py PFDijet2016=%s PFDijet2017=%s PFDijet2018=%s > cards_PFNo70Dijet161718DeepJet1b_scan/dijet_combine_qg_%s_lumi-137.700_PFNo70Dijet161718DeepJet1b.txt'%(f1,f2,f3,i)) 
