import pytest
from api.advice_predicting import Predicting

# 新建api 类的对象
events = Predicting()


# 冒烟测试的前置和后置步骤
@pytest.fixture(scope="session")
def get_advice_predicting_setup(env):
    algo_domain = env['host']['algo_users']
    vti_events = events.get_advice_predicting(algo_domain, ' ')
    return vti_events
