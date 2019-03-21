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
19. 激活函数的比较
> 从晚7:30-8:30，面试官问了一个小时的问题，自己凭记忆想出上面的，都是一些基础的问题，不是刻意刁难。基础不牢，地动山摇，好好准备吧。

## 微软
1. xgboost分类节点的依据

如何计算每次分裂的收益呢？假设当前节点记为C,分裂之后左孩子节点记为L，右孩子节点记为R，则该分裂获得的收益定义为当前节点的目标函数值减去左右两个孩子节点的目标函数值之和：Gain=ObjC-ObjL-ObjR，具体地，根据目标函数值公式可得：
![](https://upload-images.jianshu.io/upload_images/1371984-d0a9c89dbbc34f7c.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/544/format/webp)

2. 信息增益vs信息增益比

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
