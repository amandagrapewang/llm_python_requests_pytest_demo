import pytest
import requests_mock
from utils.http_request import HttpRequest
from utils.do_excel import DoExcel
import os
import json
import logging


def config_ini(section, option):
    return {
        'api': {
            'base_url': 'http://mocked-api.ecommerce.com'
        }}[section][option]


# 配置日志记录
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(os.path.dirname(__file__), '..','outputs', 'logs', 'test_log.log'), mode='a'),  # 日志文件路径
            logging.StreamHandler()  # 同时输出到控制台
        ]
    )


@pytest.fixture(scope="class")
def setup_class():
    base_url = config_ini('api', 'base_url')
    excel = DoExcel(os.path.join(os.path.dirname(__file__), '..', 'resources', 'ecommerce.xlsx'))
    data = excel.get_data_from_excel()
    params_list = {}
    return base_url, data, params_list


# 在测试开始前配置日志
setup_logging()


class TestEcommerce:

    @pytest.fixture(autouse=True)
    def setup(self, setup_class):
        self.base_url, self.data, self.params_list = setup_class

    def test_login(self):
        test_data = self.data[0]
        # test_data['Headers'] 是一个 JSON 字符串
        headers = json.loads(test_data['Headers'])
        logging.info(f"开始执行登录测试用例: {test_data['Desc']}")
        with requests_mock.Mocker() as m:
            m.post(f"{self.base_url}{test_data['Path']}",
                   json={"data": {"access_token": "mocked_token"}}, status_code=200)
            response = HttpRequest(self.base_url).http_request(
                test_data['Method'], test_data['Path'], json=test_data['Params'], headers=headers)
            self.params_list['token'] = response.json()['data']['access_token']
            assert response.status_code == 200
        logging.info("登录测试用例执行成功。")

    def test_add_to_cart(self):
        if 'token' in self.params_list:
            test_data = self.data[1]
            headers = {'Authorization': f'Bearer {self.params_list["token"]}'}
            logging.info(f"开始执行添加商品到购物车测试用例: {test_data['Desc']}")
            with requests_mock.Mocker() as m:
                m.post(f"{self.base_url}{test_data['Path']}", status_code=200)
                response = HttpRequest(self.base_url).http_request(
                    test_data['Method'], test_data['Path'], json=test_data['Params'], headers=headers)
                assert response.status_code == 200
            logging.info("添加商品到购物车测试用例执行成功。")

    def test_place_order(self):
        if 'token' in self.params_list:
            test_data = self.data[2]
            headers = {'Authorization': f'Bearer {self.params_list["token"]}'}
            logging.info(f"开始执行下单购买测试用例: {test_data['Desc']}")
            with requests_mock.Mocker() as m:

                m.post(f"{self.base_url}{test_data['Path']}", status_code=200)
                response = HttpRequest(self.base_url).http_request(
                    test_data['Method'], test_data['Path'], json=test_data['Params'], headers=headers)
                assert response.status_code == 200
            logging.info("下单购买测试用例执行成功。")

if __name__ == "__main__":
    pytest.main(['-vs', 'test_ecommerce.py'])
