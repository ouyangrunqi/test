# @Author : xhf

import os
from api.base_api import BaseApi


class Predicting(BaseApi):
    """
    公司事件类
    """

    def get_advice_predicting(self, domain, Authorization, type, amount, target):
        """
        获取部门信息
        :param durationDays:
        :param symbols: 股票、ETF代码
        :param domain: events的域名
        :return: 返回响应体
        """
        # Template模板二次修改的值，p_data
        p_data = {"algo_domain": domain, "Authorization": Authorization,"type": type, "amount": amount, "target": target}
        res = self.send_api_data('testcase/advice_predicting/advice_predicting_api.yml', p_data, "get")
        print("algo events res: ", res)
        return res


if __name__ == "__main__":
    a = Predicting()
    # print(a.get_algo_events('https://algo-internal.aqumon.com/datamaster', '00001.HK,000001.SZ,VTI.US', '2020-04-12',
    #                         '2021-04-12'))
    pass
