# 阿里飞燕

---

## 说明

---

> 该包只支持 python3 , 如果使用 python2.7版本, 请连接至 https://github.com/jerrygaoyang/feiyan


## 安装

---

> pip install feiyan


## 示例

---

```
from feiyan.http.api import Cloud

# 密钥配置
app_key = '123456'
app_secret = '12345678901234567890'

# 实例化接口类
c = Cloud(app_key, app_secret)

# 接口请求参数
params = {'grantType': 'project', 'res': 'a1234567890'}

# 调用 api 函数
res = c.token(params)

# 输出回调内容
print(res.content)
```


## api 函数清单和参数说明

---

#### 获取云端资源Token

* 函数：

> token(params)

* 参数

```

{
    "grantType": "project",
    "res": "xxxxxx"
}
```

* 回调

```
{
    "code":200,
    "data":{
        "isolationId":"a103ZqtDOCpQJFE9",
        "expireIn":7200000,
        "cloudToken":"d76c34b338184c3a933c39c3ae0ce071"
    },
    "id":"1538185690705015"
}
```


#### 刷新云端资源Token

* 函数

> refresh_token(token)

* 回调

```
{
    "code":200,
    "data":{
        "isolationId":"a103ZqtDOCpQJFE9",
        "expireIn":7200000,
        "cloudToken":"d76c34b338184c3a933c39c3ae0ce071"
    },
    "id":"1538185690705015"
}
```


#### 查询物的产品列表

* 函数

> thing_product_list_get(params, token)

* 参数

```
{
    'productInfoQuery': {
        "pageNo": 1,
        "pageSize": 10
    }
}
```

* 回调

```
{
	"code": 200,
	"data": [{
		"accessMethod": "DATA_DIRECT",
		"gmtModified": 1536298985000,
		"modifier": "501eal0af73dcc8fcce483d2777957b3ed6a4980",
		"productKey": "a1234567890",
		"extendProperties": [{
			"extendAttrId": 16467,
			"gmtModify": 1536806017000,
			"domain": 0,
			"extendAttrKey": "ACTION",
			"extendAttrValue": "ON",
			"gmtCreate": 1529053672000,
			"productKey": "a1d9uTa3b7h",
			"extendAttrName": "允许作为ACTION"
		}],
		"categoryName": "空气净化器",
		"deviceNumLimit": 500000,
		"creator": "501eal0af73dcc8fcce483d2777957b3ed6a4980",
		"productId": 213797,
		"netType": "NET_WIFI",
		"dataFormaINK_FORMAT": "ALINK_FORMAT",
		"aliyunCommodityCode": "ilop",
		"useId2Auth": false,
		"productSecret": "1234567890",
		"categoryKey": "AirPurifier",
		"nodeType": "DEVICE",
		"gmtCreate": 1527663512000,
		"domain": "abc123456789",
		"name": "Breathe2",
		"region": "cn-shanghai",
		"rbacTenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"categoryId": 83,
		"status": "RELEASE_STATUS"
	}],
	"id": "1538188889522421"
}
```


#### 查询物的产品

* 函数

> thing_product_get(params, token)

* 参数

```
{
    'productKey': '1234567890'
}
```

* 回调

```
{
	"code": 200,
	"data": {
		"accessMethod": "DATA_DIRECT",
		"gmtModified": 1536544723000,
		"modifier": "501eal0af73dcc8fcce483d2777957b3ed6a4980",
		"extendProperties": [{
			"extendAttrId": 8137,
			"gmtModify": 1536299101000,
			"domain": 0,
			"extendAttrKey": "PUBLIC_VERSION_APP",
			"extendAttrValue": "OFF",
			"gmtCreate": 1527663512000,
			"productKey": "1234567890",
			"extendAttrName": "加入公版APP标记"
		}, {
			"extendAttrId": 8134,
			"gmtModify": 1527000,
			"domain": 0,
			"extendAttrKey": "ILOP_SERVICE_GOOGLEHOME",
			"extendAttrValue": "OFF",
			"gmtCreate": 1527663512000,
			"productKey": "b1YEAzMF80d",
			"extendAttrName": "开通googleHome服"
		}],
		"productKey ": "b1YEAzMF80d ",
		"categoryName ": "空气净化器 ",
		"deviceNumLimit ": 500000,
		"creator": "501eal0af73dcc8fcce483d2777957b3ed6a4980",
		"productId": 123456,
		"dataFormat": "ALINK_FORMAT",
		"netType": "NET_WIFI",
		"useId2Auth": false,
		"aliyunCommodityCode": "ilop",
		"categoryKey": "AirPurifier",
		"productSecret": "1234567890",
		"nodeType": "DEVICE",
		"gmtCreate": 1527663512000,
		"domain": "b1YEAzMF80d",
		"name": "Breathe2",
		"region": "cn-shanghai",
		"rbacTenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"categoryId": 83,
		"status": "RELEASE_STATUS"
	},
	"id": "1538189551927810"
}
```


