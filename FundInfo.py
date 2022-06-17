# -*- coding: utf-8 -*-
import json
import requests

from PltShow import PltShow


class FundInfo(object):
    def __init__(self):
        self.tag = "FundInfo"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }
        self.url = "https://danjuanapp.com/djapi/fund/nav/history/{}?size={}&page=1"

    def log(self, msg):
        print(self.tag, msg)

    def start_request(self, code, size):
        request_url = self.url.format(code, size)
        res = requests.get(request_url, headers=self.headers)
        res.encoding = 'utf-8'
        s = json.loads(res.text)
        s = s['data']['items']
        f = ((s[len(s) - 1]['date']).split("-"))[1]

        for j in range(len(s) - 1, -1, -1):
            i = s[j]
            m = (i['date'].split("-"))
            if m[1] == f:
                try:
                    date = i['date']
                    percentage = i['percentage']
                    value = i['value']
                    print("date=" + str(date) + ",percentage=" + str(percentage) + ",value=" + str(value))
                except:
                    pass
            else:
                f = m[1]
                try:
                    date = i['date']
                    percentage = i['percentage']
                    value = i['value']
                    print("date=" + str(date) + ",percentage=" + str(percentage) + ",value=" + str(value))
                except:
                    pass
                print("---------------")

    def start_request_data(self, code, size):
        request_url = self.url.format(code, size)
        res = requests.get(request_url, headers=self.headers)
        res.encoding = 'utf-8'
        s = json.loads(res.text)
        s = s['data']['items']
        f = ((s[len(s) - 1]['date']).split("-"))[1]
        print("月份=" + str(((s[len(s) - 1]['date']).split("-"))[0] + "-" + ((s[len(s) - 1]['date']).split("-"))[1]))

        max = float(s[len(s) - 1]['percentage'])
        min = float(1000)
        start = s[len(s) - 1]['value']
        end = 0

        maxlist = []
        minlist = []
        startlist = []
        endlist = []
        reslist = []
        mlist = []
        mlist.append(str(((s[len(s) - 1]['date']).split("-"))[0] + "-" + ((s[len(s) - 1]['date']).split("-"))[1]))

        for j in range(len(s) - 1, -1, -1):
            i = s[j]

            m = (i['date'].split("-"))
            if m[1] == f:

                if float(i['percentage']) > float(max):
                    max = float(i['percentage'])
                if float(i['percentage']) < float(min):
                    min = float(i['percentage'])
                if j != 0 and ((s[j - 1]['date']).split("-"))[1] != f:
                    end = i['value']
                # try:
                #     date = i['date']
                #     percentage = i['percentage']
                #     value = i['value']
                #     print("date="+str(date)+",percentage="+str(percentage)+",value="+str(value))
                # except:
                #     pass
            else:
                print("max=" + str(max) + ",min=" + str(min))
                maxlist.append(float(str(max)))
                minlist.append(float(str(min)))
                max = float(0)
                min = float(1000)
                print("start=" + str(start) + ",end=" + str(end) + ",差值=" + str(round(float(end) - float(start), 4)))
                startlist.append(float(str(start)))
                endlist.append(float(str(end)))
                reslist.append(float(str(round(float(end) - float(start), 4))))
                f = m[1]

                start = i['value']
                # max = i['value']
                # max=0
                print("---------------")
                print("月份=" + str(m[0] + "-" + m[1]))
                mlist.append(str(m[0] + "-" + m[1]))
                # try:
                #     date = i['date']
                #     percentage = i['percentage']
                #     value = i['value']
                #     print("date="+str(date)+",percentage="+str(percentage)+",value="+str(value))
                # except:
                #     pass
            if j == 0:
                print("max=" + str(max) + ",min=" + str(min))
                maxlist.append(float(str(max)))
                minlist.append(float(str(min)))
                print("start=" + str(start) + ",end=" + s[j]['value'] + ",差值=" + str(
                    round(float(s[j]['value']) - float(start), 4)))
                startlist.append(float(str(start)))
                endlist.append(float(s[j]['value']))
                reslist.append(float(str(round(float(s[j]['value']) - float(start), 4))))

        # print(maxlist)
        # print(minlist)
        # print(startlist)
        # print(endlist)
        print(reslist)
        print(mlist)
        pltShow = PltShow()
        ###1.月初、月末
        # analysis1(mlist,startlist,endlist)
        pltShow.analysis1(mlist, startlist,endlist)
        ###2.当月最高涨、最低跌
        # analysis2(mlist, maxlist, minlist)
        pltShow.analysis2(mlist, maxlist, minlist)
        ###3.当月波动值（最高涨、最低跌之差）
        # analysis3(mlist, maxlist, minlist)
        pltShow.analysis3(mlist, maxlist, minlist)
        ###4.月差值(月末减月初，该月是否盈亏）
        # analysis4(mlist, reslist)
        pltShow.analysis4(mlist, reslist)


if __name__ == '__main__':
    fund_info = FundInfo()
    fund_info.start_request_data("004432", "365")
