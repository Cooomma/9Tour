import os
import json
import configparser
import logging
from logging.handlers import TimedRotatingFileHandler

CONFIG_PATH = 'resources/config.ini'


class Config:
    if os.path.isfile(CONFIG_PATH):
        config = configparser.ConfigParser()

        # api
        # TODO: api config

        # app
        token = config.get('app', 'token')

    else:
        # api
        # TODO: api config

        # app
        token = os.environ['token']


class Logger:
    # Create Tmp Folder
    os.makedirs('tmp/', exist_ok=True, mode=0o777)

    app_json_format = {
        'ts': '%(asctime)s',
        'level': '%(levelname)s',
        'function': '%(module)s.%(funcName)s',
        'line_num': '%(lineno)s',
        'log': '%(message)s'
    }

    dialog_json_format = {
        'ts': '%(asctime)s',
        'function': '%(module)s.%(funcName)s',
        'message': '%(message)s'
    }

    app_formatter = logging.Formatter(
        fmt=json.dumps(app_json_format, ensure_ascii=False, sort_keys=True),
        datefmt='%Y-%m-%d %H:%M:%S')
    dialog_formatter = logging.Formatter(
        fmt=json.dumps(dialog_json_format, ensure_ascii=False, sort_keys=True),
        datefmt='%Y-%m-%d %H:%M:%S')

    # For App
    app_logger = logging.getLogger('app')
    app_logger.setLevel(logging.DEBUG)
    app_handler = TimedRotatingFileHandler(
        'tmp/app.log',
        when='h',
        interval=1,
        encoding='UTF-8',
        utc=True
    )
    app_handler.setFormatter(app_formatter)
    app_logger.addHandler(app_handler)

    # For Dialog
    dialog_logger = logging.getLogger('dialog')
    dialog_logger.setLevel(logging.DEBUG)
    dialog_handler = TimedRotatingFileHandler(
        'tmp/dialog.log',
        when='h',
        interval=1,
        encoding='UTF-8',
        utc=True
    )
    dialog_handler.setFormatter(dialog_formatter)
    dialog_logger.addHandler(dialog_handler)
