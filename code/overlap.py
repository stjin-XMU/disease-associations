import pandas as pd
import numpy as np
import collections
d_m_dic = collections.defaultdict(list)
with open('mg.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        d_m_dic[line[0].strip()].append(line[1].upper())

dic = {}
d_name = []
with open('m.id.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        d_name.append(line)
for i,j in enumerate(d_name):
    dic[j] = i+1

g1 = []
g2 = []
g3 = []
chuli = []
def get_overlap(g1,g2):
    over = set(d_m_dic[g1]) & set(d_m_dic[g2])
    uni = set(d_m_dic[g1]) | set(d_m_dic[g2])
    return float(len(over)*1.0 / len(uni))

k=0
for i in range(len(d_m_dic)):
    disease1 = list(d_m_dic.keys())[i]
    for j in range(len(d_m_dic)):
        if i < j:
            disease2 = list(d_m_dic.keys())[j]
            print(k)
            k += 1
            g1.append(disease1)
            g2.append(disease2)
            g3.append(get_overlap(disease1,disease2))
        else:
            continue


df = pd.DataFrame({'d1':g1,'d2':g2,'similarity':g3})
df['d1_name'] = df['d1'].apply(lambda x : x.strip()).map(dic)
df['d2_name'] = df['d2'].apply(lambda x : x.strip()).map(dic)
df = df.dropna()
df.to_csv('overlap_similarity_mm.txt',index=False)




