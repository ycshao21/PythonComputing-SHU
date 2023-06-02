import os
import re

textPath = "../data/WilliamShakespeare.txt"
keywordPath = "../data/keywords.txt"
outputPath = "../outputs/keyword_count.txt"

folder_path = "../outputs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 从keywords.txt中读取关键词并存入字典
keywordDict = dict()
with open(keywordPath, 'r', encoding='utf-8') as fp:
    for keyword in fp:
        keyword = keyword.strip()
        keyword = keyword.lower()
        keywordDict[keyword] = 0

with open(textPath, 'r', encoding='utf-8') as fp:
    text = fp.read()

# 用正则表达式提取单词
wordList = re.findall(r'\b[^\d\W]+\b', text.lower())

# 统计关键词出现次数
for word in wordList:
    if word in keywordDict:
        keywordDict[word] += 1

with open(outputPath, 'w', encoding='utf-8') as fp:
    # 按出现次数降序排列，若次数相同则按单词字典序升序排列
    for key, value in sorted(keywordDict.items(), key=lambda x: (-x[1], x[0])):
        fp.write(key + ": " + str(value / len(wordList)) + '\n')
