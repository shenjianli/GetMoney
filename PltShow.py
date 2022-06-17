# -*- coding: utf-8 -*-
# 绘制多个条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager


class PltShow(object):
    def __init__(self):
        self.tag = "plt_show"
        self.font = font_manager.FontProperties(fname="./font/breif.ttf")

    # 4.月差值(月末减月初，该月是否盈亏）
    def analysis4(self, x, y):
        # 设置图形大小
        plt.figure(figsize=(20, 8), dpi=80)
        plt.plot(x, y, label="月末-月初")

        # 设置图例
        plt.legend(prop=self.font)
        plt.xlabel("月份", fontproperties=self.font)
        plt.ylabel("值", fontproperties=self.font)
        plt.savefig("./image/mutiy_4.png")
        plt.show()

    # 3.当月波动值（最高涨、最低跌之差）
    def analysis3(self, x, y1, y2):
        a = x
        y = []
        for i in range(0, len(y1)):
            y.append(float(y1[i] - y2[i]))
        # 设置图形大小
        plt.figure(figsize=(20, 8), dpi=80)
        plt.plot(a, y, label="波动差值")

        # 设置图例
        plt.legend(prop=self.font)
        plt.xlabel("月份", fontproperties=self.font)
        plt.ylabel("值", fontproperties=self.font)
        plt.savefig("./image/mutiy_3.png")
        plt.show()

    # 2.当月最高涨、最低跌
    def analysis2(self, x, y1, y2):
        a = x
        b_14 = y1
        b_15 = y2

        bar_width = 0.25
        x_14 = list(range(len(a)))
        x_15 = list(i + bar_width for i in x_14)

        # 设置图形大小
        plt.figure(figsize=(20, 8), dpi=80)
        plt.bar(range(len(a)), b_14, width=bar_width, label="当月最高涨")
        plt.bar(x_15, b_15, width=bar_width, label="当月最低跌")

        # 设置图例
        plt.legend(prop=self.font)
        #
        plt.xlabel("月份", fontproperties=self.font)
        plt.ylabel("值", fontproperties=self.font)
        # 设置x轴刻度
        plt.xticks(x_15, a, fontproperties=self.font)
        plt.savefig("./image/mutiy_2.png")
        plt.show()

    ###1.月初、月末
    def analysis1(self, x, y1, y2):
        a = x
        b_14 = y1
        b_15 = y2

        bar_width = 0.25
        x_14 = list(range(len(a)))
        x_15 = list(i + bar_width for i in x_14)

        # 设置图形大小
        plt.figure(figsize=(20, 8), dpi=80)
        plt.bar(range(len(a)), b_14, width=bar_width, label="月初")
        plt.bar(x_15, b_15, width=bar_width, label="月末")

        # 设置图例
        plt.legend(prop=self.font)
        #
        plt.xlabel("月份", fontproperties=self.font)
        plt.ylabel("值", fontproperties=self.font)
        # 设置x轴刻度
        plt.xticks(x_15, a, fontproperties=self.font)
        plt.savefig("./image/mutiy_1.png")
        plt.show()