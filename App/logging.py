# -*- coding: utf-8 -*-
# @File  : logging.py
# @Author: Holly
# @Date  : 2019-10-15
from App.LogManager.LogFormatter import formatter, RequestFormatter

LOG_CONFIG = {
    'version': 1,  # 该配置写法固定
    'formatters': {  # 设置输出格式
        'default': {
            'format': '{'
                      '"asctime":"%(asctime)s",'
                      '"levelname":"%(levelname)s",'
                      '"funcName":"%(funcName)s",'
                      '"filename": "%(filename)s",'
                      '"lineno": "%(lineno)d",'
                      '"message": "%(message)s"}'
        },
        'simple': {
            'format': '{'
                      '"asctime":"%(asctime)s",'
                      '"levelname":"%(levelname)s",'
                      '"funcName":"%(funcName)s",'
                      '"filename": "%(filename)s",'
                      '"lineno": "%(lineno)d",'
                      '"process": "%(process)d",'
                      '"processName": "%(processName)s",'
                      '"thread": "%(thread)d",'
                      '"threadName": "%(threadName)s",'
                      '"message": "%(message)s"}'
        },
        'requestinfo': {
            'format':'{'
            '"asctime":"%(asctime)s",'
            '"levelname":"%(levelname)s",'
            '"funcName":"%(funcName)s",'
            '"filename": "%(filename)s",'
            '"lineno": "%(lineno)d",'
            '"process": "%(process)d",'
            '"processName": "%(processName)s",'
            '"thread": "%(thread)d",'
            '"threadName": "%(threadName)s",'
            '"message": "%(message)s"'
            '}'
        }

    },
    # 设置处理器
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default'
        },
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default',
            'level': 'DEBUG'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'formatter': 'default',
            'level': 'WARNING'
        }},
    # 设置root日志对象配置
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    },
    # 设置其他日志对象配置
    'loggers': {
        'StreamLogger':
            {'level': 'DEBUG',
             'handlers': ['wsgi'],
             'propagate': 0},
        'FileLogger':
            {'level': 'DEBUG',
             'handlers': ['console', 'file'],
             'propagate': 0},
    }
}

# logging.config.dictConfig(config)
# StreamLogger = logging.getLogger("StreamLogger")
# FileLogger = logging.getLogger("FileLogger")
