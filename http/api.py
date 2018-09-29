# coding: utf-8

from feiyan.http.fy_request import FyRequest
from feiyan.fy_client import FyClient


class Cloud:
    def __init__(self, app_key, app_secret):
        self.__app_key = app_key
        self.__app_secret = app_secret

    def __client(self):
        return FyClient(self.__app_key, self.__app_secret)

    def execute(self, url, params=None, token=None):
        req = FyRequest()
        req.set_url(url)
        req.set_cloud_token(token)
        req.set_params(params)
        return self.__client().execute(req)

    # 获取云端资源Token
    def token(self, params):
        url = '/cloud/token'
        return self.execute(url, params)

    # 刷新云端资源Token
    def refresh_token(self, token):
        url = '/cloud/token/refresh'
        params = {'cloudToken': token}
        return self.execute(url, params, token)

    # 查询物的产品列表
    def thing_product_list_get(self, params, token):
        url = '/cloud/thing/productList/get'
        return self.execute(url, params, token)

    # 查询物的产品
    def thing_product_get(self, params, token):
        url = '/cloud/thing/product/get'
        return self.execute(url, params, token)

    # 获取物的属性
    def thing_properties_get(self, params, token):
        url = '/cloud/thing/properties/get'
        return self.execute(url, params, token)

    # 获取物的模板
    def thing_tsl_get(self, params, token):
        url = '/cloud/thing/tsl/get'
        return self.execute(url, params, token)

    # 触发物的服务
    def thing_service_invoke(self, params, token):
        url = '/cloud/thing/service/invoke'
        return self.execute(url, params, token)

    # 设置物的属性
    def thing_properties_set(self, params, token):
        url = '/cloud/thing/properties/set'
        return self.execute(url, params, token)

    # 获取物的连接状态
    def thing_status_get(self, params, token):
        url = '/cloud/thing/status/get'
        return self.execute(url, params, token)

    # 获取物的基本信息
    def thing_info_get(self, params, token):
        url = '/cloud/thing/info/get'
        return self.execute(url, params, token)

    # 批量获取物
    def things_info_get(self, params, token):
        url = '/cloud/things/info/get'
        return self.execute(url, params, token)

    # 获取物的事件 timeline 数据
    def thing_event_timeline_get(self, params, token):
        url = '/cloud/thing/event/timeline/get'
        return self.execute(url, params, token)

    # 获取物的属性timeline数据
    def thing_property_timeline_get(self, params, token):
        url = '/cloud/thing/property/timeline/get'
        return self.execute(url, params, token)

    # 分页查询用户列表
    def account_query_identity_by_page(self, params, token):
        url = '/cloud/account/queryIdentityByPage'
        return self.execute(url, params, token)

    # 通过三方外标查询账号信息
    def account_get_by_openid(self, params, token):
        url = '/cloud/account/getByOpenId'
        return self.execute(url, params, token)

    # 获取用户绑定的设备列表（包括设备详情）详情内容
    def device_query_by_user(self, params, token):
        url = '/cloud/device/queryByUser'
        return self.execute(url, params, token)

    # 解绑用户和设备
    def user_device_unbind(self, params, token):
        url = '/cloud/user/device/unbind'
        return self.execute(url, params, token)
