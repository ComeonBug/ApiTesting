from weixin.contact.token import WeiXin


class TestToken:

    def test_get_token(self):
        token = WeiXin.get_token()
        assert token