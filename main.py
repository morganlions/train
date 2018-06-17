from pprint import pprint
import requests
from get_urltrain import url
from prettytable import PrettyTable
from color_set import colored
from station import stations


def chair_lists(row_list) :
    chair_list = []
    for i in range(len(row_list) - 5, 21, -1) :
        if row_list[i] != '' :
            chair_list.append(row_list[i])
        else :
            chair_list.append('--')
    return chair_list


headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}

r = requests.get(url, verify=False, headers=headers)  # 请求网址1的内容
rows = r.json()['data']['result']  # 将内容解析为列表
trains = PrettyTable()
trains.field_names = ["车次", "车站", "时间", "历时", "商务座\特等座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧 ", "软座 ", "硬座", "无座",
                      "其他"]
# 设置table的header
num = len(rows)  # 打印列表的个数
# station1 = dict([v, k] for k, v in stations.items())
station_list = dict(zip(stations.values(), stations.keys()))
for row in rows :  # 列表循环
    row_list = row.split('|')
    chair_list = chair_lists(row_list)
    trains.add_row([row_list[3],
                    '\n'.join([colored('green', station_list[row_list[6]]),
                               colored('red', station_list[row_list[7]])]),
                    '\n'.join([colored('green', row_list[8]),
                               colored('red', row_list[9])]),
                    row_list[10],
                    ] + chair_list)

print('查询结束，共有 %d 趟列车。' % num)  # 列表个数也就是列车个数
print(trains)