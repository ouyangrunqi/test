import os
import allure
import pytest
from api.users_select import UsersSelect
from common.get_log import log
from conftest import headers_gl


class TestUsersSelect():
    """
    用户查询测试类
    1.参数化存放在特定的yml文件中，用三级目录管理用例、参数数据和ids的数据
    2.critical的用例等级为完整测试，blocker等级为冒烟测试
    3.每个用例都配合fixture，完成了不同的前置和后置，实现了不同用例互不干扰的状态
    """

    # 新建公司事件类实例
    event = UsersSelect()

    # 获取参数化的数据
    para_data = event.load_yaml('testcase/users/para_user_select.yml')

    # 获取不同用例需要的参数化数据以及ids标题数据
    # add_data = para_data["add"]["data"]
    # add_ids = para_data["add"]["ids"]

    get_data = para_data["get"]["data"]
    get_ids = para_data["get"]["ids"]

    #
    # delete_data = para_data["delete"]["data"]
    # delete_ids = para_data["delete"]["ids"]
    #
    # edit_data = para_data["edit"]["data"]
    # edit_ids = para_data["edit"]["ids"]

    @pytest.mark.parametrize("Authorization, status, expect_http_code", get_data, ids=get_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_users_select(self, env, Authorization, status, expect_http_code):
        algo_domain = env['host']['algo_users']
        # Authorization = headers_gl['get']['headers']['Authorization']
        log.info("-------------开始获取公司事件测试---------")
        res = self.event.get_users_select(algo_domain, Authorization)
        log.info("-------------测试结束---------")

        # ******** http协议状态码判断 ********
        print('******** http协议状态码判断... ')
        print("res.status_code: {0}".format(res.status_code))
        if res.status_code == expect_http_code:
            print('检测点：http status_code 符合预期！')
            assert True
        else:
            print('WARN --> http请求响应status_code={0}'.format(res.status_code))
            assert False
        # ******** 实际测试输出 ********
        print('******** 实际测试输出... ')
        res_json = res.json()
        if res.status_code == 200:
            real_data = res_json['data']
            error = res_json['errors']
            if real_data:  # 数据非空
                # print('检测点：接口返回data非空,符合预期！')
                print('检测点：接口返回data 符合预期！返回数据为：{0}'.format(real_data))
                # 检测返回的数据类型
                if isinstance(real_data, dict):
                    print('检测点：接口返回data type符合预期！返回数据为：{0}'.format(type(real_data)))
                else:
                    print('WARN --> data 部分类型与预期不符,预期类型:dict,实际类型:{0}.(real_data={1})'.format(type(real_data),
                                                                                              real_data))
                    assert False
                event_keys = ['clientNumber', 'riskType', 'prefRegion', 'prefSector', 'status',
                              'riskAckStatus']

            elif error[0]['code'] == 100002:
                assert True
            else:
                assert False
        else:
            pass




if __name__ == '__main__':
    # a = TestEvents
    # print('Test data: {0}, Test ids: {1}'.format(a.get_data, a.get_ids))
    pytest.main(['-v', 'test_users_select.py'])
    # pytest.main(['-v', '--alluredir', '../report/result', 'test_algo_stock_info.py'])
    # os.system('allure generate ../report/result -o ../report/html --clean')
