# coding: utf-8

import time
import uuid
import hmac
import hashlib
import base64
from feiyan.common import constant

TIME_ZONE = "GMT"
FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%SZ"
FORMAT_RFC_2616 = "%a, %d %b %Y %X GMT"


def get_iso_8061_date():
    return time.strftime(FORMAT_ISO_8601, time.gmtime())


def get_rfc_2616_date():
    return time.strftime(FORMAT_RFC_2616, time.gmtime())


def get_timestamp():
    return str(int(time.time() * 1000))


def get_uuid():
    return str(uuid.uuid4())


def sign(source, secret):
    h = hmac.new(secret.encode('utf-8'), source.encode('utf-8'), hashlib.sha256)
    signature = base64.b64encode(h.digest()).strip().decode()
    return signature


def _get_md5(content):
    return hashlib.md5(content.encode('utf-8')).digest()


def get_md5_base64_str(content):
    return base64.b64encode(_get_md5(content)).strip().decode()


def build_sign_str(uri=None, method=None, headers=None, body=None):
    lf = '\n'
    string_to_sign = list()
    string_to_sign.append(method)

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_ACCEPT in headers and headers[constant.HTTP_HEADER_ACCEPT]:
        string_to_sign.append(headers[constant.HTTP_HEADER_ACCEPT])

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_CONTENT_MD5 in headers and headers[constant.HTTP_HEADER_CONTENT_MD5]:
        string_to_sign.append(headers[constant.HTTP_HEADER_CONTENT_MD5])

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_CONTENT_TYPE in headers and headers[constant.HTTP_HEADER_CONTENT_TYPE]:
        string_to_sign.append(headers[constant.HTTP_HEADER_CONTENT_TYPE])

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_DATE in headers and headers[constant.HTTP_HEADER_DATE]:
        string_to_sign.append(headers[constant.HTTP_HEADER_DATE])

    string_to_sign.append(lf)
    string_to_sign.append(_format_header(headers=headers))
    string_to_sign.append(_build_resource(uri=uri, body=body))

    return ''.join(string_to_sign)


def _build_resource(uri="", body=None):
    if body is None:
        body = {}
    if uri.__contains__("?"):
        uri_array = uri.split("?")
        uri = uri_array[0]
        query_str = uri_array[1]
        if not body:
            body = {}
        if query_str:
            query_str_array = query_str.split("&")
            for query in query_str_array:
                query_array = query.split("=")
                if query_array[0] not in body:
                    body[query_array[0]] = query_array[1]

    resource = list()
    resource.append(uri)
    if body:
        resource.append("?")
        param_list = list(body.keys())
        param_list.sort()
        first = True
        for key in param_list:
            if not first:
                resource.append("&")
            first = False

            if body[key]:
                resource.append(key)
                resource.append("=")
                resource.append(body[key])
            else:
                resource.append(key)

    if resource is None:
        return ''

    return "".join(str(x) for x in resource)


def convert_utf8(input_string):
    if isinstance(input_string, str):
        input_string = input_string.encode('utf-8')
    return input_string


def _format_header(headers=None):
    if headers is None:
        headers = {}
    lf = '\n'
    temp_headers = []
    if len(headers) > 0:
        header_list = list(headers.keys())
        header_list.sort()
        signature_headers = []
        for k in header_list:
            if k.startswith("X-Ca-"):
                temp_headers.append(k)
                temp_headers.append(":")
                temp_headers.append(str(headers[k]))
                temp_headers.append(lf)
                signature_headers.append(k)
        headers[constant.X_CA_SIGNATURE_HEADERS] = ','.join(signature_headers)
    return ''.join(temp_headers)


def device_data_sign(app_key, app_secret, message, msg_code):
    parameters = {
        'appKey': app_key,
        'message': message,
        'msgCode': msg_code
    }
    sign_str = _build_resource(body=parameters)[1:] + app_secret
    signature = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    return signature
