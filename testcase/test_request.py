import json
import requests
import logging
import jsonpath
import hamcrest
from hamcrest import assert_that, any_of
import warnings
warnings.filterwarnings("ignore")

class TestRequests:

    logging.basicConfig(level=logging.INFO)
    url = 'https://testerhome.com/api/v3/topics.json?limit=2'

    def test_get(self):
        r = requests.get(self.url)
        logging.info('测试log')
        logging.info(r.text)
        print(r)

    def test_post(self):
        r = requests.post(self.url,
                          json={'a':1,'b':'string content'},
                          headers={'head1':'a','head2':'b'},
                          proxies={'https':'http://127.0.0.1:8899','http':'http://127.0.0.1:8899'},
                          verify=False)
        print('*'*20)
        print(r.url)
        print(r.json())
        logging.info(json.dumps(r.json(), indent=2))

    def test_cookie(self):
        r = requests.get("https://httpbin.org/cookies",
                         cookies={'a':'cookie_a'})
        print('**************')
        print(json.dumps(r.json(), indent=2))
        # assert r.json()['cookies']['a'] == 'cookie_a'
        print(jsonpath.jsonpath(r.json(),"$.cookies.a"))

    def test_json(self):
        r = requests.get('https://httpbin.org/json', headers = {"accept": "application/json"})
        # jsonpaht里加入判断条件：
        assert jsonpath.jsonpath(r.json(), "$.slideshow.slides[?(@.title=='Overview')].items")[0] == "xxxx"

    def test_hamcrest(self):
        # 通过：校验hamcrest.has_item函数的参数是否在前面assert_that的第一个参数中
        # assert_that(['a','v','b'],hamcrest.has_item('a'))
        # 通过：校验hamcrest.has_items函数的参数是否全部都在前面assert_that的第一个参数中
        # assert_that(['a','v','b'],hamcrest.has_items('a','v'))
        # 不通过
        # assert_that(['a','b','c'], hamcrest.has_items('a','x'))
        # 通过
        assert_that(['a','v'],
                    any_of(['a','v'],'b'))