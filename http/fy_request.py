# coding: utf-8

import json
import time
from feiyan.http.request import Request


class FyRequest(Request):
    def __init__(self):
        Request.__init__(self)
        self.__params = dict()
        self.__cloudToken = None
        self.__version = '1.0'
        self.__apiVer = '1.0.0'

    def set_version(self, version):
        self.__version = version

    def get_version(self):
        return self.__version

    def set_api_ver(self, api_ver):
        self.__apiVer = api_ver

    def get_api_ver(self):
        return self.__apiVer

    def set_cloud_token(self, cloud_token):
        self.__cloudToken = cloud_token

    def get_cloud_token(self):
        return self.__cloudToken

    def add_param(self, k, v):
        self.__params[k] = v

    def set_params(self, params):
        self.__params = params

    def get_params(self):
        return self.__params

    def format_params(self):
        body = {
            "id": int(time.time() * pow(10, 6)),
            "version": self.get_version(),
            "request": {
                "apiVer": self.get_api_ver(),
                "cloudToken": self.get_cloud_token()
            },
            "params": self.get_params()
        }
        self.set_body(json.dumps(body))
