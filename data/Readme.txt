disease-miRNA-gene.data:初始网络数据集。（d.id:疾病名和id;dm:disease-miRNA;omim.dm:从omim中得到的disease-gene里有的疾病的disease-miRNA关联；
omim.dg:从omim中得到的disease-gene;omim.d.id:从omim中得到的disease-gene中的疾病；g.id:gene的名字和id;mg:miRNA-gene;mg-m.id:miRNA-gene中存在的miRNA的名字；
m.id:所有的miRNA的名字。

metapath2vec++(dggd).similarity：选择元路径为dggd得到的疾病之间的相似性。

metapath2vec++(dgggd).similarity:选择元路径为dgggd得到的疾病之间的相似性。

metapath2vec++(dmgggmd).similarity:选择元路径为dmgggmd得到的疾病之间的相似性。

metapath2vec++(dmggmd).similarity:选择元路径为dmggmd得到的疾病之间的相似性。

metapath2vec++(dmgg-gggmd).similarity:合并元路径为dmggmd和dmgggmd得到的疾病之间的相似性。

similarity_dmg_dg.ggg:合并多条元路径在disease-miRNA-gene和disease-gene构造的综合网络中得到的疾病之间的相似性。

simple overlap.similarity：简单重叠计算得到的相似性。