import random
import string
from functools import singledispatch


"""
一般方法
"""


def removeDuplicate1(iterable):
    appeared = set()  # 记录出现的元素
    if isinstance(iterable, list):
        for value in iterable:
            if value not in appeared:
                appeared.add(value)
                yield value
    elif isinstance(iterable, dict):
        for key, value in iterable.items():
            if value not in appeared:
                appeared.add(value)
                yield key, value
    else:
        raise TypeError("Type must be list or dict")


"""
函数"重载"方法
"""


@singledispatch
def removeDuplicate2(other):
    print("调用other版本")
    raise TypeError("Type must be list or dict.")


@removeDuplicate2.register(list)
def _(ls: list):
    print("调用list版本")
    appeared = set()  # 记录出现的元素
    for value in ls:
        if value not in appeared:
            appeared.add(value)
            yield value


@removeDuplicate2.register(dict)
def _(dic):
    print("调用dict版本")
    appeared = set()  # 记录出现的元素
    for key, value in dic.items():
        if value not in appeared:
            appeared.add(value)
            yield key, value


if __name__ == "__main__":
    print("去除列表重复元素：")
    # 生成含有20个整数的列表
    int_ls: list = [random.randint(-10, 10) for i in range(20)]
    print("int_ls =", int_ls)
    print("使用removeDuplicate1函数，得到", list(removeDuplicate1(int_ls)))
    print("使用removeDuplicate2函数，得到", list(removeDuplicate2(int_ls)))

    # 生成含有20个大写字母的列表
    str_ls: list = random.choices(string.ascii_uppercase, k=20)
    print("\nstr_ls =", str_ls)
    print("使用removeDuplicate1函数，得到", list(removeDuplicate1(str_ls)))
    print("使用removeDuplicate2函数，得到", list(removeDuplicate2(str_ls)))

    print("\n去除字典重复元素：")
    keys: list = list(removeDuplicate1(str_ls))
    values: list = [random.randint(-10, 10) for i in range(len(keys))]
    d: dict = dict(zip(keys, values))
    print("d =", d)
    print("使用removeDuplicate1函数，得到", dict(removeDuplicate1(d)))
    print("使用removeDuplicate2函数，得到", dict(removeDuplicate2(d)))

    print("\n尝试去除元组重复元素：")
    gen = (random.randint(-10, 10) for i in range(20))
    t:tuple = tuple(gen)
    print("t =", t)
    try:
        print("使用removeDuplicate1函数，得到", tuple(removeDuplicate1(t)))
    except TypeError:
        print("参数类型不正确!")
    try:
        print("使用removeDuplicate2函数，得到", tuple(removeDuplicate2(t)), '\n')
    except TypeError:
        print("参数类型不正确!\n")
