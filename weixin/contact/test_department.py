import requests
import logging
import json
from weixin.contact.token import WeiXin


class TestDepartment:
    logging.basicConfig(level=logging.DEBUG)
    @classmethod
    def setup_class(cls):
        print('setup_class')
        WeiXin.get_token()
        print(WeiXin._token)

    def setup(self):
        print('setup')

    def test_create(self):
        data = {
                   "name": "上海研发中心",
                   "name_en": "SHDD",
                   "parentid": 1,
                   "order": 1,
                   "id": 2
                }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                      params={"access_token":WeiXin.get_token()},
                      json=data).json()
        logging.debug(json.dumps(r, indent=2))

    def test_create_nlevel(self):
        parentid = 1
        for i in range(1,6):
            data = {
                       "name": "上海研发中心"+str(i),
                       "parentid": parentid
                    }
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token":WeiXin.get_token()},
                          json=data).json()
            logging.debug(json.dumps(r, indent=2))
            parentid = r['id']



    def test_getDepartment(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token":WeiXin.get_token()}).json()
        logging.debug(json.dumps(r, indent=2))
