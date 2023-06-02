import re
import random


class Markov:
    def __init__(self, filepath: str):
        self.__prefixDict = dict()  # 前缀字典
        self.__beginWords = list()  # 句首列表
        # 读取文本
        with open(filepath, 'r', encoding='utf-8') as fp:
            text = fp.read()
        # 划分句子
        punc = re.compile(r"[\"#$%&'()*+\-/<=>@\[\]^_`{|}~]")
        text = punc.sub('', text)
        text = re.sub(r'[\n\r]', ' ', text)
        sentences: list = re.split(r'[.!?:;]', text)
        # 按空格划分各句单词
        self.__sentence_words = list()
        for sentence in sentences:
            self.__sentence_words.append(list(filter(lambda x: x != '', sentence.split(" "))))

    def train(self, n: int):
        self.__prefixDict = dict()  # 前缀字典
        self.__beginWords = list()  # 句首列表
        # 生成字典
        for words in self.__sentence_words:
            for i in range(len(words) - n):
                # 获取前缀
                key = words[i]
                for j in range(1, n):
                    if i + j + 1 >= len(words): break
                    key += " " + words[i + j]
                # 将首字母为大写的前缀作为句首
                if key[0].isupper():
                    self.__beginWords.append(key)
                # 其余前缀存入字典
                if key not in self.__prefixDict:
                    self.__prefixDict[key] = [words[i + n]]
                else:
                    self.__prefixDict[key].append(words[i + n])

    def generate(self, m: int):
        sentence = ""
        for i in range(m):
            # 随机选择句首
            key = self.__beginWords[random.randint(0, len(self.__beginWords) - 1)]
            sentence += key
            while True:
                if key not in self.__prefixDict:
                    sentence += ". "
                    break
                nextWord = self.__prefixDict[key][random.randint(0, len(self.__prefixDict[key]) - 1)]
                # 更新前缀
                if len(key.split()) > 1:
                    key = " ".join(key.split()[1:]) + " " + nextWord
                else:
                    key = nextWord
                # 若不存在该前缀，则结束
                sentence += " " + nextWord
        return sentence

    @ property
    def dictLen(self):
        return len(self.__prefixDict)


if __name__ == '__main__':
    markov = Markov("../../data/emma.txt")
    for n in (1, 2, 3, 4, 5, 10, 15, 20, 30, 50):
        markov.train(n)
        print(f"{n}阶马尔可夫模型训练结果：")
        print(f"字典长度：{markov.dictLen}")
        print(f"生成文本：{markov.generate(1)}\n")  # 生成一句话
