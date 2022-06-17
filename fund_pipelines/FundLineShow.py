# -*- coding: utf-8 -*-
# 绘制多个条形图
import bar_chart_race as bcr
import pandas as pd
import matplotlib.pyplot as plt


class FundLineShow(object):
    def __init__(self):
        self.tag = "FundLineShow"

    def log(self, msg):
        print(self.tag, msg)
    # https://hanabi.data-viz.cn/visualisation/dynamic_bar_chart?lang=zh-CN
    def show(self, name):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号“-”显示为方块的问题
        # 获取数据
        df = pd.read_excel("{}.xlsx".format(name), index_col=0)
        # 生成动态流水线
        bcr.bar_chart_race(df=df,
                           filename='{}.mp4'.format(name),  # 生成的动态条形图的文件位置
                           orientation='h',  # h条形图 v柱状图
                           sort='desc',  # 降序，asc-升序
                           n_bars=10,  # 设置最多能显示的条目数
                           fixed_order=False,  # 设置固定类目
                           fixed_max=False,  # 固定数值轴，使其不发生动态变化 True-固定
                           steps_per_period=24,  # 图像帧数:数值越小，越不流畅,越大，越流畅
                           period_length=20,  # 设置帧率，单位时间默认为500ms 即为24帧的总时间是500ms
                           interpolate_period=False,
                           period_label={'x': .80, 'y': .5, 'ha': 'right', 'va': 'center', 'size': 16},  # 设置日期标签的时间格式
                           colors='dark12',  # 设置柱状图颜色颜色，通过在「_colormaps.py」文件中添加颜色信息，即可自定义配置颜色
                           title={'label': '指数型近一年日涨幅流水', 'size': 18, },  # 图表标题
                           bar_size=.95,  # 条形图高度
                           bar_textposition='inside',  # 条形图标签文字位置
                           bar_texttemplate='{x:,.0f}',  # 条形图标签文字格式
                           bar_label_font=16,  # 条形图标签文字大小
                           tick_label_font=16,  # 坐标轴标签文字大小
                           tick_template='{x:,.0f}',  # 坐标轴标签文字格式
                           shared_fontdict={'family': 'Microsoft YaHei', 'color': 'rebeccapurple'},  # 全局字体属性
                           scale='linear',
                           fig=None,
                           writer=None,
                           bar_kwargs={'alpha': .7},  # 条形图属性，可以设置透明度，边框等
                           fig_kwargs={'figsize': (16, 10), 'dpi': 144},  # figsize-设置画布大小，默认(6, 3.5)，dpi-图像分辨率，默认144
                           filter_column_colors=True,  # 去除条形图重复颜色，True去除,默认为False
                           )
        self.log("完成")
