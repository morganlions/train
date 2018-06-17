from pprint import pprint
import urllib
from urllib import request
import re

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
req = urllib.request.Request(url)
r = urllib.request.urlopen(req).read().decode('utf-8')
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r)
stations = dict(stations)
stations = dict(zip(stations.keys(),stations.values()))