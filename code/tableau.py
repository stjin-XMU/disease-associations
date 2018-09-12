import numpy as np
import pandas as pd
from sklearn.manifold import TSNE

rep = np.loadtxt('omim_dmg.txt')
id = rep[:,0]
rep = rep[:,1:]
x_tsne = TSNE().fit_transform(rep)
id_name = {}
with open('omim_d_id.txt','r') as f:
    lines = f.readlines()
    for i,j in enumerate(lines):
        j = j.strip()
        id_name[i] = j
id = [id_name[x] for x in id]
df1 = pd.DataFrame(x_tsne)
df1.index = id
df1.columns=['x','y']
writer = pd.ExcelWriter('omim_dmg_tsne.xlsx')
df1.to_excel(writer,'omim_dmg')


'''rep = np.loadtxt('t_sen.gg_ggg.txt')
id = rep[:,0]
rep = rep[:,1:]
x_tsne = TSNE().fit_transform(rep)
id_name = {}
with open('d_id.txt','r') as f:
    lines = f.readlines()
    for i,j in enumerate(lines):
        j = j.strip()
        id_name[i] = j
id = [id_name[x] for x in id]
df = pd.DataFrame(x_tsne)
df.index = id
df.columns=['x','y']
df.to_excel(writer,'gg_ggg')'''
writer.save()