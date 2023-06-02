import os
import re

folder_path = "../../outputs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def rotateword(strsrc: str, n: int) -> str:
    """
    将strsrc中各个字母在字母表中轮转n个字符
    """
    if not isinstance(strsrc, str) or not isinstance(n, int):
        raise TypeError
    strdes: str = ""
    pattern = re.compile(r'[a-zA-Z]')
    for i in strsrc:
        if pattern.match(i) is not None:  # 当前字符为英文字母，则轮转n位
            if i.isupper():
                strdes += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            else:
                strdes += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:  # 当前字符为非英文字母，则不变
            strdes += i
    return strdes


def avoids(word: str, prohibit: str) -> bool:
    """
    判断该单词是否含有禁止字母
    """
    if not isinstance(word, str) or not isinstance(prohibit, str):
        raise TypeError
    # 在word中查找prohibit中的字符，若存在则说明含有禁止字母
    pattern = re.compile(f"[{prohibit}]")
    return bool(pattern.search(word) is not None)


def useonly(word: str, allow: str) -> bool:
    """
    判断该单词是否仅仅由允许字母组成
    """
    if not isinstance(word, str) or not isinstance(allow, str):
        raise TypeError
    # 在word中查找allow之外的字符，若不存在则说明仅由允许字母组成
    pattern = re.compile(f"[^{allow}]")
    return bool(pattern.search(word) is None)


def useall(word: str, require: str) -> bool:
    """
    判断该单词是否包含了所有需要字母至少一个
    """
    if not isinstance(word, str) or not isinstance(require, str):
        raise TypeError
    # 在require中匹配所有word中的字符，若匹配个数与require长度相同则说明包含了所有需要字母至少一个
    pattern = re.compile(f"[{word}]")
    return len(pattern.findall(require)) == len(require)


def hasnoe(word: str) -> bool:
    """
    判断一个英语单词是否包含字母e
    """
    if not isinstance(word, str):
        raise TypeError
    # 在word中查找e或E，若不存在则说明不包含字母e
    pattern = re.compile(r"[eE]")
    return bool(pattern.search(word) is None)


def isabecedarian(word: str) -> bool:
    """
    判断一个英语单词中的字母是否符合字母表序
    """
    if not isinstance(word, str):
        raise TypeError
    reg = "^"
    for asc in range(ord('a'), ord('z') + 1):
        reg += f"({chr(asc)}|{chr(asc - ord('a') + ord('A'))})*"
    reg += "$"
    pattern = re.compile(reg)
    return bool(pattern.match(word) is not None)


def test():
    s = "Hello, my name is Matthew!"
    print("1. rotateword测试")
    print(rotateword(s, -2))
    print(rotateword(s, 35))

    print("\n2. avoids测试")
    print(avoids(s, "cju"))
    print(avoids(s, "meet"))

    print("\n3. useonly测试")
    w = "Beautiful"
    print(useonly(w, "abBefiltuw"))
    print(useonly(w, "aBju"))

    print("\n4. useall测试")
    print(useall(w, "abBefiltuw"))
    print(useall(w, "tea"))
    print(useall(w, "tcha"))

    print("\n5. hasnoe测试")
    print(hasnoe("beautiful"))
    print(hasnoe("hatE"))
    print(hasnoe("your"))

    print("\n6. isabecedarian测试")
    print(isabecedarian("aBdeHlSt"))
    print(isabecedarian("aaaaaaA"))
    print(isabecedarian("uFed"))


def useall_test():
    res = ""
    cnt = 0
    with open("../../data/words.txt") as fp:
        for word in fp:
            word = word.strip()
            if useall(word, "aeiou"):
                res += f"{word} "
                cnt += 1
    with open("../../outputs/useall.txt", "w") as fp:
        fp.write(res)
    print(f"\nwords.txt中使用了所有元音字母aeiou的单词共有{cnt}个")


def hasnoe_test():
    res = ""
    total_cnt = 0
    noe_cnt = 0
    with open("../../data/words.txt") as fp:
        for word in fp:
            total_cnt += 1
            word = word.strip()
            if hasnoe(word):
                res += f"{word} "
                noe_cnt += 1
    with open("../../outputs/hasnoe.txt", "w") as fp:
        fp.write(res)
    print(f"\nwords.txt中不含e的单词共有{noe_cnt}个，在整个字母表中的百分比为{noe_cnt / total_cnt * 100:.2f}%")


def isabecedarian_test():
    res = ""
    cnt = 0
    with open("../../data/words.txt") as fp:
        for word in fp:
            word = word.strip()
            if isabecedarian(word):
                res += f"{word} "
                cnt += 1
    with open("../../outputs/isabecedarian.txt", "w") as fp:
        fp.write(res)
    print(f"\nwords.txt中字母表序的单词共有{cnt}个")


if __name__ == '__main__':
    # test()
    useall_test()
    hasnoe_test()
    isabecedarian_test()
