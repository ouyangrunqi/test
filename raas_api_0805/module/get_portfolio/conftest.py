import pytest
from api.algo_events import AlgoEvents

# 新建api 类的对象
events = AlgoEvents()


# 冒烟测试的前置和后置步骤
@pytest.fixture(scope="session")
def get_events_smoke():
    pass
