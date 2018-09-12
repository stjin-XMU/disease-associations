import pandas as pd
import collections
import numpy as np
from scipy.spatial.distance import pdist

disease_dic = collections.defaultdict(list)
with open('omim_output.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        if line[0].startswith('i'):
            vec = line[1:]
            vec = [float(i) for i in vec]
            disease_dic[int(line[0][1:])] = vec

def cos(vec1,vec2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a,b in zip(vec1,vec2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    return dot_product / ((normA * normB) ** 0.5)


disease_name = collections.defaultdict()
with open('omim_d_id.txt','r') as f:
    lines = f.readlines()
    for i,j in enumerate(lines):
        j = j.strip()
        disease_name[i+1] = j

disease_list = sorted(disease_dic.keys())
disease1 = []
disease2 = []
cos_similarity = []
for i in disease_list:
    for j in disease_list:
        if i < j:
            disease1.append(i)
            disease2.append(j)
            cos_similarity.append(cos(disease_dic[i],disease_dic[j]))

similarity = pd.DataFrame({'disease1':disease1,'disease2':disease2,'similarity':cos_similarity})
similarity['disease1_name'] = similarity['disease1'].apply(lambda x :disease_name[x])
similarity['disease2_name'] = similarity['disease2'].apply(lambda x :disease_name[x])

# disease1 = []
# disease2 = []
# similarity_df = pd.DataFrame(index=disease_list)
# for i in disease_list:
#     cos_similarity = []
#     for j in disease_list:
#             cos_similarity.append(cos(disease_dic[i],disease_dic[j]))
#     similarity_df[i] = cos_similarity
#
# ddscore = pd.read_excel('D-D-score.xlsx','Sheet1',names=['d1','d2','score'])
# ddscore['d1name'] = ddscore['d1'].apply(lambda x : disease_name[x])
# ddscore['d2name'] = ddscore['d2'].apply(lambda x : disease_name[x])
# writer = pd.ExcelWriter('ddscore.xlsx')
# ddscore.to_excel(writer,'Sheet1',index=False)
# writer.save()


writer = pd.ExcelWriter('similarity-omim.xlsx')
similarity.to_excel(writer,'Sheet1',index=False)
#similarity_df.to_excel(writer,'Sheet2',index=False)
writer.save()

