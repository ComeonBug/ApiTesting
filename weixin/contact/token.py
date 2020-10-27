import requests
import yaml
import json
import logging


class WeiXin:
    logging.basicConfig(level=logging.DEBUG)
    _token = ""

    # 不需要初始化，用classmethod
    @classmethod
    def get_token(cls):
        if len(cls._token) == 0:
            # 从yaml文件中读取数据
            conf = yaml.load(open('weixin.yml'))
            # logging.debug(conf.get('env'))
            url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
            r = requests.get(url, params={'corpid':conf['env']['corpid'],'corpsecret':conf['env']['corpsecret']})
            result = r.json()
            cls._token = result['access_token']
            # logging.debug(cls._token)
        return cls._token
