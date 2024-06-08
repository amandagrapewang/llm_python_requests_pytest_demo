class DataHandle:
    def __init__(self, data):
        self.data = data

    def replace_params(self, params_list):
        # 替换params中的参数
        return {k: v.replace('${' + params_list[k] + '}', params_list[k]) for k, v in self.data.items()}