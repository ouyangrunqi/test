import os
from api.base_api import BaseApi


class AlgoStockInfo(BaseApi):
    """
    获取股票信息类
    """

    def get_algo_stock_info(self, domain, symbols, lang):
        """
        获取部门信息
        :param lang:
        :param symbols: 股票、ETF代码
        :param domain: stock_info的域名
        :return: 返回响应体
        """
        # Template模板二次修改的值，p_data
        p_data = {"algo_domain": domain, "symbols": symbols, "lang": lang}
        res = self.send_api_data('testcase/stock_info/stock_info_api.yml', p_data, "get")
        print("algo events res: ", res)
        return res


if __name__ == "__main__":
    a = AlgoStockInfo()
    # print(a.get_algo_events('https://algo-internal.aqumon.com/datamaster', '00001.HK,000001.SZ,VTI.US', '2020-04-12',
    #                         '2021-04-12'))
    pass
