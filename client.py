# coding: utf-8

import requests
from feiyan.common import constant
from feiyan.auth.signature_composer import get_timestamp, get_uuid, get_md5_base64_str, build_sign_str, sign


class DefaultClient:
    def __init__(self, app_key=None, app_secret=None, time_out=None):
        self.__app_key = app_key
        self.__app_secret = app_secret
        self.__time_out = time_out
        pass

    def execute(self, request=None):
        try:
            headers = self.build_headers(request)
            r = requests.request(
                url=request.get_host() + request.get_url(),
                method=request.get_method(),
                headers=headers,
                data=request.get_body(),
                timeout=request.get_time_out()
            )
            return r
        except IOError:
            raise
        except AttributeError:
            raise

    def build_headers(self, request=None):
        headers = dict()
        header_params = request.get_headers()
        headers[constant.X_CA_TIMESTAMP] = get_timestamp()
        headers[constant.X_CA_KEY] = self.__app_key

        body = request.get_body()

        headers[constant.X_CA_NONCE] = get_uuid()

        if request.get_content_type():
            headers[constant.HTTP_HEADER_CONTENT_TYPE] = request.get_content_type()
        else:
            headers[constant.HTTP_HEADER_CONTENT_TYPE] = constant.CONTENT_TYPE_JSON

        if constant.HTTP_HEADER_ACCEPT in header_params \
                and header_params[constant.HTTP_HEADER_ACCEPT]:
            headers[constant.HTTP_HEADER_ACCEPT] = header_params[constant.HTTP_HEADER_ACCEPT]
        else:
            headers[constant.HTTP_HEADER_ACCEPT] = constant.CONTENT_TYPE_JSON

        if constant.POST == request.get_method() and constant.CONTENT_TYPE_JSON == request.get_content_type():
            headers[constant.HTTP_HEADER_CONTENT_MD5] = get_md5_base64_str(request.get_body())
            str_to_sign = build_sign_str(
                uri=request.get_url(),
                method=request.get_method(),
                headers=headers
            )
        else:
            str_to_sign = build_sign_str(
                uri=request.get_url(),
                method=request.get_method(),
                headers=headers, body=body
            )

        headers[constant.X_CA_SIGNATURE] = sign(str_to_sign, self.__app_secret)

        return headers
