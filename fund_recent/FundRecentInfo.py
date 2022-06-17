# -*- coding: utf-8 -*-
import json
import requests

from FundShow import FundShow


class FundRecentInfo(object):
    def __init__(self):
        self.tag = "FundRecentInfo"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }
        self.url = "https://danjuanapp.com/djapi/v3/filter/fund?type={}&order_by=1w&size=10&page=1"

        # 基金类型
        self.dict_type = {"股票型": 1, "混合型": 3, "债券型": 2, "指数型": 5, "QDII型": 11}
        # 时间 order_by
        self.dict_time = {'近一周': '1w', '近一月': '1m', '近三月': '3m', '近六月': '6m', '近1年': '1y',
                          '近2年': '2y', '近3年': '3y', '近5年': '5y'}

    def log(self, msg):
        print(self.tag, msg)

    # 分析1： 近一月涨跌幅前10名
    def start_request(self):
        for key in self.dict_type:
            request_url = self.url.format(str(self.dict_type[key]))
            # self.log("请求地址{}".format(request_url))
            res = requests.get(request_url, headers=self.headers)
            res.encoding = 'utf-8'
            s = json.loads(res.text)
            s = s['data']['items']
            name = []
            value = []
            for i in range(0, len(s)):
                name.append(s[i]['fd_name'])
                value.append(s[i]['yield'])
                self.log(s[i]['fd_name'] + ":" + s[i]['yield'])
            fund_show = FundShow()
            fund_show.pie(name, value, str(key) + "基金涨跌幅", "[" + str(key) + "]基金近一月涨跌幅前10名")

    # 分析2： 基金各个阶段涨跌幅
    def analysis2(self):
        name = ['近1周', '近1月', '近3月', '近6月', '近1年', '近3年', '近5年']
        ##五类基金
        dict_value = {}

        for key in self.dict_type:
            #### 获取排名第一名基金代号
            url = "https://danjuanapp.com/djapi/v3/filter/fund?type=" + str(
                self.dict_type[key]) + "&order_by=1w&size=10&page=1"
            res = requests.get(url, headers=self.headers)
            res.encoding = 'utf-8'
            s = json.loads(res.text)
            ###取第一名
            fd_code = s['data']['items'][0]['fd_code']

            #### 获取排名第一名基金各个阶段情况
            fu_url = "https://danjuanapp.com/djapi/fund/derived/" + str(fd_code)
            res = requests.get(fu_url, headers=self.headers)
            res.encoding = 'utf-8'
            s = json.loads(res.text)
            data = s['data']

            valuess = []

            # 防止基金最长时间不够1年、2年、5年的情况报错，用0填充
            # 近1周
            try:
                valuess.append(float(data['nav_grl1w']))
            except:
                valuess.append(0)
            # 近1月
            try:
                valuess.append(float(data['nav_grl1m']))
            except:
                valuess.append(0)
            # 近3月
            try:
                valuess.append(float(data['nav_grl3m']))
            except:
                valuess.append(0)
            # 近6月
            try:
                valuess.append(float(data['nav_grl6m']))
            except:
                valuess.append(0)
            # 近1年
            try:
                valuess.append(float(data['nav_grl1y']))
            except:
                valuess.append(0)
            # 近3年
            try:
                valuess.append(float(data['nav_grl3y']))
            except:
                valuess.append(0)
            # 近5年
            try:
                valuess.append(float(data['nav_grl5y']))
            except:
                valuess.append(0)
            # 添加到集合中
            dict_value[key] = valuess
        self.log(name)
        self.log(dict_value)
        fund_show = FundShow()
        fund_show.bars(name, dict_value)

    # 分析3： 近30个交易日净值情况
    def analysis3(self):
        for key in self.dict_type:
            # 获取排名第一名基金代号
            url = "https://danjuanapp.com/djapi/v3/filter/fund?type=" + str(
                self.dict_type[key]) + "&order_by=1w&size=10&page=1"
            res = requests.get(url, headers=self.headers)
            res.encoding = 'utf-8'
            s = json.loads(res.text)
            # 取第一名
            fd_code = s['data']['items'][0]['fd_code']

            # 获取排名第一名基金近30个交易日净值情况
            fu_url = "https://danjuanapp.com/djapi/fund/nav/history/" + str(fd_code) + "?size=30&page=1"
            res = requests.get(fu_url, headers=self.headers)
            res.encoding = 'utf-8'
            s = json.loads(res.text)
            data = s['data']['items']
            name = []
            value = []
            for k in range(0, len(data)):
                name.append(data[k]['date'])
                value.append(data[k]['nav'])
            fund_show = FundShow()
            fund_show.silder(name, value, key)


if __name__ == '__main__':
    fund_info = FundRecentInfo()
    #fund_info.start_request()
    # fund_info.analysis2()
    fund_info.analysis3()