#### 获取物的属性

* 函数

> thing_properties_get(params, token)

* 参数

```
{
    'iotId': 'c69B4mcRz26v6JGLgOJD0010336900'
}
```

* 回调

```
{
	"code": 200,
	"data": [{
		"iotId": "c69B4mcRz26v6JGLgOJD0010336900",
		"gmtModified": 1537871668144,
		"attribute": "AppointmentTime",
		"batchId": "f979237c50be4605881a4d2702cf6ead",
		"value": 108.0000000000000000
	}, {
		"iotId": "c69B4mcRz26v6JGLgOJD0010336900",
		"gmtModified": 1537871666958,
		"attribute": "CurrentTemperature",
		"batchId": "441b6438f292433badac829f6a463fcd",
		"value": 27.0000000000000000
	}, {
		"iotId": "c69B4mcRz26v6JGLgOJD0010336900",
		"gmtModified": 1537871668946,
		"attribute": "DeviceConfiguration",
		"batchId": "6af55fbd191f43009958d2303e380375",
		"value": {
			"MotorSpeedPWM_2": 27368,
			"MotorSpeedPWM_1": 11428,
			"CalibrationPM25": 0,
			"AlarmPM25": 30,
			"AlarmCO2": 1000,
			"CalibrationCO2": 0,
			"MotorSpeedPWM_3": 43156
		}
	}, {
		"iotId": "c69B4mcRz26v6JGLgOJD0010336900",
		"gmtModified": 1537871660604,
		"attribute": "_sys_device_pid",
		"batchId": "9d1b63b9-aace-49dc-8623-85eb41f9ef0d",
		"value": "AliOSThings"
	}],
	"id": "1538190327259799"
}
```


#### 获取物的模板

* 函数

> thing_tsl_get(params, token)

* 参数

```
{
    'iotId': 'c69B4mcRz26v6JGLgOJD0010336900'
}
```

* 回调

```
{
	"code": 200,
	"data": {
		"schema": "https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json",
		"profile": {
			"productKey": "a1d9uTa3b7h",
			"deviceName": "c69B4mcRz26v6JGLgOJD"
		},
		"link": "/sys/a1d9uTa3b7h/c69B4mcRz26v6JGLgOJD/thing/",
		"services": [{
				"outputData": [],
				"identifier": "AddKey",
				"inputData": [{
						"identifier": "LockType",
						"dataType": {
							"specs": {
								"1": "指纹",
								"2": "密码",
								"3": "卡",
								"4": "机械钥匙"
							},
							"type": "enum"
						},
						"name": "开锁方式"
					},
					{
						"identifier": "UserLimit",
						"dataType": {
							"specs": {
								"1": "普通用户",
								"2": "管理员",
								"3": "劫持用户"
							},
							"type": "enum"
						},
						"name": "用户权限"
					}
				],
				"method": "thing.service.AddKey",
				"name": "添加钥匙",
				"required": true,
				"callType": "async"
			}
		],
		"properties": [{
			"identifier": "LockState",
			"dataType": {
				"specs": {
					"0": "关闭",
					"1": "打开"
				},
				"type": "enum"
			},
			"name": "门锁状态",
			"accessMode": "r",
			"required": true
		}],
		"events": [
			{
				"outputData": [],
				"identifier": "TamperAlarm",
				"method": "thing.event.TamperAlarm.post",
				"name": "防撬报警",
				"type": "alert",
				"required": true
			}
		]
	},
	"id": "1538190870103674"
}
```


#### 触发物的服务

* 函数

> thing_service_invoke(params, token)

* 参数

```
{
    "iotId": "D95D242941CE821ECCE4F31A2697",
    "identifier": "xxxx",
    "args": {}
}
```

* 回调

```
{
  "code": 200,
  "data": {},
  "id": "1538190870103674"
}
```


#### 设置物的属性

* 函数

> thing_properties_set(params, token)

* 参数

```
{
    "iotId": "D95D242941CE821ECCE4F31A2697",
    "items": {}
}
```

* 回调

```
{
  "code": 200,
  "data": {},
  "id": "1538190870103674"
}
```


#### 获取物的连接状态

* 函数

> thing_status_get(params, token)

* 参数

