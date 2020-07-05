# -*- coding:utf-8 -*-
# @time   :2020/6/30  13:42
# @Author :sunzhe
# @Email  :15967579213@163.com
# @File   :http_request_case.py
import requests
def http_request(url, data, token, method='post'):  # 因为我的形参一定要放在默认参数的前面
    header = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json',
                    'Authorization':token}
    if method == 'get':  # 判断是不是get请求，如果是get请求，就返回result
        response = requests.get(url, params=data, headers=header)
    elif method == 'post':  # 判断是不是post请求，如果是post请求，就返回result
        response = requests.post(url, json=data, headers=header)
    elif method == 'patch':  # 判断是不是potch请求，如果是patch请求，就返回result
        response = requests.patch(url, json=data, headers=header)
    result = response.json()
    return result  # 返回result
