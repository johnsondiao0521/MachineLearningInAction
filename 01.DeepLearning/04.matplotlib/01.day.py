#encoding:utf-8

from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

def test1():
    x = range(2,26,2)
    y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

    plt.figure(figsize=(20,8),dpi=80)
    _xtick_labels = [i / 2 for i in range(4, 49)]
    plt.xticks(_xtick_labels)
    plt.yticks(range(min(y), max(y) + 1))
    plt.plot(x,y)
    plt.show()

def test2():
    x = range(0, 120)
    y = [random.randint(20, 35) for i in range(120)]
    plt.figure(figsize=(20,9),dpi=90)
    _xtick_labels = ["10点{}分".format(i) for i in range(60)]
    _xtick_labels += ["11点{}分".format(i) for i in range(60)]
    plt.xticks(list(x)[::3], _xtick_labels[::3],fontproperties=my_font,rotation = 45)  # rotaion旋转的度数
    plt.xlabel("时间", fontproperties=my_font)
    plt.ylabel("温度 单位(℃)", fontproperties=my_font)
    plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)
    plt.plot(x,y)
    plt.show()

def test3():
    y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    x = range(11, 31)
    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(x, y)
    # 设置x轴刻度
    _xtick_labels = ["{}岁".format(i) for i in x]
    plt.xticks(x, _xtick_labels, fontproperties=my_font)
    plt.yticks(range(0, 9))
    # 绘制网格
    plt.grid(alpha=0.4)
    # 展示
    plt.show()

def test4():
    y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    x = range(11, 31)
    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(x, y_1, label="自己", color="#F08080")
    plt.plot(x, y_2, label="同桌", color="#DB7093", linestyle="--")
    # 设置x轴刻度
    _xtick_labels = ["{}岁".format(i) for i in x]
    plt.xticks(x, _xtick_labels, fontproperties=my_font)
    # 绘制网格
    plt.grid(alpha=0.4, linestyle=':')
    #添加图例
    plt.legend(prop=my_font,loc="upper left")
    # 展示
    plt.savefig("./tmp/test4.svg")
    plt.show()

if __name__ == '__main__':
    test4()


