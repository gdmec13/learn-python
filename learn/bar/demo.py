# -*- coding: utf-8 -*-
import numpy
import pandas as pd
import bar_chart_race as bcr
import matplotlib.pyplot as plt


# 设置字体，否则无法显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def demo1():
    """
    简单的示例
    动态条形图
    """
    df = pd.read_csv('./demo.csv', index_col=['date'])
    bcr.bar_chart_race(df, "demo.gif")


def demo2():
    """
    动态柱状图
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    bcr.bar_chart_race(df, "demo2.gif", orientation='v')


def demo3():
    """
    指定排序方式
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    # 设置排序方式
    bcr.bar_chart_race(df, "demo3.gif", sort='asc')


def demo4():
    """
    限制条目数
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    # 设置最多能显示的条目数，这里最多显示6条
    bcr.bar_chart_race(df, "demo4.gif", n_bars=1)


def demo5():
    """
    固定数值轴，使其不发生动态变化
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    # 设置数值的最大值，固定数据轴
    bcr.bar_chart_race(df, 'demo5.gif', fixed_max=True)


def demo6():
    """
    设置图像帧数，默认10帧
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    # 图像帧数：数值越小，越不流畅；越大，越流畅
    bcr.bar_chart_race(df, 'demo6.gif', steps_per_period=3)


def demo7():
    """
    设置帧率，单位时间默认为500ms
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    # 设置帧率为200ms，总共20帧
    bcr.bar_chart_race(df, 'demo7.gif', steps_per_period=20, period_length=200)


def demo8():
    """
    设置每帧增加的标签时间，默认为False
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    bcr.bar_chart_race(df, "demo8.gif", interpolate_period=True)


def demo9():
    """
    figsize:设置画布大小，默认(6,3.5)
    dpi:图像分辨率，默认144
    label_bars:显示柱状图的数值信息，默认为 True；
    指定为 False 则不显示；指定为字典，则自定义显示属性
    period_label:显示时间标签信息，默认为 True；
    指定为 False 则不显示；指定为字典，则自定义显示属性
    period_fmt:设置日期格式
    title:图表标题
    title_size:标题字体大小
    shared_fontdict:全局字体属性，例如
    {'family':'Helvetica','weight':'bold',
    'color':'rebeccapurple'}
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    bcr.bar_chart_race(df, "demo9.gif",
                       figsize=(5, 3),
                       dpi=100,
                       label_bars=False,
                       period_label={'x': .99, 'y': .1, 'ha': 'right', 'color': 'red'},
                       title="测试标题"
                       )


def demo10():
    """
    条形图属性，可以设置透明度，边框等
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    # bar_kwargs: 条形图属性
    bcr.bar_chart_race(df, "demo10.gif", bar_kwargs={"alpha": .2, 'ec': 'black', 'lw': 3})


def demo11():
    """
    添加动态文本
    """

    def summary(values, ranks):
        """
        动态文本的内容
        values为df的每一行（Series），例如
        Belgium1143.0
        China3326.0
        France6520.0
        Germany1275.0
        Iran3294.0
        Italy14681.0
        Netherlands1490.0
        Spain11198.0
        USA7418.0
        UnitedKingdom3611.0
        Name:2020-04-03,dtype:float64

        ranks则是针对values的值进行了排名，例如
        Belgium1.0
        China5.0
        France7.0
        Germany2.0
        Iran4.0
        Italy10.0
        Netherlands3.0
        Spain9.0
        USA8.0
        UnitedKingdom6.0
        Name:2020-04-03,dtype:float64
        """
        all_people = int(values.sum())
        ranks_country = ranks.sort_values().index
        s = (f'总英雄人数：{all_people}，'
             f'英雄人数最多的国家：{ranks_country[-1]}，'
             f'英雄人数最少的国家：{ranks_country[0]}')
        # 设置文本位置、数值、大小、颜色等
        return {'x': .99, 'y': .05, 's': s,
                'ha': 'right', 'size': 8}

    df = pd.read_csv('./demo.csv', index_col=['date'])
    # 添加文本
    bcr.bar_chart_race(df, 'demo11.gif', period_summary_func=summary)


def demo12():
    """
    添加垂直条 todo:未测试完
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])

    # 设置垂直条数值，分位数
    def func(values, ranks):
        return numpy.quantile(values, .9)

    # 添加垂直条
    bcr.bar_chart_race(df, 'demo12.gif', period_summary_func=func)


def demo13():
    """
    设置柱状图颜色
    """
    df = pd.read_csv('./demo.csv', index_col=["date"])
    bcr.bar_chart_race(df, 'demo13.gif', cmap="plotly3")


def list_all_color():
    """
    查看有哪些颜色，对应demo13
    """
    from bar_chart_race._colormaps import colormaps
    print(list(colormaps.keys()))


if __name__ == '__main__':
    list_all_color()
