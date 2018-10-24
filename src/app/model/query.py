# -*- coding: utf-8 -*-
import requests
from app.model.stations import stations_dict
from app.config.constant import url_query

# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()

# 反转k，v形成新的字典
code_dict = {v: k for k, v in stations_dict.items()}


def get_query_url(*args):
    # 解析参数
    date = ""
    from_station_name = ""
    to_station = ""
    try:
        date = args[0]
        from_station_name = args[1]
        to_station_name = args[2]
        from_station = stations_dict[from_station_name]
        to_station = stations_dict[to_station_name]
    except Exception as e:
        date, from_station, to_station = '--', '--', '--'

    url = (url_query + '?'
           'leftTicketDTO.train_date={}&'
           'leftTicketDTO.from_station={}&'
           'leftTicketDTO.to_station={}&'
           'purpose_codes=ADULT').format(date, from_station, to_station)

    return url


def query_train_info(url):
    info_list = []
    try:
        r = requests.get(url, verify=False)
        # 获取返回的json数据里的data字段的result结果
        raw_trains = r.json()['data']['result']

        for raw_train in raw_trains:
            data_list = raw_train.split('|')

            train_no = data_list[3]
            from_station_code = data_list[6]
            from_station_name = code_dict[from_station_code]
            to_station_code = data_list[7]
            to_station_name = code_dict[to_station_code]
            start_time = data_list[8]
            arrive_time = data_list[9]
            time_fucked_up = data_list[10]
            first_class_seat = data_list[31] or '--'
            second_class_seat = data_list[30] or '--'
            soft_sleep = data_list[23] or '--'
            hard_sleep = data_list[28] or '--'
            hard_seat = data_list[29] or '--'
            no_seat = data_list[26] or '--'

            # 打印查询结果
            keys = [
                "车次", "出发站", "目的地", "出发时间", "到达时间", "消耗时间", "座位情况：", "一等座",
                "二等座", "软卧", "硬卧", "硬座", "无座"
            ]
            values = [
                train_no, from_station_name, to_station_name, start_time,
                arrive_time, time_fucked_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat
            ]
            info = dict(zip(keys, values))
            info_list.append(info)

        return info_list
    except Exception as e:
        return "参数错误"


# eg: "2018-10-23", "武汉", "庐山"
def get_trains(date, from_station_name, to_station_name):
    url = get_query_url(date, from_station_name, to_station_name)
    return query_train_info(url)
