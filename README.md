# PythonComputing-SHU
如果你是一名上大计院学生，还在考虑选择什么选修课的话，那《Python计算》一定是一门超值的课程。  
3学分就可以拥有**3次统一实验**+**1次主题研讨**+**1次个人实验**，最后还附赠一场**期末考试**。如果你厌倦了“小组验收+小组报告”的实验模式，那这门课程就能带给你“**小组验收+个人报告**”的全新体验，这样的课谁能不爱呢？  

下面的内容仅包含要求写入报告的实验，大多为设计性实验，实验三包含了部分验证性实验。
***

## 实验一
1. Task1_polygon.py：绘制一条蛇。  
   运行需要安装**swampy**模块。
2. Task2_one_second_later.py：两种计算1秒后时间的方法。  
3. Task3_reverse_pair.py：找出word.txt中词汇表包含的反向对，提供了用字典和集合两种存储方法，并进行了效率对比，将反向对分别写入reversed_dict.txt和reversed_set.txt。  

4. Task4_word_count.py：统计文本中各单词出现的次数，结果写入word_count.txt。  
   Task4_keyword_count.py：统计文本中给定关键词的出现频率，结果写入keyword_count.txt。  
   测试文本存放于WilliamShakespeare.txt，内容为William Shakespeare的维基百科简介。  
   指定关键词存放于keywords.txt，采用了大小写混用的拼写方式。

## 实验二
1. Task1_pi.py：用拉马努金圆周率公式逼近圆周率，精确到小数点后15位，并和math.pi的值做比较。  
   solution1和solution1_better的解法是当计算值与理论值的差值小于3e-16时停止计算，后者在前者的基础上改用decimal对象计算，保证更高的精度；solution2则是使用sympy库直接进行符号运算，避免了中间过程带来的损失。

2. Task2_koch.py：绘制Quadratic type 2 curve雪花。  
运行需要安装**swampy**模块。

3. Task3_birthday  
   * birthday.py：对于各有N名学生的M个班级，计算每个班级中有相同生日的概率。  
   * analysis.py：绘制P-N曲线和P-M散点图，计算要等待一些时间。  
运行需要安装**matplotlib**模块。  

4. Task4_subwords.py：统计words.txt中的最长可缩短单词，并将所有可缩短单词的缩短路径写入path.txt。  
   程序使用递归算法，需要事先向words.txt中加上a和i两个单词。  

## 实验三
### 验证性实验
1. Task6_grid_for_py3.py：将grid.py修改成能在Python3.x下运行的代码，并绘制函数调用图，保存为grid_2.png和grid_4.png。  
运行需要安装**graphviz**和**pycallgraph2**模块。  

2. Task8_Kangaroo.py：修正Kangaroo.py的构造方法中的bug。

### 设计性实验
1. Task1
   * ackermann.py：两种计算Ackermann函数的方式
   * remove_duplicate.py：移除列表或字典重复项，提供了单个函数实现和重载函数实现

2. Task2_time  
Time.py和Time_better.py：实现Time类，但前者为了迎合题目要求的is_valid方法而没有在构造时检查参数合法性，导致其他方法中都需要调用is_valid方法；后者则是去掉了is_valid方法，用更合乎准则的方式重新设计了类。

3. Task3_markov：用emma.txt构造n阶马尔可夫链生成文本。data文件夹中还有whitefang.txt可供训练。
   
4. Task4_order
   * Lunch.py：订餐管理类  
   * Customer.py：顾客类  
   * Employee.py：商户类
   * Food.py：食物类
   * main.py：交互界面  
   这题做得不是很好，有什么改进建议欢迎提出。

5. Task5_regular_expressions.py：用正则表达式处理字符串  
useall、hasnoe和isabecedarian函数的测试结果分别保存为useall.txt、hasnoe.txt和isabecedarian.txt。

## 个人实验
我的选题是手写字符识别，可以识别手写的0-9、A-Z和a-z，内附*介绍视频*。  
数据集为English Handwritten Characters，神经网络模型为ResNet34，在测试集（10%）上的准确率约为80%。  

### 文件介绍
* load_dataset.py：加载数据集，按8:1:1划分训练集、验证集和测试集。
* mymodel.py：ResNet34模型
* train.py：训练模型
* draw_plot.py：绘制训练过程中的loss和accuracy曲线图
* predict.py：交互界面预测手写字符

### 运行方法
1. 从 https://www.kaggle.com/datasets/dhruvildave/english-handwritten-characters-dataset 下载数据集，将压缩包中的两个文件放在PersonalExp/dataset/路径下。

2. 安装以下模块
    * pytorch
    * opencv
    * numpy
    * scikit-learn
    * pillow
    * pandas
    * matplotlib
    * tqdm
    * tk

3. 运行train.py训练模型，可通过test参数设置是否跑训练集，可通过show_plot参数设置是否显示loss和accuracy曲线图

4. 运行predict.py打开界面，在左侧区域绘图，按下“识别”按钮识别字符，在右上方显示结果，按下“清除”可清空画布。

### 可改进方面
* 数据集太小，也没有做数据增强，拟合效果不好
* 没有对图像做预处理，可以将有效部分裁剪到中心
* 只能识别单个字符，不能识别一段文字
* predict.py中的代码结构很乱
* 界面太丑
* 第一次按下“识别”按钮也很慢