```
{
    "iotId": "D95D242941CE821ECCE4F31A2697"
}
```

* 回调

```
{
	"code": 200,
	"data": {
		"time": 1537871888000,
		"status": 3
	},
	"id": "1538193184384915"
}
```


#### 获取物的基本信息

* 函数

> thing_info_get(params, token)

* 参数

```
{
    "iotId": "D95D242941CE821ECCE4F31A2697"
}
```

* 回调

```
{
	"code": 200,
	"data": {
		"gmtModified": 1537871888000,
		"activeTime": 1537871662000,
		"deviceKey": "c69B4mcRz26v6JGLgOJD",
		"statusLast": 1,
		"productKey": "a1d9uTa3b7h",
		"gmtCreate": 1537856353000,
		"iotId": "c69B4mcRz26v6JGLgOJD0010336900",
		"deviceSecret": "Pcxnrhc1DikSMnZ48FUIH9brb1Rc5sYr",
		"name": "c69B4mcRz26v6JGLgOJD",
		"thingType": "DEVICE",
		"region": "cn-shanghai",
		"firmwareVersion": "app-1.0.0-20180925.1338",
		"rbacTenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"status": 3
	},
	"id": "1538193367379207"
}
```


#### 批量获取物

* 函数

> things_info_get(params, token)

* 参数

```
{
    "productKey": "a1d9uTa3b7h",
    "status": 3,
    'currentPage': 1,
    'pageSize': 2
}
```

* 回调

```
{
	"code": 200,
	"data": [{
		"gmtModified": 1534922756000,
		"activeTime": 1529651482000,
		"deviceKey": "rwpefi5N8sIPWBiL5LNc",
		"gmtCreate": 1529546182000,
		"productKey": "a1d9uTa3b7h",
		"statusLast": 1,
		"iotId": "rwpefi5N8sIPWBiL5LNc0010e16a00",
		"deviceSecret": "5Cjez2vpxJmAZyaNxLC6PCrK45OckBW6V+jv+KlO4Egl51dLNnK7CMa6j/W9ZKVV",
		"name": "rwpefi5N8sIPWBiL5LNc",
		"thingType": "DEVICE",
		"region": "cn-shanghai",
		"firmwareVersion": "app-1.0.0-20180705.1111",
		"rbacTenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"status": 3
	}, {
		"gmtModified": 1537863306000,
		"activeTime": 1536842173000,
		"deviceKey": "YJSSBqiCaV8v57ez1yI8",
		"gmtCreate": 1529559542000,
		"productKey": "a1d9uTa3b7h",
		"statusLast": 1,
		"iotId": "YJSSBqiCaV8v57ez1yI80010c05e00",
		"deviceSecret": "18dP050cpclibg22/SUmXvF61v/C3zp6eOLymYDrypEl51dLNnK7CMa6j/W9ZKVV",
		"name": "YJSSBqiCaV8v57ez1yI8",
		"thingType": "DEVICE",
		"region": "cn-shanghai",
		"firmwareVersion": "app-1.0.0-20180903.2246",
		"rbacTenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"status": 3
	}],
	"id": "1538193644477318"
}
```


#### 获取物的事件 timeline 数据

* 函数

> thing_event_timeline_get(params, token)

* 参数

```
{
    "iotId": "rwpefi5N8sIPWBiL5LNc0010e16a00",
    "identifier": "xxxx",
    "eventType": "Error",
    "start": 1517217645000,
    "end": 1587217645000,
    "pageSize": 10,
    "ordered": True
}
```


* 回调

```
{
    "code":200,
    "data":{
        "items": [
            {
                "eventCode": "Error",
                "iotId": "YzqEnI5DY03rxLS2pjjo0010840500",
                "eventName": "故障上报",
                "eventType": "info",
                "eventBody": {
                    "ErrorCode": 0
                },
                "batchId": "5ebc6a9c7d15459f823edde6d28c8fb3",
                "timestamp": 1516342985261
            },
            {
                "eventCode": "Error",
                "iotId": "YzqEnI5DY03rxLS2pjjo0010840500",
                "eventName": "故障上报",
                "eventType": "info",
                "eventBody": {
                    "ErrorCode": 0
                },
                "batchId": "4a0b5a7ac85e470684438d5ff77456f1",
                "timestamp": 1516342995305
            }
        ],
        "timestamp": 1516343075699
    },
    "id":"1538194017374719"
}
```


#### 获取物的属性timeline数据

* 函数

> thing_property_timeline_get(params, token)

* 参数

