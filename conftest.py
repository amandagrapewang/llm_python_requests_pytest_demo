import pytest

@pytest.fixture
def login_guanliren():
    # 模拟登录并返回包含Authorization的headers
    return {"Authorization": "Bearer mock_token"}