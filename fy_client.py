# coding: utf-8

from feiyan import client
from feiyan.common import constant
from feiyan.http.fy_request import FyRequest


class FyClient:
    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
        self.host = 'https://api.link.aliyun.com'

    def __client(self):
        return client.DefaultClient(app_key=self.app_key, app_secret=self.app_secret)

    def execute(self, fy_request):
        if not isinstance(fy_request, FyRequest):
            raise Exception('invalid fy_request instance')
        fy_request.set_host(self.host)
        fy_request.set_method('post')
        fy_request.set_protocol(constant.HTTPS)
        fy_request.set_content_type(constant.CONTENT_TYPE_JSON)
        fy_request.format_params()
        return self.__client().execute(fy_request)