```
{
    "iotId": "D95D242941CE821ECCE4F31A2697",
    "identifier": "xxxx",
    "start": 1517217645000,
    "end": 1517217645000,
    "pageSize": 10,
    "ordered": True
}
```

* 回调

```
{
  "code": 200,
  "data": {
    "items": [
      {
        "iotid": "xqxyZjSKzCwaGdlvbv0O0010851c00",
        "data": 1.23,
        "modifytime": 1511812747287,
        "property": "LightVolt",
        "batchId": "2fc766c5e7064554933ed1f3e4b61803",
        "group": null,
        "timestamp": 1511812747245
      },
      {
        "iotid": "xqxyZjSKzCwaGdlvbv0O0010851c00",
        "data": 1.24,
        "modifytime": 1511812747288,
        "property": "LightVolt",
        "batchId": "2fc766c5e7064554933ed1f3e4b61803",
        "group": null,
        "timestamp": 1511812747245
      }
    ],
    "timestamp": 1511812747245
  },
  "id":"1538194017374719"
}
```


#### 分页查询用户列表

* 函数

> account_query_identity_by_page(params, token)


* 参数

```
{
    "offset": 0,
    "count": 1
}
```

* 回调

```
{
	"code": 200,
	"data": [{
		"gmtModified": 1536931534000,
		"loginId": "36014",
		"nickName": "17681870200",
		"onlineStatus": 0,
		"gmtCreate": 1531462622000,
		"lastLoginTime": 1536931534000,
		"identityId": "50e1op23399ee0c1f32e84f78241f62eed2a6183",
		"loginName": "17681870200",
		"tenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"loginSource": "openAccount",
		"status": "0"
	}],
	"id": "1538197847763446"
}
```


#### 通过三方外标查询账号信息

* 函数

> account_get_by_openid(params ,token)

* 参数

```
{
    "openId":"10000000001",
    "openIdAppKey":"xxx"
}
```

* 回调

```
{
	"code": 200,
	"data": {
		"gmtModified": 1537952076000,
		"loginId": "56947",
		"nickName": "18150106733",
		"gmtCreate": 1537952076000,
		"lastLoginTime": 1537952076000,
		"identityId": "5099opcfba51921fe9d11157b6ad715a0c572941",
		"loginName": "18150106733",
		"tenantId": "BAE4F5145D20416EA228A564AE5F2467",
		"loginSource": "openAccount",
		"status": "0"
	},
	"id": "1538198838429908"
}
```


#### 获取用户绑定的设备列表（包括设备详情）详情内容

* 函数

> device_query_by_user(params ,token)

* 参数

```
{
    "openId":"10000000001",
    "openIdAppKey":"xxx"
}
```

* 回调

```
{
	"code": 200,
	"data": {
		"code": 200,
		"data": [{
			"gmtModified": 1537870633000,
			"categoryImage": "http://iotx-paas-admin.oss-cn-shanghai.aliyuncs.com/publish/image/1526474025826.png",
			"netType": "NET_WIFI",
			"groupId": "",
			"nodeType": "DEVICE",
			"productKey": "b1YEAzMF80d",
			"gmtCreate": 1537870633000,
			"deviceName": "izLR74cr5WVKt0RDvkZA",
			"identityAlias": "15721595369",
			"productName": "Breathe2",
			"iotId": "izLR74cr5WVKt0RDvkZA0010f40d00",
			"owned": 0,
			"identityId": "5081opd8f24e72faeb45194bfabeff5355238011",
			"thingType": "DEVICE",
			"status": 1
		}, {
			"gmtModified": 1537843991000,
			"categoryImage": "http://iotx-paas-admin.oss-cn-shanghai.aliyuncs.com/publish/image/1526474025826.png",
			"netType": "NET_WIFI",
			"nickName": "BREATHE2",
			"groupId": "",
			"nodeType": "DEVICE",
			"productKey": "b1YEAzMF80d",
			"gmtCreate": 1537843897000,
			"deviceName": "OSp1Uuw3kDMBUQDznhWQ",
			"identityAlias": "15721595369",
			"productName": "Breathe2",
			"iotId": "OSp1Uuw3kDMBUQDznhWQ0010a98e00",
			"owned": 1,
			"identityId": "5081opd8f24e72faeb45194bfabeff5355238011",
			"thingType": "DEVICE",
			"status": 1
		}],
		"message": "success"
	},
	"id": "1538198926424070"
}
```


#### 解绑用户和设备

* 函数

> user_device_unbind(params, token)

* 参数

```
{
    "openId":"10000000001",
    "openIdAppKey":"xxx",
    "iotId": "zzzzzzzzzzzzzz"
}
```

* 回调

```

```

