# encoding = utf-8


import configparser

cfg = configparser.ConfigParser()
cfg.read('test.ini')
print(cfg.sections())
