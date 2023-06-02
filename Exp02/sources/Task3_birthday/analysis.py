import matplotlib.pyplot as plt
from birthday import count_same_birthday


def draw_curve():
    # 生成p值矩阵
    m_tuple = (1000, 2000, 5000, 10000, 15000, 20000)
    n_tuple = (10, 20, 30, 40, 50, 80, 100, 120)
    p_mat = list()
    for m in m_tuple:
        row = list()
        for n in n_tuple:
            q = count_same_birthday(m, n)
            row.append(q / m)
        p_mat.append(row)

    # 绘制P-N图
    color = ('red', 'magenta', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple')
    for i in range(len(m_tuple)):
        plt.plot(n_tuple, p_mat[i], color=color[i], label=f'M={m_tuple[i]}')
    plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置字体
    plt.grid()  # 显示网格
    plt.legend(loc='lower right')  # 在右下角显示图例
    plt.xlabel("N", fontsize=16)
    plt.ylabel("P", fontsize=16)
    plt.show(block=True)


def draw_dot():
    m_list = tuple(range(1000, 40000, 1000))
    n_tuple = (23, 60)

    for i in range(len(n_tuple)):
        p_mat = list()
        for m in m_list:
            p_row = list()
            # 对每个m生成6个p值
            for j in range(6):
                p_row.append(count_same_birthday(m, n_tuple[i]) / m)
            p_mat.append(p_row)

        ax = plt.subplot(1, 2, i + 1)  # 创建子图并设定位置
        plt.sca(ax)  # 选择当前子图
        # 按行遍历pMat，绘制散点图
        for j in range(len(m_list)):
            ax.scatter([m_list[j]] * 6, p_mat[j], color='red')
        plt.grid()  # 显示网格
        plt.xlabel("M", fontsize=16)
        plt.ylabel("P", fontsize=16)

    plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置字体
    plt.show(block=True)


if __name__ == '__main__':
    draw_curve()
    draw_dot()
