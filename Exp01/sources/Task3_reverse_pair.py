import os
import time


def solution1(wordSet):  # 用字典存放反向对
    start = time.time()
    revWordDict = dict()  # 存放反向对的字典
    for word in wordSet:
        # 若存在反向单词且字典没有记录，则将该反向对存入字典
        if (word[::-1] in wordSet) and (word[::-1] not in revWordDict):
            revWordDict[word] = word[::-1]

    # 将反向对写入reversed_dict.txt
    with open("../outputs/reversed_dict.txt", 'w', encoding='utf-8') as fp:
        for key, value in sorted(revWordDict.items()):
            fp.write(key + ": " + value + "\n")
    end = time.time()

    print("Dictionary")
    print("Number of reverse-pair:", len(revWordDict))
    print("Time required:", end - start)


def solution2(wordSet):  # 用集合存放
    start = time.time()
    revWordSet = set()  # 可反向集合
    for word in wordSet:
        # If the reversed word is in the set but not recorded in the set,
        # 若存在反向单词且集合没有记录，则将原词存入集合
        if (word[::-1] in wordSet) and (word[::-1] not in revWordSet):
            revWordSet.add(word)

    # 将反向对写入reversed_set.txt
    with open("../outputs/reversed_set.txt", 'w', encoding='utf-8') as fp:
        for word in sorted(revWordSet):
            fp.write(word + ": " + word[::-1] + '\n')
    end = time.time()

    print("\nSet")
    print("Number of reverse-pair:", len(revWordSet))
    print("Time required:", end - start)


if __name__ == '__main__':
    folder_path = "../outputs"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open("../data/words.txt", 'r', encoding='utf-8') as fp:
        wordSet = set(fp.read().splitlines())
    solution1(wordSet)
    solution2(wordSet)
