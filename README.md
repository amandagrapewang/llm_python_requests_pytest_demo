# python_requests_pytest_demo

使用 `pytest` 和 `requests-mock` 进行接口自动化测试，支持从 Excel 文件读取测试数据

## 环境配置

确保您的开发环境中安装了以下软件和库：

- Python 3.8 或更高版本
- Pytest
- Requests
- Openpyxl
- Requests-mock
- configparser（Python 标准库中已包含）

您可以通过以下命令安装所需的 Python 库：

```bash
pip install -r requirements.txt
```

## 项目结构

```bash
project/
│
├── config/               # 配置文件目录
│   └── config.ini
├── outputs/              # 输出目录，包括日志
│   └── logs
├── resources/            # 测试数据和资源文件目录
│   └── ecommerce.xlsx    # Excel格式的测试数据文件
├── testcases/            # 测试脚本目录
│   └── test_ecommerce.py  # 测试用例脚本文件
├── utils/                # 工具类目录
│   ├── http_request.py   # HTTP请求工具类
│   ├── do_excel.py       # Excel文件处理工具类
│   └── data_handle.py    # 数据处理工具类
└── conftest.py           # pytest配置和fixture文件
```
## 运行测试
- 确保所有文件都在正确的位置。
- 打开终端或命令提示符。
- 切换到项目根目录。
- 运行以下命令来执行测试（或直接RUN test_ecommerce.py）：

```bash
pytest testcases/test_ecommerce.py -vs
```
