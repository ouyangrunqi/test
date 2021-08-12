import pytest
from api.advices_post import AdvicesPost

# 新建api 类的对象
events = AdvicesPost()


# 冒烟测试的前置和后置步骤
@pytest.fixture(scope="session")
def get_advices_post_setup(env):
    algo_domain = env['host']['algo_users']
    vti_events = events.get_advices_post(algo_domain, ' ')
    return vti_events
