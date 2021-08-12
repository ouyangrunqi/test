# @Author : xhf

import os
from api.base_api import BaseApi


class Cancelorder(BaseApi):
    """
    公司事件类
    """

    def get_cancel_order(self, domain, Authorization, taskId):
        """
        获取部门信息
        :param durationDays:
        :param symbols: 股票、ETF代码
        :param domain: events的域名
        :return: 返回响应体
        """
        # Template模板二次修改的值，p_data
        p_data = {"algo_domain": domain, "Authorization": Authorization,"taskId": taskId}
        res = self.send_api_data('testcase/cancel_order/cancel_order_api.yml', p_data, "get")
        print("algo events res: ", res)
        return res


if __name__ == "__main__":
    a = Cancelorder()
    # print(a.get_algo_events('https://algo-internal.aqumon.com/datamaster', '00001.HK,000001.SZ,VTI.US', '2020-04-12',
    #                         '2021-04-12'))
    pass
