## 1 TF-IDF

- **使用TF-IDF进行特征词的选取，将所有文章转化成特征词TF-IDF矩阵**
```text
vectorizer = TfidfVectorizer(max_df=0.95,max_features=20000, min_df=2, use_idf=True)
X = vectorizer.fit_transform(texts)
```
- **TF-IDF原理**

假设有一篇文章一共有100个词，其中“卫浴”、“九牧”分别出现了100和40次，那么它们的词频分别如下：

![](https://upload-images.jianshu.io/upload_images/1531909-c8eb8905df398eba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

假设语料库中一共有50篇文章，其中包含“卫浴”的文章有19篇，包含“九牧”的有9篇，那么它们的IDF计算如下:

![](https://upload-images.jianshu.io/upload_images/1531909-8e060aac00466ad9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

TF-IDF的计算结果如下：

![](https://upload-images.jianshu.io/upload_images/1531909-cadbc646b0c830b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- TF-IDF优缺点 

> TF-IDF的优点是简单快速，而且容易理解。缺点是有时候用词频来衡量文章中的一个词的重要性不够全面，有时候重要的词出现的可能不够多，而且这种计算无法体现位置信息，无法体现词在上下文的重要性。[reference：https://zhuanlan.zhihu.com/p/31197209]

## K-means

- **使用K-means进行文本聚类**

>k-means算法需要事先指定簇的个数k，算法开始随机选择k个记录点作为中心点，然后遍历整个数据集的各条记录，将每条记录归到离它最近的中心点所在的簇中，之后以各个簇的记录的均值中心点取代之前的中心点，然后不断迭代，直到收敛

![将点归类到与聚类中心距离最短的类别](https://upload-images.jianshu.io/upload_images/1531909-6cd52f756d2c0586.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![更新聚类中心](https://upload-images.jianshu.io/upload_images/1531909-6d2e7a974b5531f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- K-means优缺点

容易理解，而且有效，但是计算量比较大，耗费时间长，K的个数不好确定

## TextRank
提到TextRank，我们需要先从PageRank说起
- **PageRank**

PageRank，又称网页排名、谷歌左侧排名，是一种由搜索引擎根据网页之间相互的超链接计算的技术，而作为网页排名的要素之一，以Google公司创办人拉里·佩奇（Larry Page）之姓来命名。

假设一个由4个网页组成的群体：A，B，C和D。如果所有页面都只链接至A，那么A的PR（PageRank）值将是B，C及D的Pagerank总和。
![](https://wx2.sinaimg.cn/mw690/e59539f0ly1g1jhnsn7wxj208a07zt8q.jpg) 
计算公式如下：
![](https://www.quantinfo.com/attachment/article/20180728/1532762247287744613.png)

重新假设B链接到A和C，C只链接到A，并且D链接到全部其他的3个页面。一个页面总共只有一票。所以B给A和C每个页面半票。以同样的逻辑，D投出的票只有三分之一算到了A的PageRank上。
![](https://wx3.sinaimg.cn/mw690/e59539f0ly1g1jho6s18cj207u07swek.jpg)
计算公式如下：
![](https://www.quantinfo.com/attachment/article/20180728/1532762238832115527.png)
