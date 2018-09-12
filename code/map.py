# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# MeSH = pd.read_csv('201610_MeSH.txt')
import sys   
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')  

MeSH = pd.read_excel('Workbook1.xlsx')
MeSH['Name'] = MeSH['Name'].apply(lambda x: str(x).lower())
d_id = []
with open('c.id.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        d_id.append(line)
d_id_low = [x.lower() for x in d_id]
d_id_df = pd.DataFrame({'Name': d_id_low,'Name1':d_id})
d_merge = pd.merge(MeSH,d_id_df,left_on='Name',right_on='Name')
d_merge = d_merge.iloc[:,[-2,-1]]
d_merge['Name1'] = d_merge['Name1'].astype(str)
d_merge.to_csv('c_id_unique.txt',index=False)