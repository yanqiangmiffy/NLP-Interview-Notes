# NLP-Interview-Notes
专门为自然语言处理(NLP)面试准备的学习笔记与资料

## 招职位/投简历
1. 学校BBS

> 力推`北大未名`、`水木社区`,:这里面一般是学长或者学姐发布的内推职位，一般回复较快，但是你面对的竞争也很大（清北的学子们）

2. 招聘网站

> `BOSS直聘`、`实习僧`:有些岗位是重合的，信息较新，BOSS直聘回复较快

3. 互联网公司官网

> 一般春招和秋招的时候可以集中关注下

## 蚂蚁金服-NLP内推面试
1. 简单自我介绍
2. 详细讲解下自己做过的一个项目（最熟悉的）
3. 解释下泛化，处理方法
4. bagging和boosting的原理以及区别
> 二者都是集成学习算法，都是将多个弱学习器组合成强学习器的方法。

> Bagging：从原始数据集中每一轮有放回地抽取训练集，训练得到k个弱学习器，将这k个弱学习器以投票的方式得到最终的分类结果。

> Boosting：每一轮根据上一轮的分类结果动态调整每个样本在分类器中的权重，训练得到k个弱分类器，他们都有各自的权重，通过加权组合的方式得到最终的分类结果。

5. 深度学习的过拟合欠拟合和解决方法
6. epoch和batch的原理
7. 调整learning rate的依据
8. xgboost和lightgbm的联系与区别
9. 孪生网络的原理
10. LDA的原理
11. CRF
12. 命名实体识别的原理BILSTM-CRF
13. 结巴词性标注的原理
14. 深度学习流行或者普及的原因
15. 在样本数据很少的情况下（不是样本不均衡），应该怎么做
16. 你有什么想问的？想了解的
17. L1和L2正则化
18. Dropout
> 防止过拟合。每次训练，都对每个神经网络单元，按一定概率临时丢弃。
19. 激活函数的比较
> 从晚7:30-8:30，面试官问了一个小时的问题，自己凭记忆想出上面的，都是一些基础的问题，不是刻意刁难。基础不牢，地动山摇，好好准备吧。

## 微软 DKI小组
> 刚开始一个开放型编程题，二选一；第一题是给定了数据集，然后要求做二分类，评价指标AUC；第二题是自我介绍+前端或者后端二选一，一天内完成，我选择了第一题，auc达到0.8269。

1. xgboost分类节点的依据

