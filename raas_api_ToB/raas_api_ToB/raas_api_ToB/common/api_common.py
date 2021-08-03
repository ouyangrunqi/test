#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 14:28
# @Author  : hhf
# @File    : api_common.py

import requests, json, yaml
from os import path


def access_api(domain, url, method, params, headers):
    print('params={0},type={1}'.format(params, type(params)))
    if str(method).lower() == 'get':
        print('开始get请求...')
        res = requests.get(url=domain + url, params=params, headers=headers, timeout=60)
    else:  # str(method).lower() == 'post'
        print('开始post请求...')
        res = requests.post(url=domain + url, data=json.dumps(params), headers=headers)
    print('res.url=', res.url)

    return res
    # if res.status_code != 200:
    #     print('WARN --> 接口[method：{0}, url: {1}, params:{2}]请求响应状态码为:[{3}]'.format(method, url, params, res.status_code))
    #     raise Exception('WARN --> 接口[method：{0}, url: {1}, params:{2}]请求响应状态码为:[{3}]'.format(method, url, params, res.status_code))
    # res_json = res.json()
    # print('res_json=', res_json)
    # return res_json


def access_yaml(yaml_file):
    parent_path = path.dirname(__file__)
    grandparent_path = path.dirname(parent_path)
    testcase_path = path.join(grandparent_path, 'testcase', yaml_file)
    # print('testcase_path=', testcase_path)
    f = open(file=testcase_path, encoding='utf-8')
    content = yaml.load(f, Loader=yaml.FullLoader)
    return content


if __name__ == '__main__':
    res = access_yaml('account_module')
    print(type(res))
    print(res)
