#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 15:00
# @Author  : hhf
# @File    : conftest.py
import os

import pytest
import yaml


@pytest.fixture(scope='session')
def headers_gl():
    headers = {'accept': 'application/json, text/plain, */*'}
    return headers

@pytest.fixture(scope="session")
def env(request):
    parent_path = os.path.dirname(__file__)
    config_path = os.path.join(parent_path, 'config', 'test', 'config')  # 测试env
    # config_path = os.path.join(request.config.rootdir,
    #                            "config",
    #                            "test",     # 测试env
    #                            "config")
    with open(config_path, encoding='utf-8') as f:
        env_config = yaml.load(f, Loader=yaml.SafeLoader)
    return env_config


@pytest.fixture(scope="session")
def dev_env(request):
    parent_path = os.path.dirname(__file__)
    config_path = os.path.join(parent_path, 'config', 'dev', 'config')
    # config_path = os.path.join(request.config.rootdir,
    #                            "config",
    #                            "test",     # 测试env
    #                            "config")
    with open(config_path, encoding='utf-8') as f:
        env_config = yaml.load(f, Loader=yaml.SafeLoader)
    return env_config


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
