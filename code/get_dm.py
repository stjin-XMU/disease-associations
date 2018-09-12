import pandas as pd
dm = pd.read_excel('dm-mg.xlsx','dm',names=['disease','mi','s'])
mg = pd.read_excel('dm-mg.xlsx','mg')
dg = pd.merge(dm,mg,left_on='mi',right_on='miRNAname')
dic = {}
d_name = []
with open('d_id.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        d_name.append(line)
for i,j in enumerate(d_name):
    dic[j] = i+1

dg['d_id'] = dg['disease'].map(dic)

dg = dg.iloc[:,[-1,-2]]
dg = dg.drop_duplicates(['d_id','EntrezID'])
dg = dg.dropna()
dg['d_id'] = dg['d_id'].astype(int)
dg.to_csv('DGmat_id.txt',sep=' ',index=False)