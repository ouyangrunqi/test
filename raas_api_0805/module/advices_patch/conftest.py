import pytest
from api.advices_patch import AdvicesPatch



# 新建api 类的对象
events = AdvicesPatch()



# 冒烟测试的前置和后置步骤
@pytest.fixture(scope="session")
def get_advices_patch_setup(env):
    algo_domain = env['host']['algo_users']
    vti_events = events.get_advices_patch(algo_domain, ' ')
    return vti_events