>如何计算每次分裂的收益呢？假设当前节点记为C,分裂之后左孩子节点记为L，右孩子节点记为R，则该分裂获得的收益定义为当前节点的目标函数值减去左右两个孩子节点的目标函数值之和：`Gain=ObjC-ObjL-ObjR`，具体地，根据目标函数值公式可得：
![](https://upload-images.jianshu.io/upload_images/1371984-d0a9c89dbbc34f7c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/544/format/webp)

2. 信息增益vs信息增益比
3. HMM原理
4. LDA原理
5. LSTM网络结构图
6. 二叉树层次遍历
7. 青蛙上楼梯
8. 快速排序
9. 项目（中间考虑项目是否存在缺陷，比较细节，这一块很重要）
10. 余弦距离、曼哈顿距离公式
11. SQL取第50条到第100条数据
12. pandas取最后三列的方法
13. TextRank原理

## 微软小冰NLP组面试
1. 反转单词
2. 最长公共子串
3. 二叉树层次遍历变型
4. 手写KNN
5. 列举神经网络以及用处和场景；RNN自动翻译，怎么处理输入与输出长度不同的情况
6. 还有一个矩阵题（太长了，四五行，题意读不懂）
7. AI自动写作系统设计写出思路，没有代码

## 联想面试
1. CNN的3大优点

>CNN的三个优点：sparse interaction(稀疏的交互)，parameter sharing(参数共享)，equivalent respresentation(等价表示)。适合于自动问答系统中的答案选择模型的训练。
2. RNN、LSTM、DNN、CNN比较
3. LR的损失函数
4. 常见激活函数的比较
5. SVM 支持向量到直线的距离公式
6. 常见核函数有哪些
7. 剪枝策略
## 联想研究员自然语言处理实习生
面试小组是做联想智能问答的，然后主要题目如下：
1. 数据预处理方法
2. TensorFlow实现基本运算
3. sgd原理、是否收敛
4. cnn卷积作用、参数共享怎么回事
> 所谓的权值共享就是说，用一个卷积核去卷积一张图，这张图每个位置是被同样数值的卷积核操作的，权重是一样的，也就是参数共享。

5. 池化和池化作用
> 减小图像尺寸即数据降维，缓解过拟合，保持一定程度的旋转和平移不变性。
6. batchsize选择的依据
> 较大Batch Size：1、 提高了内存的利用率，大矩阵乘法的并行化效率提高；2、 运行一次epoch所需要的迭代次数减少，相同数据量的数据处理速度加快；3、 Batch_Size越大下降方向越准，引起的训练震荡越小。但是每次迭代耗时更长。

> 较小Batch Size：Batch_Size不宜选的太小，太小了容易修正方向导致不收敛，或者需要经过很大的epoch才能收敛；
7. attention机制

> 深度学习中的注意力机制从本质上讲和人类的选择性视觉注意力机制类似，核心目标是从大量信息中有选择地筛选出少量重要信息并聚焦到这些重要信息上，忽略大多不重要的信息。目前在神经机器翻译(Neural Machine Translation)、图像理解(Image caption)等场景都有广泛应用。

8. word2vec

9. knn、贝叶斯、svm，kmeans、pca

10. 编程题统计100w词频

11. 1亿个数排序，查找

12. 开放性题目：如何实现问题检索

13. 编辑距离

14. python2.7和python3的区别

15. 梯度爆炸和梯度消失出现的原因以及解决方法

> 针对梯度爆炸问题，解决方案是引入Gradient Clipping(梯度裁剪)。通过Gradient Clipping，将梯度约束在一个范围内，这样不会使得梯度过大。


> 梯度消失：在反向传播算法计算每一层的误差项的时候，需要乘以本层激活函数的导数值，如果导数值接近于0，则多次乘积之后误差项会趋向于0，而参数的梯度值通过误差项计算，这会导致参数的梯度值接近于0，无法用梯度下降法来有效的更新参数的值。改进激活函数，选用更不容易饱和的函数，如ReLU函数。

    
## 百度在线笔试

1. 数字0-9，每个数字的使用次数大于等于0，输入数A的位数，数B的位数，求A和B乘积的最小值
```

# cnts=[1,3,0,0,0,0,0,0,0,1]

# A=2;B=2


# cnts=[2,3,0,0,0,0,0,0,0,1]
cnts=[2,3,0,0,0,0,0,0,0,1]
A=1;B=1
def findMinFac(cnts,A,B):
    nums=[0,1,2,3,4,5,6,7,8,9]
    num_cnt=dict(zip(nums,cnts))
    if A<=B:
        A,B=B,A
    aval=0
    for num in num_cnt:
        while num_cnt[num]>0 and A>0:
            aval=aval+10**(A-1)*num
            num_cnt[num]-=1
            A-=1
            # print("A:",A,"aval",aval)    

    bval=0
    for num in num_cnt:
        while num_cnt[num]>0 and B>0:
            bval=bval+10**(B-1)*num
            num_cnt[num]-=1
            B-=1
            # print("B:",B,"aval",bval)
    return aval*bval
print(findMinFac(cnts,A,B))

```
## 香侬科技 NLP算法实习生
1. 如果模型在训练结果表现很好，在测试集表现很差的原因有哪些
    > 比如在测试集的准确率为90%，在测试集的准确率为10%
2. Dropout(p)的理解，随着p的增加，模型的性能会是怎样的表现
3. 假如随着p的增加，模型的性能一直在下降，还有哪些原因
4. 给定一个实数列表nums和一个数key，寻找在nums离key最近的n个数
5. 动态规划：给定一个词典dictionary，实现分词：
    > 词语长度最大;最少分词次数

## 神州泰岳
- 连续子数组乘积最大
- 连续子数组求和最大
- 连续最长的无重复子串
- Dropout
- Attention，Self Attention
- seq2seq如何解决不等长问题
    >通过一些标志填充
- 未登录如何解决：增量学习，word2vec重新训练
- FastText的sub-word
- CNN
- RNN,LSTM的结构

## 猿辅导
- 简历项目
- 算法题
    > https://leetcode.com/problems/add-two-numbers/

## 阿里巴巴-本地生活
- Doc2Vec与word2vec的区别
- 如何使用别人的pretrained embedding进行fine-tuning

## 其他公司面试
1. 堆排序和快速排序
2. 贝叶斯原理和推理过程
3. 青蛙上楼梯 动态规划
4. 最短路径问题
5. RNN的前向和后向传播
6. 三层全连接网络的模拟过程
7. [基于矩阵分解的推荐算法](https://www.jianshu.com/p/812234c0da87)
8. [最大似然估计与贝叶斯估计的区别](https://www.jianshu.com/p/ead99acd6437)
9. 如何在embedding层之前实现两个句子向量交互


## 算法刷题
1. 《剑指Offer》
2. Leetcode
3. 牛客网

## 面试技巧
1. 掌握一门基础语言（c++或者java），尤其大厂很注重这一点
2. 发散性思维
## 相关资料
- [机器学习算法岗面试与提问总结](https://zhuanlan.zhihu.com/p/58434325?utm_source=wechat_session&utm_medium=social&s_r=0#showWechatShareTip)
- [精选Python面试100题](https://mp.weixin.qq.com/s/uPvzonBTGYLqF7PO3hZ8cg)
- [知识点 | 关于机器学习的超全总结](http://wemedia.ifeng.com/86075044/wemedia.shtml)
- [生成模型学习笔记：从高斯判别分析到朴素贝叶斯](https://www.jiqizhixin.com/articles/2018-12-24-13?from=synced&keyword=%E6%9D%A1%E4%BB%B6%E6%A6%82%E7%8E%87%E5%88%86%E5%B8%83)
- [专栏 | Bi-LSTM+CRF在文本序列标注中的应用](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650735630&idx=4&sn=726c61346d436edb69963dd88cc35a41)
- [机器学习与深度学习常见面试题（上）](https://mp.weixin.qq.com/s/e8rlmjNp9solM3ZJXsioaA)