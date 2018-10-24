# -*- coding: utf-8 -*-
"""
   使用方法：python3 get_stations.py >> stations.py
"""
import requests
import re
from app.config.constant import url_station_name

# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()

# key：城市名 value：城市代码
url = url_station_name
r = requests.get(url, verify=False)

pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
result = re.findall(pattern, r.text)
station = dict(result)

print("stations_dict =", station)
