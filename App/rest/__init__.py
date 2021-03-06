# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-08-28

import logging

from flask import Blueprint
from App.LogManager.LogFormatter import requestformatter
from App.LogManager.LogHandler import LoggerHandlerToMysql
from App.settings import DevelopConfig
from flask_restful import Api
rest = Blueprint('rest', __name__, url_prefix='/rest')
api = Api(rest)
dblogger = logging.getLogger('Dblogger')
consolelog = logging.getLogger('StreamLogger')

SQLALCHEMY_DATABASE_URI = DevelopConfig.SQLALCHEMY_DATABASE_URI
LoggerHandler = LoggerHandlerToMysql(configdb_str=SQLALCHEMY_DATABASE_URI, table_name="example_log")
LoggerHandler.setFormatter(requestformatter)
dblogger.addHandler(LoggerHandler)

from App.rest import views
