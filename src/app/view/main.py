# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from app.util.common import ret_json
from app.model.query import get_trains

main_view = Blueprint('main', __name__)


@main_view.route('/trains', methods=['GET'])
def register():
    data = request.args
    info = get_trains(
        data.get("date", "2018-11-23"), data.get("from_station_name", "武汉"),
        data.get("to_station_name", "庐山"))
    return ret_json(200, "", info)
