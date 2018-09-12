# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
import collections
d_name = []
#打开疾病名称文本文件，获取疾病名
with open('omim_d_id.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        d_name.append(line.upper())

d_name_id = collections.defaultdict()
for d,v in enumerate(d_name):
    d_name_id[v] = 'i' + str(d+1)


m_name = []
with open('m.id.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        m_name.append(line.upper())

m_name_id = collections.defaultdict()
for d,v in enumerate(m_name):
    m_name_id[v] = 'f' + str(d+1)


#添加疾病，mirna的名字到对应编号里
dm = collections.defaultdict(list)
md = collections.defaultdict(list)
with open('omim_dm.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        if line[1].upper() in m_name:
            dm[d_name_id[line[0].upper().strip()]].append(m_name_id[line[1].upper()])
            md[m_name_id[line[1].upper()]].append(d_name_id[line[0].upper().strip()])

mg_df = pd.read_table('mg.txt',names=['mrna','gene'])
gg_df = pd.read_table('Lung_GTEx_co-expression_PIN_update.txt',names=['gene1','gene2','pvalue1','pvalue','pvalue3'],sep='\t')
gg_df = gg_df[abs(gg_df['pvalue']) <= 0.05]
g_name = set(gg_df['gene1'].unique()) | set(gg_df['gene2'].unique())
g_name = set(mg_df['gene'].unique()) & g_name
g_name = ['a' + str(i) for i in g_name]


gg = collections.defaultdict(list)
with open('Lung_GTEx_co-expression_PIN_update.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        if float(line[3]) <= 0.05:
            g1 = 'a' + str(line[0])
            g2 = 'a' + str(line[1])
            if (g1 in g_name) & (g2 in g_name):
                gg[g1].append(g2)
                gg[g2].append(g1)

gene_del = []
for gene in gg.keys():
    if len(gg[gene]) == 2:
        gene_del.append(gene)
for gene in gene_del:
    del gg[gene]

g_name = list(gg.keys())

mg = collections.defaultdict(list)
gm = collections.defaultdict(list)
with open('mg.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        g = 'a'+str(line[1])
        if (line[0].upper() in m_name) & (g in g_name):
            mg[m_name_id[line[0].upper().strip()]].append(g)
            gm[g].append(m_name_id[line[0].upper().strip()])

def random_walk_disease(d1):
    m1 = random.choice(dm[d1])
    g1 = random.choice(mg[m1])
    g2 = random.choice(gg[g1])
    m2 = random.choice(gm[g2])
    d2 = random.choice(md[m1])
    return [d1,m1,g1,g2,m2,d2]

disease_list = []
for d in dm.keys():
    ms = dm[d]
    for m in ms:
        if set(mg[m]) & set(g_name):
            disease_list.append(d)
disease_list = list(set(disease_list))

disease_list2 = []
for disease in disease_list:
    jj = 0
    j = 1
    while((j == 1) & (jj != 1000)):
        try:
            random_walk_disease(disease)
        except:
            j = 1
            jj += 1
        else:
            j = 0
            jj = 0
    if jj == 0:
        disease_list2.append(disease)


total_walk = []
ii=0
for disease in disease_list:
    jj = 0
    for i in range(1000):
        print(str(ii) + ' ' + str(i))
        temp = [disease]
        for k in range(50):
            j=1
            while ((j == 1) & (jj!=1000)):
                try:
                    temp2 = random_walk_disease(disease)
                    temp.extend(temp2[1:])
                    disease = temp2[-1]
                except:
                    j = 1
                    jj += 1
                else:
                    j = 0
            if jj ==1000:
                break
        total_walk.append(temp)
    ii += 1

with open('inputomim.txt','w') as f:
    for lines in total_walk:
        for line in lines:
            f.write(line +' ')
        f.write('\n')










































































































































































































































