# -*- coding: utf-8 -*-
from matplotlib import font_manager
from lxml import etree
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
from pyecharts.charts import Pie


class FundShow(object):
    def __init__(self):
        self.tag = "FundShow"
        self.font = font_manager.FontProperties(fname="./font/breif.ttf")

    # 饼状图
    def pie(self,name, value, picname, tips):
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(name, value)],
                # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
                # 默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
                center=["35%", "50%"],
            )
                .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])  # 设置颜色
                .set_global_opts(
                title_opts=opts.TitleOpts(title="" + str(tips)),
                legend_opts=opts.LegendOpts(type_="scroll", pos_left="70%", orient="vertical"),  # 调整图例位置
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
                .render(str(picname) + ".html")
        )

    # 柱形图
    def bars(self, name, dict_values):
        # 链式调用
        c = (
            Bar(
                init_opts=opts.InitOpts(  # 初始配置项
                    theme=ThemeType.MACARONS,
                    animation_opts=opts.AnimationOpts(
                        animation_delay=1000, animation_easing="cubicOut"  # 初始动画延迟和缓动效果
                    ))
            )
                .add_xaxis(xaxis_data=name)  # x轴
                .add_yaxis(series_name="股票型", y_axis=dict_values['股票型'])  # y轴
                .add_yaxis(series_name="混合型", y_axis=dict_values['混合型'])  # y轴
                .add_yaxis(series_name="债券型", y_axis=dict_values['债券型'])  # y轴
                .add_yaxis(series_name="指数型", y_axis=dict_values['指数型'])  # y轴
                .add_yaxis(series_name="QDII型", y_axis=dict_values['QDII型'])  # y轴
                .set_global_opts(
                title_opts=opts.TitleOpts(title='涨跌幅', subtitle='绘制',  # 标题配置和调整位置
                                          title_textstyle_opts=opts.TextStyleOpts(
                                              font_family='SimHei', font_size=25, font_weight='bold', color='red',
                                          ), pos_left="90%", pos_top="10",
                                          ),
                xaxis_opts=opts.AxisOpts(name='阶段', axislabel_opts=opts.LabelOpts(rotate=45)),
                # 设置x名称和Label rotate解决标签名字过长使用
                yaxis_opts=opts.AxisOpts(name='涨跌点'),

            )
            .render("基金各个阶段涨跌幅.html")
        )

    # 拉伸图
    def silder(self, name, value, tips):
        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
                .add_xaxis(xaxis_data=name)
                .add_yaxis(tips, y_axis=value)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=str(tips) + "近30个交易日净值情况"),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            )
            .render(str(tips) + "近30个交易日净值情况.html")
        )
