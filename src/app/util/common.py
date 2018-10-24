# -*- coding: utf-8 -*-
import json


def ret_json(ret_code=200, error_msg="ok", data=""):
    ret = {"ret_code": ret_code}
    if ret_code != 200:
        ret["error_msg"] = error_msg
    if data != "":
        ret["data"] = data
    return json.dumps(ret)
