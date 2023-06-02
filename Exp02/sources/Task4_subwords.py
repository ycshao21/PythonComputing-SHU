import os

def initSet():
    word_set = set()
    # 读取文件
    with open("../data/words.txt", 'r', encoding='utf-8') as fp:
        for word in fp.readlines():
            word = word.lower().strip()  # 转为小写并删去首尾空白字符
            if 'a' in word or 'i' in word:  # 可缩短单词必须包含字母a或i
                word_set.add(word)
    return word_set


def getSubwords(word, word_set):
    subwordSet = set()
    for i in range(len(word)):
        subword = word[:i] + word[i + 1:]  # 用切片去除一个字母
        if subword in word_set:
            subwordSet.add(subword)  # 保留有效子单词
    return subwordSet


def isShortenable(word, word_set):
    if word in resDict:
        return True
    shortables = set()  # word的所有可缩短子单词
    for subword in getSubwords(word, word_set):
        if isShortenable(subword, word_set):
            shortables.add(subword)
    if len(shortables) == 0:
        return False
    resDict[word] = shortables
    return True

def findShortenable(word_set):
    # 在所有单词中从短到长查找所有可缩短单词
    allShortables = list()
    for word in sorted(word_set):
        if isShortenable(word, word_set):
            allShortables.append(word)
    return sorted(allShortables, key=len, reverse=True)


def outputPath(word, path=""):
    if word in ('a', 'i'):
        return path + word + '\n'  # 路径终止
    output = ""
    for subword in resDict[word]:  # 遍历所有可缩短子路径
        output += outputPath(subword, path + f"{word} -> ")
    return output


wordSet = initSet()  # 获取所有可能的可缩短单词
resDict = {"": set(), "a": {""}, "i": {""}}  # 引入空字符串、a、i作为基准字符
shortableList = findShortenable(wordSet)  # 获取所有可缩短单词

longestWords = list()  # 统计最长可缩短单词
maxLength = len(shortableList[0])
out = ""  # 所有可缩短路径
for word in shortableList:
    out += outputPath(word)  # 输出可缩短路径
longestWords = list(filter(lambda x: len(x) == maxLength, shortableList))
print(f"最长可缩短单词长度为{maxLength}")
print("最长可缩短单词有", longestWords)

folder_path = "../outputs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
with open("../outputs/path.txt", 'w', encoding='utf-8') as fp:
    fp.write(out)
