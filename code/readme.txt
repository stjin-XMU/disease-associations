random_walk.py
随机游走代码，在异构网络中通过选定的元路径获得随机游走实例
输入：所用的关联网络
输出：随机游走实例

metapath2vec++ :
训练设置:
	-train <file>：用来自<file>文本数据去训练模型。
	-output <file>：用<file>保存得到的向量结果。
	-size <int>：设置向量尺寸，默认100。
	-window <int>：设置最大的skip长度，默认为5。
	-sample <float>：设置阈值。在训练数据中出现频率较高的那些将被随机采样; 默认值为0.001，有用范围为（0,0.00005）。
	-pp <int>：metapath2vec++，默认为1
	-negative <int>：负样本的数量，默认为5；常用值3-10，0不可用。
	-threads <int>：线程数量，默认为12。
	-iter <int>：运行训练的迭代次数，默认为5。
	-min-count <int>：丢弃出现小于<int>次的节点; 默认值为5
	-alpha <float>：设定起始学习率; skip-gram的默认值为0.025
例如cmd指令:
./metapath2vec -train input.txt -output ../output -pp 1 -size 128 -window 7 -negative 5 -threads 32
输入: 通过选定的元路径随机游走获得的实例数据。
输出：每个节点的多维向量数据。

cosine.py:
根据得到的多维向量计算疾病节点之间的相似性
输入：节点的多维向量数据。
输出：节点与节点之间的相似性数据表格。

其余的为一些对比，分析，画图的代码。

	


			



