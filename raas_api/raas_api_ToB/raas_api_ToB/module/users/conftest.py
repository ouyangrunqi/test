import pytest
from api.users_select import UsersSelect

# 新建api 类的对象
events = UsersSelect()


# 冒烟测试的前置和后置步骤
@pytest.fixture(scope="session")
def get_users_select_setup(env):
    algo_domain = env['host']['algo_users']
    vti_events = events.get_users_select(algo_domain, ' ')
    return vti_events
