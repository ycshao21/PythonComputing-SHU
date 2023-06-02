from collections import defaultdict
import os
import re

textPath = "../data/WilliamShakespeare.txt"
outputPath = "../outputs/word_count.txt"

folder_path = "../outputs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open(textPath, 'r', encoding='utf-8') as fp:
    text = fp.read()

# 用正则表达式提取单词
wordList = re.findall(r'\b[^\d\W]+\b', text.lower())
wordDict = defaultdict(int)  # 值默认为0
for word in wordList:
    wordDict[word] += 1

with open(outputPath, 'w', encoding='utf-8') as fp:
    # 按出现次数降序排列，若次数相同则按单词字典序升序排列
    for key, value in sorted(wordDict.items(), key=lambda x: (-x[1], x[0])):
        fp.write(key + ": " + str(value) + '\n')
